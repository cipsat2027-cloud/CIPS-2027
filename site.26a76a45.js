const FORM_ENDPOINT = window.CIPS_FORM_ENDPOINT || "";
const refCode = () => {
const abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", n = new Uint32Array(5);
(window.crypto || window.msCrypto).getRandomValues(n);
return Array.from(n, (v) => abc[v % 36]).join("");
};
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
(() => {
const header = document.querySelector("[data-header]");
const toggles = document.querySelectorAll("[data-menu-toggle]");
if (header) {
const onScroll = () => header.classList.toggle("stuck", window.scrollY > 24);
onScroll();
window.addEventListener("scroll", onScroll, { passive: true });
}
const setOpen = (open) => {
document.body.classList.toggle("menu-open", open);
toggles.forEach((t) => t.setAttribute("aria-expanded", String(open)));
};
toggles.forEach((t) => t.addEventListener("click", () => setOpen(!document.body.classList.contains("menu-open"))));
document.querySelectorAll("[data-menu] a").forEach((a) => a.addEventListener("click", () => setOpen(false)));
window.addEventListener("keydown", (e) => e.key === "Escape" && setOpen(false));
})();
(() => {
const els = document.querySelectorAll(".reveal");
if (!("IntersectionObserver" in window) || reduceMotion) return els.forEach((el) => el.classList.add("in"));
const io = new IntersectionObserver(
(entries) => entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }),
{ threshold: 0.12, rootMargin: "0px 0px -6% 0px" }
);
els.forEach((el) => io.observe(el));
})();
(() => {
const els = document.querySelectorAll("[data-count]");
if (!els.length) return;
const run = (el) => {
const target = +el.dataset.count;
const fmt = (n) => n.toLocaleString("en-US");
if (reduceMotion) return (el.textContent = fmt(target));
const t0 = performance.now(), dur = 1600;
const tick = (t) => {
const p = Math.min((t - t0) / dur, 1);
el.textContent = fmt(Math.round(target * (1 - Math.pow(1 - p, 4))));
if (p < 1) requestAnimationFrame(tick);
};
requestAnimationFrame(tick);
};
const io = new IntersectionObserver((entries) => entries.forEach((e) => { if (e.isIntersecting) { run(e.target); io.unobserve(e.target); } }), { threshold: 0.6 });
els.forEach((el) => io.observe(el));
})();
(() => {
const deck = document.getElementById("deck");
const dots = document.querySelectorAll(".deck-dots button");
if (!deck || !dots.length) return;
const cards = [...deck.children];
const setActive = () => {
let best = 0, dist = Infinity;
cards.forEach((c, i) => { const d = Math.abs(c.offsetLeft - deck.scrollLeft - 20); if (d < dist) { dist = d; best = i; } });
if (deck.scrollLeft + deck.clientWidth >= deck.scrollWidth - 4) best = cards.length - 1;
dots.forEach((d, i) => (i === best ? d.setAttribute("aria-current", "true") : d.removeAttribute("aria-current")));
};
deck.addEventListener("scroll", () => requestAnimationFrame(setActive), { passive: true });
dots.forEach((d, i) => d.addEventListener("click", () => deck.scrollTo({ left: cards[i].offsetLeft - 20, behavior: reduceMotion ? "auto" : "smooth" })));
setActive();
})();
if (window.matchMedia("(max-width: 560px)").matches) document.querySelectorAll(".dg-sec[open]").forEach((d) => d.removeAttribute("open"));
(() => {
const root = document.querySelector("[data-path]");
if (!root) return;
const tabs = [...root.querySelectorAll('[role="tab"]')];
const panels = tabs.map((t) => document.getElementById(t.getAttribute("aria-controls")));
let cur = 0;
const show = (i, focus) => {
i = Math.max(0, Math.min(tabs.length - 1, i));
if (i === cur && !focus) return;
cur = i;
root.style.setProperty("--i", i);
tabs.forEach((t, k) => {
t.setAttribute("aria-selected", String(k === i));
t.tabIndex = k === i ? 0 : -1;
t.classList.toggle("done", k < i);
panels[k].hidden = k !== i;
panels[k].classList.toggle("show", k === i);
});
if (focus) tabs[i].focus();
};
tabs.forEach((t, k) => {
t.addEventListener("click", () => show(k));
t.addEventListener("keydown", (e) => {
const d = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
if (d) { e.preventDefault(); show(cur + d, true); }
if (e.key === "Home" || e.key === "End") { e.preventDefault(); show(e.key === "Home" ? 0 : tabs.length - 1, true); }
});
});
root.addEventListener("click", (e) => {
const go = e.target.closest("[data-go]");
if (!go) return;
show(+go.dataset.go);
const top = root.getBoundingClientRect().top;
if (top < 0) root.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
});
let x0 = null, y0 = 0;
root.addEventListener("touchstart", (e) => { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
root.addEventListener("touchend", (e) => {
if (x0 === null) return;
const dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0;
if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) show(cur + (dx < 0 ? 1 : -1));
x0 = null;
}, { passive: true });
})();
const CIPSPay = (() => {
const FEE = { delegate: ["10,000", "11,800"], individual: ["25,000", "29,500"], company: ["50,000", "59,000"] };
let loading = null;
const loadCheckout = () => (loading ||= new Promise((resolve, reject) => {
const s = document.createElement("script");
s.src = "https://checkout.razorpay.com/v1/checkout.js";
s.onload = () => resolve(window.Razorpay);
s.onerror = () => { loading = null; reject(new Error("checkout")); };
document.head.appendChild(s);
}));
const api = async (params) => {
const ctl = new AbortController(), t = setTimeout(() => ctl.abort(), 45000);
try { return await (await fetch(`${FORM_ENDPOINT}?${new URLSearchParams(params)}`, { signal: ctl.signal })).json(); }
finally { clearTimeout(t); }
};
const phone = (v) => { const d = String(v).replace(/[^\d+]/g, ""); return /^\d{10}$/.test(d) ? "+91" + d : /^0\d{10}$/.test(d) ? "+91" + d.slice(1) : d; };
const esc = (v) => String(v).replace(/[&<>"]/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[ch]);
let wait;
const waiting = (on) => {
if (!wait) {
wait = document.createElement("div");
wait.className = "pay-wait";
wait.setAttribute("role", "alertdialog");
wait.setAttribute("aria-modal", "true");
wait.setAttribute("aria-label", "Confirming your payment");
wait.innerHTML = '<div class="pay-wait-in"><span class="pay-spin" aria-hidden="true"></span><b>Confirming your payment</b><p>This usually takes 10 to 20 seconds. Please keep this page open.</p></div>';
document.body.appendChild(wait);
}
wait.classList.toggle("show", on);
document.documentElement.classList.toggle("pay-waiting", on);
};
const mount = (box, ctx) => {
const btn = box.querySelector("[data-pay-now]"), label = box.querySelector("[data-pay-label]"), msg = box.querySelector("[data-pay-msg]");
const idle = `Pay ₹${FEE[ctx.kind][1]} securely`;
const say = (html, bad) => { msg.innerHTML = html; msg.hidden = !html; msg.classList.toggle("bad", !!bad); };
const busy = (text) => { btn.disabled = !!text; btn.classList.toggle("is-busy", !!text); label.textContent = text || idle; };
const paid = (d = {}) => {
if (box._pay.onSuccess) { box._pay.onSuccess(d); return; }
const c = box._pay, amount = d.amount ? Number(d.amount).toLocaleString("en-IN") : FEE[c.kind][1];
box.classList.add("is-paid");
btn.hidden = true;
box.querySelector(".paybox-sub").hidden = true;
say("");
box.querySelector(".pay-done")?.remove();
box.insertAdjacentHTML("beforeend", `<div class="pay-done" tabindex="-1">
<span class="pay-done-tick" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>
<h3>Payment <em>Successful</em></h3>
<p class="pay-done-amt">&#8377;${amount} paid</p>
<dl><div><dt>Reference</dt><dd>${esc(c.ref)}</dd></div>${d.payment_id ? `<div><dt>Payment ID</dt><dd>${esc(d.payment_id)}</dd></div>` : ""}</dl>
<p>${c.kind === "delegate" ? "Your delegate pass and receipt are" : "Your payment confirmation and receipt are"} on their way to ${c.email ? `<b>${esc(c.email)}</b>` : "your inbox"}.
${c.kind === "delegate" ? "Bring it on your phone or printed, with photo ID, to the registration desk at ITC Maratha." : "Your nomination now goes to the judging panel."}</p>
</div>`);
box.closest(".success, .pay-out")?.querySelectorAll(".pay-later, .nm-pay-t, .pay-msg, [data-po='note']").forEach((n) => (n.hidden = true));
const done = box.querySelector(".pay-done");
done.focus({ preventScroll: true });
done.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "center" });
c.onPaid?.();
};
box.classList.remove("is-paid");
box.querySelector(".pay-done")?.remove();
btn.hidden = false;
box.querySelector(".paybox-sub").hidden = false;
busy("");
say("");
box._pay = ctx;
if (!FORM_ENDPOINT) { btn.hidden = true; say("Online payment isn’t switched on yet: our team will email you payment instructions using your reference."); return; }
loadCheckout().catch(() => {});
ctx.order = Promise.resolve(ctx.ready).then(() => api({ action: "order", ref: ctx.ref })).catch(() => null);
if (box.dataset.mounted) return;
box.dataset.mounted = "1";
btn.addEventListener("click", async () => {
const c = box._pay;
say("");
if (c.ready) {
busy(c.uploading ? "Finishing your upload…" : "Saving your details…");
try { await c.ready; }
catch (err) {
busy("");
say("We couldn’t send your details. Please check your connection, then press Pay again to retry.", true);
c.ready = c.resend ? c.resend() : null;
c.order = null;
return;
}
}
busy("Opening secure payment…");
let order, Razorpay;
try {
const pre = c.order && (await c.order);
[order, Razorpay] = await Promise.all([pre && pre.result === "order" ? pre : api({ action: "order", ref: c.ref }), loadCheckout()]);
} catch (err) { busy(""); say("We couldn’t start the payment. Please check your connection and try again.", true); return; }
c.order = null;
if (order.result === "paid") { busy(""); paid(); return; }
if (order.result !== "order") {
busy("");
say(order.result === "notfound" ? "We couldn’t find this reference yet. Please try again in a minute."
: order.result === "closed" || order.result === "refunded" ? "This booking is no longer active. Reply to any email from us if you need help."
: "We couldn’t start the payment. Please try again in a moment.", true);
return;
}
const rz = new Razorpay({
key: order.key, order_id: order.order_id, amount: order.amount, currency: order.currency,
name: "CIPS Summit 2027", description: order.description,
image: new URL("assets/email/cips-logo-light.png", location.href).href,
prefill: Object.assign({}, c.prefill, c.prefill && c.prefill.contact ? { contact: phone(c.prefill.contact) } : {}),
notes: { reference: c.ref }, theme: { color: "#0b5cff" },
modal: { ondismiss: () => { busy(""); if (!box.classList.contains("is-paid") && msg.hidden) say("Payment not completed. You can try again whenever you’re ready."); } },
handler: async (r) => {
busy("Confirming your payment…");
say("");
waiting(true);
try {
const v = await api({ action: "verify", ref: c.ref, order_id: r.razorpay_order_id, payment_id: r.razorpay_payment_id, signature: r.razorpay_signature });
if (v.result === "paid") {
fetch(`${FORM_ENDPOINT}?${new URLSearchParams({ action: "send", ref: c.ref })}`, { keepalive: true }).catch(() => {});
waiting(false); busy(""); paid(v); return;
}
} catch (err) {  }
waiting(false);
busy("");
btn.hidden = true;
say("<b>Thank you, we’ve received your payment.</b> It’s still being confirmed: you’ll get an email as soon as it is. There’s no need to pay again.");
},
});
rz.on("payment.failed", (r) => { busy(""); say(`Payment didn’t go through${r && r.error && r.error.description ? ": " + r.error.description.replace(/[<>&]/g, "") : ""}. You can try again.`, true); });
rz.open();
});
};
return { mount, FEE };
})();
const inFlight = new Set();
window.addEventListener("beforeunload", (e) => { if (inFlight.size) { e.preventDefault(); e.returnValue = ""; } });
const keepOpen = (p) => { inFlight.add(p); p.then(() => inFlight.delete(p), () => inFlight.delete(p)); return p; };
let pageTitle = "";
const printAlone = (html, cls, title) => {
document.querySelectorAll("#print-pass").forEach((n) => n.remove());
const sheet = document.createElement("div");
if (!document.body.classList.contains("printing-pass")) pageTitle = document.title;
if (title) document.title = title;
sheet.id = "print-pass";
if (cls) sheet.className = cls;
sheet.innerHTML = html;
document.body.appendChild(sheet);
document.body.classList.add("printing-pass");
const done = () => { document.body.classList.remove("printing-pass"); sheet.remove(); document.title = pageTitle; };
window.addEventListener("afterprint", done, { once: true });
window.print();
setTimeout(() => { if (!matchMedia("print").matches && document.body.contains(sheet)) done(); }, 1500);
};
const inr = (n) => "\u20b9" + Math.round(Number(n)).toLocaleString("en-IN");
const inWords = (num) => {
const ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
const tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
const two = (n) => n < 20 ? ones[n] : tens[Math.floor(n / 10)] + (n % 10 ? "-" + ones[n % 10] : "");
const three = (n) => [n >= 100 ? ones[Math.floor(n / 100)] + " hundred" : "", two(n % 100)].filter(Boolean).join(" ");
let n = Math.round(Number(num)), out = [];
[[10000000, "crore"], [100000, "lakh"], [1000, "thousand"]].forEach(([v, w]) => { if (n >= v) { out.push(three(Math.floor(n / v)) + " " + w); n %= v; } });
if (n) out.push(three(n));
return "Rupees " + (out.join(" ") || "zero") + " only";
};
const paidOn = () => new Date().toLocaleString("en-IN", { day: "2-digit", month: "short", year: "numeric", hour: "2-digit", minute: "2-digit" });
const fillReceipt = (root, r) => {
const total = Math.round(Number(r.total)), base = Math.round(total / 1.18);
const v = { name: r.name, org: r.org, email: r.email, item: r.item, itemSub: r.itemSub, base: inr(base), gst: inr(total - base), total: inr(total), words: inWords(total) };
Object.entries(v).forEach(([k, x]) => root.querySelectorAll(`[data-rc="${k}"]`).forEach((n) => { n.textContent = x || ""; n.hidden = !x; }));
root.querySelectorAll('[data-conf="pid"]').forEach((n) => (n.textContent = r.pid || ""));
root.querySelectorAll('[data-conf-row="pid"]').forEach((n) => (n.hidden = !r.pid));
root.querySelectorAll('[data-conf="when"]').forEach((n) => (n.textContent = r.when));
};
document.querySelector("[data-print-receipt]")?.addEventListener("click", (e) => {
const rc = e.currentTarget.closest("[data-receipt]");
printAlone(rc.outerHTML
+ '<p class="rcpt-foot">CIPS Summit 2027, ITC Maratha, Mumbai. Questions about this receipt? Reply to your confirmation email.</p>', "is-receipt", "CIPS-2027-Receipt-" + rc.querySelector("[data-ref]").textContent.trim());
});
document.querySelectorAll("[data-copy]").forEach((b) => b.addEventListener("click", () => {
const ref = b.parentElement.querySelector("[data-ref]").textContent;
navigator.clipboard?.writeText(ref).then(() => { b.textContent = "Copied"; setTimeout(() => (b.textContent = "Copy"), 2000); });
}));
(() => {
const dlg = document.getElementById("aw-dlg");
const cards = [...document.querySelectorAll(".acats .ac")];
if (!dlg || !cards.length || typeof dlg.showModal !== "function") return;
const body = dlg.querySelector(".aw-dlg-bd"), key = dlg.querySelector(".aw-dlg-k"), pos = dlg.querySelector(".aw-dlg-pos");
const [prev, next] = dlg.querySelectorAll("[data-step]");
const nom = dlg.querySelector(".aw-dlg-nom");
let cur = 0;
const fill = (i) => {
cur = i;
const c = cards[i], tag = c.querySelector(".tag");
key.innerHTML = `<span class="tag ${tag.classList.contains("ind") ? "ind" : "com"}">${tag.textContent}</span> Award ${c.querySelector(".ac-n").textContent}`;
const [amt, gst] = c.querySelector(".ac-fee").textContent.split("+");
body.innerHTML = `<i>${c.querySelector("i").innerHTML}</i><h2 id="aw-dlg-t">${c.querySelector("h3").innerHTML}</h2>` +
`<p class="aw-dlg-about">${c.querySelector(".ac-about").innerHTML}</p>` +
`<div class="aw-dlg-fee"><b>${amt.trim()}</b><small>+ ${(gst || "").trim()} per nomination</small></div>` +
`<div class="ac-body">${c.querySelector(".ac-body").innerHTML}</div>`;
body.scrollTop = 0;
pos.textContent = `${i + 1} / ${cards.length}`;
prev.disabled = i === 0; next.disabled = i === cards.length - 1;
nom.href = "nominate.html?award=" + c.dataset.key;
};
const open = (i) => { fill(i); if (!dlg.open) { document.documentElement.classList.add("dlg-lock"); dlg.showModal(); } };
dlg.addEventListener("close", () => document.documentElement.classList.remove("dlg-lock"));
cards.forEach((c, i) => {
const sum = c.querySelector("summary");
sum.addEventListener("click", (e) => { e.preventDefault(); open(i); });
c.addEventListener("click", (e) => { if (!e.target.closest("summary, a, button")) open(i); });
});
dlg.addEventListener("click", (e) => {
if (e.target === dlg || e.target.closest("[data-close]")) dlg.close();
const step = e.target.closest("[data-step]");
if (step && !step.disabled) fill(cur + +step.dataset.step);
});
dlg.addEventListener("keydown", (e) => {
const d = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
if (d && cards[cur + d]) { e.preventDefault(); fill(cur + d); }
});
})();
(() => {
const form = document.getElementById("nominate-form");
if (!form) return;
const AW = JSON.parse(document.getElementById("nm-awards").textContent);
const byKey = Object.fromEntries(AW.map((a) => [a.key, a]));
const steps = [...form.querySelectorAll(".nm-step")];
const dots = [...document.querySelectorAll(".nm-steps li")];
const back = form.querySelector("[data-back]"), next = form.querySelector("[data-next]"), submit = form.querySelector("[data-submit]");
const pos = form.querySelector(".nm-pos"), alertBox = form.querySelector(".form-alert"), card = document.getElementById("nm-card");
const DRAFT = "cips-nomination-draft", TOTAL = 30 * 1024 * 1024, MB = (n) => (n < 1048576 ? Math.max(1, Math.round(n / 1024)) + " KB" : (n / 1048576).toFixed(1) + " MB");
const files = { photo: [], docs: [], endorse: [] }, LIMIT = { photo: 1, docs: 3, endorse: 2 };
const esc = (v) => String(v).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const fill = (k, v) => document.querySelectorAll(`[data-fill="${k}"]`).forEach((n) => (n.textContent = v));
const relevant = (el) => !el.closest("[data-for][hidden], [data-for-award][hidden], [data-if-member][hidden]");
const applyMember = () => form.querySelectorAll("[data-if-member]").forEach((n) => (n.hidden = form.elements.membership.value !== "CIPS member"));
let cur = 1, award = null;
const applyAward = (key) => {
award = byKey[key] || null;
const t = award ? award.type : "Individual";
form.querySelectorAll("[data-for]").forEach((n) => (n.hidden = n.dataset.for !== t));
form.querySelectorAll("[data-for-award]").forEach((n) => (n.hidden = !award || !n.dataset.forAward.split(",").includes(award.key)));
const sumName = document.querySelector('[data-sum="name"]'), sumMeta = document.querySelector('[data-sum="meta"]'), sumFee = document.querySelector('[data-sum="fee"]');
if (!award) return;
fill("name", award.name); fill("elig", award.elig); fill("fee", "₹" + award.fee);
fill("ev", award.ev || "Quantified achievements and case studies, with supporting testimonials where relevant.");
form.querySelector('[data-fill="crit"]').innerHTML = award.crit.map((c) => `<li>${esc(c)}</li>`).join("");
form.querySelector("[data-photo-label]").textContent = t === "Individual" ? "Individual Headshot" : "Team Photograph";
const eb = form.querySelector('[data-file="endorse"]');
eb.querySelector(".req-star").hidden = !award.endorse;
eb.querySelector("input").required = award.endorse;
sumName.textContent = award.name;
sumMeta.textContent = `${t} Award ${award.n}`;
sumFee.hidden = false;
sumFee.innerHTML = `<b>₹${award.fee}</b> <small>+ GST nomination fee</small>`;
showPage();
};
const q = form.querySelector("#nm-q"), qx = form.querySelector(".nm-find-x"), qn = form.querySelector(".nm-find-n");
if (q) {
const norm = (s) => String(s).toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
const SYN = { esg: ["sustainab"], green: ["sustainab"], climate: ["sustainab"], environment: ["sustainab"], tech: ["technolog", "digital"],
ai: ["digital", "technolog"], software: ["technolog", "solution"], saas: ["technolog"], vendor: ["solution", "technolog"], young: ["emerging"], leadership: ["leader"],
junior: ["emerging"], graduate: ["emerging"], chief: ["cpo"], head: ["cpo", "leader"], government: ["public"], psu: ["public"], gem: ["public"],
training: ["knowledge"], learning: ["knowledge"], sme: ["small"], msme: ["small"], startup: ["small"] };
const STOP = ["the", "of", "and", "for", "a", "best", "award", "awards", "category", "sector", "project", "program", "programme"];
const cats = [...form.querySelectorAll(".nm-cat")].map((el, i) => {
const a = byKey[el.querySelector("input").value], t = el.querySelector(".nm-cat-t");
return { el, i, t, title: t.textContent, n: parseInt(a.n, 10), type: a.type === "Individual" ? "individual" : "company organisation",
name: norm(a.name), more: norm([a.elig, ...(a.crit || []), a.ev || ""].join(" ")) };
});
const groups = [...form.querySelectorAll(".nm-cats")];
const run = () => {
const raw = q.value.trim(), terms = norm(raw).split(/[\s,/]+/).filter((w) => w && !STOP.includes(w)).map((w) => (w.length > 4 ? w.replace(/s$/, "") : w));
const alts = (w) => [w, ...(SYN[w] || [])];
const inName = (c, w) => (/^\d{1,2}$/.test(w) ? +w === c.n : /^(individual|company|organi[sz]ation)$/.test(w) ? c.type.includes(w.replace("organiz", "organis"))
: alts(w).some((x) => c.name.includes(x)));
cats.forEach((c) => {
const all = terms.every((w) => inName(c, w) || (!/^\d{1,2}$/.test(w) && alts(w).some((x) => c.more.includes(x))));
c.score = !terms.length ? 1 : all ? 1 + terms.filter((w) => inName(c, w)).length : 0;
});
if (cats.some((c) => c.score > 1)) cats.forEach((c) => { if (c.score === 1) c.score = 0; });
let shown = 0;
cats.forEach((c) => {
const score = c.score;
c.el.hidden = !score;
if (score) shown++;
const hits = terms.filter((w) => w.length > 1 && !/^\d+$/.test(w));
c.t.innerHTML = hits.length ? esc(c.title).replace(new RegExp("(" + hits.map((w) => w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|") + ")", "gi"), "<mark>$1</mark>") : esc(c.title);
});
groups.forEach((g) => {
const list = cats.filter((c) => c.el.parentNode === g).sort((a, b) => (terms.length ? b.score - a.score : 0) || a.i - b.i);
list.forEach((c) => g.appendChild(c.el));
g.hidden = !list.some((c) => c.score);
});
qx.hidden = !raw;
qn.hidden = !raw;
qn.innerHTML = !raw ? "" : shown ? `${shown} of ${cats.length} awards match <b>“${esc(raw)}”</b>`
: `No award matches <b>“${esc(raw)}”</b>. Try another word, or <button type="button" class="nm-find-all">show all 12</button>.`;
form.querySelectorAll(".nm-find-tags button").forEach((b) => b.setAttribute("aria-pressed", String(norm(raw) === b.dataset.q)));
};
const visible = () => cats.filter((c) => !c.el.hidden).sort((a, b) => [...a.el.parentNode.children].indexOf(a.el) - [...b.el.parentNode.children].indexOf(b.el)
|| groups.indexOf(a.el.parentNode) - groups.indexOf(b.el.parentNode));
const clear = () => { q.value = ""; run(); q.focus(); };
q.addEventListener("input", run);
q.addEventListener("keydown", (e) => {
if (e.key === "Escape" && q.value) { e.preventDefault(); e.stopPropagation(); clear(); }
if (e.key === "Enter" || e.key === "ArrowDown") {
e.preventDefault();
const v = visible();
if (!v.length) return;
const input = v[0].el.querySelector("input");
if (e.key === "Enter" && v.length === 1) input.click();
input.focus();
}
});
qx.addEventListener("click", clear);
qn.addEventListener("click", (e) => e.target.closest(".nm-find-all") && clear());
form.querySelectorAll(".nm-find-tags button").forEach((b) => b.addEventListener("click", () => {
q.value = b.getAttribute("aria-pressed") === "true" ? "" : b.dataset.q;
run();
}));
run();
}
const errBox = (k, msg) => { const n = form.querySelector(`[data-err="${k}"]`); if (n) { n.textContent = msg; n.classList.toggle("show", !!msg); } };
const setErr = (el, msg) => {
const box = el.closest(".field");
if (box) { box.classList.toggle("invalid", !!msg); box.querySelector(".err").textContent = msg; }
el.setAttribute("aria-invalid", msg ? "true" : "false");
};
const msgFor = (el) => {
if (el.type === "file") { const s = el.name; return el.required && !files[s].length ? (s === "photo" ? "Please attach a photograph." : "Please attach at least one file.") : ""; }
const v = (el.value || "").trim();
if (el.required && !v) return el.tagName === "SELECT" ? "Please choose an option." : "This field is required.";
if (!v) return "";
if (el.type === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) return "Please enter a valid email address.";
if (el.type === "tel") { const d = v.replace(/\D/g, ""); if (d.length < 7 || d.length > 15 || /[^\d\s()+\-.]/.test(v)) return "Please enter a valid mobile number, including country code."; }
if (el.type === "url" && !/^https?:\/\/\S+\.\S+/.test(v)) return "Please enter a full link starting with https://";
if (el.tagName === "TEXTAREA" && v.length < 80) return "Please add a little more detail (at least 80 characters).";
return "";
};
const validateStep = (n, focus = true, sec = steps[n - 1]) => {
let first = null;
if (n === 1) { const m = award ? "" : "Please select an award category."; errBox("award", m); if (m) first = sec.querySelector("input[name=award]"); }
sec.querySelectorAll("input:not([type=radio]):not([type=checkbox]), select, textarea").forEach((el) => {
if (!el.name || el.name === "website" || !relevant(el)) return;
const m = msgFor(el); setErr(el, m); if (m && !first) first = el;
});
const checks = [...sec.querySelectorAll(".check input[required]")].filter(relevant);
const bad = checks.filter((c) => !c.checked);
const errKey = sec.querySelector(".nm-err")?.dataset.err;
if (checks.length && errKey) errBox(errKey, bad.length ? `Please tick the confirmation${bad.length > 1 ? "s" : ""} above to continue.` : "");
if (bad.length && !first) first = bad[0];
if (first && focus) first.focus();
return !first;
};
form.addEventListener("input", (e) => { const f = e.target.closest(".field.invalid"); if (f) setErr(e.target, msgFor(e.target)); });
const isImage = (f) => f.type.startsWith("image" + "/") || /\.(heic|heif)$/i.test(f.name);
const compress = (f) => new Promise((resolve, reject) => {
const url = URL.createObjectURL(f), img = new Image();
img.onload = () => {
URL.revokeObjectURL(url);
const w = img.naturalWidth, h = img.naturalHeight, k = Math.min(1, 2000 / Math.max(w, h));
if (f.type === "image/jpeg" && k === 1 && f.size <= 1.5 * 1048576) { resolve(f); return; }
const c = document.createElement("canvas");
c.width = Math.max(1, Math.round(w * k)); c.height = Math.max(1, Math.round(h * k));
const g = c.getContext("2d");
g.fillStyle = "#fff"; g.fillRect(0, 0, c.width, c.height);
g.drawImage(img, 0, 0, c.width, c.height);
c.toBlob((b) => (b ? resolve(new File([b], f.name.replace(/\.[^.]+$/, "") + ".jpg", { type: "image/jpeg" })) : reject(new Error("encode"))), "image/jpeg", 0.85);
};
img.onerror = () => { URL.revokeObjectURL(url); reject(new Error("decode")); };
img.src = url;
});
const used = () => Object.values(files).flat().reduce((n, f) => n + f.size, 0);
const renderFiles = (slot, busy) => {
form.querySelector(`[data-file="${slot}"] .files`).innerHTML = files[slot].map((f, i) =>
`<li><span>${esc(f.name)}</span><small>${f._from ? `${MB(f._from)} &rarr; ` : ""}${MB(f.size)}</small><button type="button" data-rm="${slot}:${i}" aria-label="Remove ${esc(f.name)}">&times;</button></li>`).join("")
+ (busy ? `<li class="busy"><span>Optimising ${esc(busy)}&hellip;</span></li>` : "");
};
const addFiles = async (slot, list) => {
const input = form.querySelector(`[data-file="${slot}"] input`), errs = [], picked = [...list];
input.value = "";
for (const f of picked) {
const pdf = f.type === "application/pdf" || /\.pdf$/i.test(f.name);
if (!(isImage(f) || (pdf && slot !== "photo"))) { errs.push(`${f.name}: please use ${slot === "photo" ? "a photo (JPEG, PNG, HEIC or WebP)" : "a PDF or an image"}.`); continue; }
if (slot !== "photo" && files[slot].length >= LIMIT[slot]) { errs.push(`You can attach up to ${LIMIT[slot]} files here.`); break; }
let out = f;
if (!pdf) {
renderFiles(slot, f.name);
try {
out = await compress(f);
if (out !== f && out.size >= f.size && /^image\/(jpeg|png)$/.test(f.type)) out = f;
if (out !== f) out._from = f.size;
}
catch (err) { errs.push(`${f.name} couldn't be read. Please save it as a JPEG or PNG and try again.`); continue; }
} else if (f.type !== "application/pdf") out = new File([f], f.name, { type: "application/pdf" });
const before = slot === "photo" ? used() - (files.photo[0] ? files.photo[0].size : 0) : used();
if (before + out.size > TOTAL) { errs.push(`${f.name} (${MB(out.size)}) would take your attachments over 30 MB in total. Please use a smaller PDF, for example with "Reduce file size" or "Save as optimised PDF".`); continue; }
if (slot === "photo") files.photo = [out]; else files[slot].push(out);
}
renderFiles(slot);
setErr(input, errs.join(" "));
};
form.querySelectorAll("[data-file]").forEach((box) => {
const slot = box.dataset.file, input = box.querySelector("input"), drop = box.querySelector(".drop");
input.addEventListener("change", () => addFiles(slot, input.files));
["dragenter", "dragover"].forEach((ev) => drop.addEventListener(ev, (e) => { e.preventDefault(); drop.classList.add("over"); }));
["dragleave", "drop"].forEach((ev) => drop.addEventListener(ev, (e) => { e.preventDefault(); drop.classList.remove("over"); }));
drop.addEventListener("drop", (e) => addFiles(slot, e.dataTransfer.files));
});
const save = () => {
try {
const d = {};
[...form.elements].forEach((el) => {
if (!el.name || el.type === "file" || el.name === "website" || el.name.startsWith("decl")) return;
if (el.type === "radio") { if (el.checked) d[el.name] = el.value; } else d[el.name] = el.type === "checkbox" ? el.checked : el.value;
});
localStorage.setItem(DRAFT, JSON.stringify(d));
} catch (e) {  }
};
const restore = () => {
try {
const d = JSON.parse(localStorage.getItem(DRAFT) || "null");
if (!d) return;
Object.entries(d).forEach(([k, v]) => {
const el = form.elements[k];
if (!el) return;
if (el instanceof RadioNodeList) { const r = [...el].find((x) => x.value === v); if (r) r.checked = true; }
else if (el.type === "checkbox") el.checked = !!v; else el.value = v;
});
} catch (e) {  }
};
const counters = () => form.querySelectorAll("textarea").forEach((t) => { form.querySelector(`[data-count-for="${t.name}"]`).textContent = `${t.value.length} / ${t.maxLength}`; });
form.addEventListener("input", (e) => { if (e.target.tagName === "TEXTAREA") counters(); save(); });
form.addEventListener("change", (e) => {
if (e.target.name === "award") { applyAward(e.target.value); errBox("award", ""); }
if (e.target.name === "membership") applyMember();
if (e.target.name === "selfNominate" && e.target.checked)
[["nomineeName", "nomName"], ["nomineeEmail", "nomEmail"], ["nomineeDesignation", "nomDesignation"], ["nomineeOrg", "nomOrg"]].forEach(([a, b]) => (form.elements[a].value = form.elements[b].value));
save();
});
const labelOf = (el) => { const l = form.querySelector(`label[for="${el.id}"]`); return l ? l.textContent.replace("*", "").trim() : el.name; };
const fieldsIn = (n) => [...steps[n - 1].querySelectorAll("input:not([type=radio]):not([type=checkbox]):not([type=file]), select, textarea")]
.filter((el) => el.name && el.name !== "website" && relevant(el) && el.value.trim()).map((el) => [labelOf(el), el.value.trim()]);
const names = (l) => l.map((f) => f.name).join(", ");
const buildReview = () => {
const groups = [
[1, "Award Category", [["Category", `${award.name} (${award.type} Award ${award.n})`], ["Nomination fee", `₹${award.fee} + GST`]]],
[2, "Nomination Form", fieldsIn(2)],
[3, "Supporting Evidence", [["Photograph", names(files.photo)], ["Supporting documents", names(files.docs)], ["Endorsements", names(files.endorse) || "None attached"], ...fieldsIn(3)]],
];
form.querySelector("[data-review]").innerHTML = groups.map(([n, t, rows]) =>
`<section><header><h3><span>0${n}</span>${t}</h3><button type="button" class="nm-edit" data-goto="${n}">Edit</button></header>` +
`<dl>${rows.map(([k, v]) => `<div><dt>${esc(k)}</dt><dd>${esc(v)}</dd></div>`).join("")}</dl></section>`).join("");
};
const mq = window.matchMedia("(max-width: 760px)");
const now = document.querySelector(".nm-now"), chip = form.querySelector("[data-chip]");
let page = 0;
const pagesOf = (n) => (mq.matches ? [...steps[n - 1].querySelectorAll(":scope > .fs")].filter(relevant) : []);
const toTop = (focusEl) => {
card.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
if (focusEl) { focusEl.setAttribute("tabindex", "-1"); focusEl.focus({ preventScroll: true }); }
};
const showPage = () => {
const sec = steps[cur - 1], pages = pagesOf(cur), multi = pages.length > 1;
sec.querySelectorAll(":scope > .fs").forEach((f) => f.classList.toggle("nm-pg-off", multi && f !== pages[page]));
sec.querySelectorAll(":scope > h2, :scope > .note, :scope > .nm-elig").forEach((el) => el.classList.toggle("nm-pg-off", multi && page > 0));
const part = multi ? `Part ${page + 1} of ${pages.length}` : "";
pos.textContent = `Step ${cur} of ${steps.length}` + (part ? ` · ${part}` : "");
now.innerHTML = `<b>Step ${cur} of ${steps.length}</b><span>${esc(dots[cur - 1].querySelector("b").textContent)}</span>` + (part ? `<small>${part}</small>` : "");
back.hidden = cur === 1 && page === 0;
chip.hidden = !award || cur === 1;
if (award) { chip.querySelector("[data-chip-name]").textContent = award.name; chip.querySelector("[data-chip-fee]").textContent = `₹${award.fee} + GST`; }
};
const go = (n, scroll = true, pg = 0) => {
cur = n;
steps.forEach((s, i) => (s.hidden = i !== n - 1));
dots.forEach((d, i) => { d.classList.toggle("done", i < n - 1); if (i === n - 1) d.setAttribute("aria-current", "step"); else d.removeAttribute("aria-current"); });
next.hidden = n === steps.length; submit.hidden = n !== steps.length;
page = pg === "last" ? Math.max(pagesOf(n).length - 1, 0) : pg;
if (n === steps.length) buildReview();
showPage();
if (scroll) toTop(steps[n - 1].querySelector("h2"));
};
const nmWait = (p, ms) => Promise.race([p, new Promise((_, rej) => setTimeout(() => rej(new Error("timeout")), ms))]);
const nomWho = () => {
const v = (k) => (form.elements[k] ? form.elements[k].value.trim() : "");
return award ? { award: award.key, awardType: award.type, nomineeName: v("nomineeName"), nomineeEmail: v("nomineeEmail"), nomineeOrg: v("nomineeOrg"), orgName: v("orgName"), nomEmail: v("nomEmail") } : null;
};
const askNom = (extra) => fetch(FORM_ENDPOINT, { method: "POST", body: new URLSearchParams({ ...nomWho(), ...extra }) }).then((r) => r.json());
let nomAsked = { key: "", req: null }, nomTimer;
const nomCheck = () => {
const w = nomWho();
if (!FORM_ENDPOINT || !w || !(w.awardType === "Company" ? w.orgName : w.nomineeName && (w.nomineeEmail || w.nomineeOrg))) return null;
const key = JSON.stringify(w);
if (nomAsked.key !== key) nomAsked = { key, req: nmWait(askNom({ formType: "check-nomination" }), 12000).catch(() => null) };
return nomAsked.req;
};
["nomineeName", "nomineeEmail", "nomineeOrg", "orgName", "nomEmail"].forEach((n) => form.elements[n] && form.elements[n].addEventListener("change", () => {
clearTimeout(nomTimer);
nomTimer = setTimeout(nomCheck, 900);
}));
const showNomDuplicate = (d) => {
const ind = award && award.type === "Individual", them = ind ? "this nominee" : "this organisation";
let html;
if (!d.mine) html = ind
? "<b>This nominee has already been entered for a CIPS India Awards 2027 individual category.</b> Each nominee may enter only one individual category, so a second nomination can’t be submitted."
: "<b>This organisation has already been entered for this award.</b> It can still be entered for a different company category.";
else if (d.status === "paid") html = `<b>You’ve already nominated ${them} for the ${esc(d.award)}, and the nomination is complete.</b> The confirmation was emailed to ${esc(d.email)}.`;
else html = `<b>You’ve already started this nomination for the ${esc(d.award)}.</b> It’s waiting for payment, so there’s no need to submit it again: complete it with the payment link we emailed to ${esc(d.email)}.`;
if (d.mine) html += `<span class="dup-acts"><button type="button" class="btn ghost" data-dup-send>${d.status === "paid" ? "Email my confirmation again" : "Email me the payment link"}</button>`
+ `${d.status === "paid" ? "" : '<a href="pay.html">I have my reference</a>'}</span>`;
alertBox.innerHTML = html;
alertBox.classList.add("show", "is-info");
const b = alertBox.querySelector("[data-dup-send]");
if (b) b.addEventListener("click", async () => {
b.disabled = true;
b.textContent = "Sending…";
let r = null;
try { r = await nmWait(askNom({ formType: "remind-nomination" }), 40000); } catch (err) {  }
const ok = r && r.result === "sent";
b.textContent = ok ? `Sent to ${r.email}` : "Couldn’t send it. Please try again";
b.disabled = ok;
});
alertBox.scrollIntoView({ block: "center", behavior: reduceMotion ? "auto" : "smooth" });
};
const nomTaken = async () => {
const was = next.disabled;
next.disabled = submit.disabled = true;
const r = await nomCheck();
next.disabled = was; submit.disabled = false;
if (r && r.result === "duplicate") { showNomDuplicate(r); return true; }
return false;
};
next.addEventListener("click", async () => {
const pages = pagesOf(cur), multi = pages.length > 1, pg = multi ? pages[page] : steps[cur - 1];
alertBox.classList.remove("show", "is-info");
if (!validateStep(cur, true, pg)) return;
if ([form.elements.nomineeName, form.elements.orgName].some((el) => el && pg.contains(el) && relevant(el)) && (await nomTaken())) return;
if (multi && page < pages.length - 1) { page++; showPage(); toTop(pages[page].querySelector("legend")); }
else go(cur + 1);
});
back.addEventListener("click", () => {
if (page > 0) { page--; showPage(); toTop(pagesOf(cur)[page].querySelector("legend")); }
else go(cur - 1, true, "last");
});
mq.addEventListener?.("change", () => { page = 0; showPage(); });
if (mq.matches) document.querySelector(".nm-tipbox")?.removeAttribute("open");
form.addEventListener("click", (e) => {
const g = e.target.closest("[data-goto]");
if (g) go(+g.dataset.goto);
const rm = e.target.closest("[data-rm]");
if (rm) { const [s, i] = rm.dataset.rm.split(":"); files[s].splice(+i, 1); renderFiles(s); }
});
const readB64 = (f) => new Promise((res, rej) => { const r = new FileReader(); r.onload = () => res(String(r.result).split(",")[1]); r.onerror = rej; r.readAsDataURL(f); });
form.addEventListener("submit", async (e) => {
e.preventDefault();
alertBox.classList.remove("show", "is-info");
for (const n of [1, 2, 3]) if (!validateStep(n, false)) { go(n); validateStep(n); return; }
if (!validateStep(4)) return;
if (form.elements.website.value) return;
if (await nomTaken()) return;
const ref = "CIPS27-" + award.key.replace("-", "").toUpperCase() + "-" + refCode();
const data = { formType: "nomination", ref, award: award.key, awardName: award.name, awardType: award.type, fee: award.fee, submittedAt: new Date().toISOString() };
[...form.elements].forEach((el) => {
if (!el.name || el.type === "file" || el.name === "website" || el.name === "award" || !relevant(el)) return;
data[el.name] = el.type === "checkbox" ? (el.checked ? "Yes" : "No") : el.value.trim();
});
const label = submit.querySelector("span");
submit.disabled = true; back.disabled = true;
label.textContent = used() > 4 * 1048576 ? "Preparing attachments…" : "Submitting…";
try {
const enc = await Promise.all(Object.entries(files).flatMap(([slot, list]) => list.map((f) => readB64(f).then((b) => ({ slot, name: f.name, type: f.type, data: b })))));
data.files = JSON.stringify(enc);
const send = () => (FORM_ENDPOINT ? fetch(FORM_ENDPOINT, { method: "POST", mode: "no-cors", body: new URLSearchParams(data) })
: Promise.resolve(console.warn("[CIPS Awards] FORM_ENDPOINT is not set in js/config.js: this nomination was NOT sent anywhere.", { ...data, files: enc.map((f) => f.name) })));
const ready = keepOpen(send()), uploading = used() > 1048576;
try { localStorage.removeItem(DRAFT); } catch (err) {  }
const done = document.getElementById("nominate-success"), kind = award.type === "Individual" ? "individual" : "company";
const stepPay = done.querySelector('[data-nm-step="pay"]'), stepDone = done.querySelector('[data-nm-step="done"]');
const base = Number(String(award.fee).replace(/,/g, ""));
const nominee = kind === "individual" ? [data.nomineeName, data.nomineeOrg].filter(Boolean).join(", ") : [data.orgName, data.entryTitle].filter(Boolean).join(": ");
const nc = (k, v) => done.querySelectorAll(`[data-nc="${k}"]`).forEach((n) => (n.textContent = v));
form.hidden = true;
dots.forEach((d) => { d.classList.add("done"); d.removeAttribute("aria-current"); });
done.querySelectorAll("[data-ref]").forEach((n) => (n.textContent = ref));
fill("nomEmail", data.nomEmail);
nc("award", award.name);
nc("type", `${award.type} Award ${award.n}`);
nc("nominee", nominee);
nc("nominator", [data.nomName, data.nomOrg].filter(Boolean).join(", "));
nc("nominatorName", data.nomName);
nc("base", inr(base));
nc("gst", inr(base * 0.18));
nc("total", inr(base * 1.18));
done.querySelector("[data-pay-later]").href = "pay.html?ref=" + encodeURIComponent(ref);
stepPay.hidden = false;
stepDone.hidden = true;
CIPSPay.mount(done.querySelector("[data-paybox]"), { ref, kind, email: data.nomEmail, ready, uploading, resend: () => keepOpen(send()),
prefill: { name: data.nomName, email: data.nomEmail, contact: data.nomMobile },
onSuccess: (d) => {
fillReceipt(stepDone, { name: data.nomName, org: [data.nomDesignation, data.nomOrg].filter(Boolean).join(", "), email: data.nomEmail,
item: `Nomination fee: ${award.name}`, itemSub: `${award.type} Award ${award.n}, CIPS India Awards 2027. Nominee: ${nominee}`,
total: d.amount || base * 1.18, pid: d.payment_id, when: paidOn() });
const tick = done.querySelector(".flow-steps .done span").innerHTML;
done.querySelectorAll('[data-flow="pay"], [data-flow="done"]').forEach((li) => { li.className = "done"; li.querySelector("span").innerHTML = tick; });
stepPay.hidden = true;
stepDone.hidden = false;
stepDone.focus({ preventScroll: true });
done.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
} });
done.classList.add("show");
done.setAttribute("tabindex", "-1");
done.focus({ preventScroll: true });
card.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
} catch (err) {
alertBox.textContent = "Sorry, we couldn't submit your nomination just now. Please check your connection and try again. Your answers are still here.";
alertBox.classList.add("show");
submit.disabled = false; back.disabled = false;
label.textContent = "Submit Nomination";
}
});
restore();
const qs = new URLSearchParams(location.search).get("award");
if (qs && byKey[qs]) [...form.elements.award].find((x) => x.value === qs).checked = true;
const chosen = [...form.elements.award].find((x) => x.checked);
applyAward(chosen ? chosen.value : null);
applyMember();
counters();
go(qs && byKey[qs] ? 2 : 1, false);
})();
(() => {
const form = document.getElementById("register-form");
if (!form) return;
const COUNTRIES = ["India","United Kingdom","United Arab Emirates","Saudi Arabia","Qatar","Oman","Kuwait","Bahrain","Singapore","Malaysia","Australia","New Zealand","United States","Canada","Germany","France","Netherlands","Switzerland","Ireland","Italy","Spain","Sweden","Norway","Denmark","Finland","Belgium","Austria","Poland","Portugal","South Africa","Nigeria","Kenya","Egypt","Ghana","Tanzania","Uganda","Zambia","Sri Lanka","Bangladesh","Nepal","Pakistan","Bhutan","Maldives","Indonesia","Thailand","Vietnam","Philippines","Hong Kong SAR","China","Japan","South Korea","Brazil","Mexico","Turkey","Israel","Jordan","Other"];
const select = form.elements.country;
COUNTRIES.forEach((c) => select.add(new Option(c, c)));
const rules = {
firstName: (v) => v.trim() ? "" : "Please enter your first name.",
lastName: (v) => v.trim() ? "" : "Please enter your last name.",
email: (v) => !v.trim() ? "Please enter your official email address." : /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()) ? "" : "Please enter a valid email address.",
mobile: (v) => { const d = v.replace(/\D/g, ""); return !v.trim() ? "Please enter your mobile number." : d.length < 7 || d.length > 15 || /[^\d\s()+\-.]/.test(v) ? "Please enter a valid mobile number, including country code." : ""; },
country: (v) => v ? "" : "Please select your country.",
organisation: (v) => v.trim() ? "" : "Please enter your organisation or company.",
designation: (v) => v.trim() ? "" : "Please enter your designation.",
};
const check = (name) => {
const input = form.elements[name], field = input.closest(".field");
const msg = rules[name](input.value);
field.classList.toggle("invalid", !!msg);
field.querySelector(".err").textContent = msg;
input.setAttribute("aria-invalid", msg ? "true" : "false");
return !msg;
};
Object.keys(rules).forEach((name) => {
const input = form.elements[name];
input.addEventListener("blur", () => input.value && check(name));
input.addEventListener("input", () => input.closest(".field").classList.contains("invalid") && check(name));
});
const alertBox = form.querySelector(".form-alert");
const btn = form.querySelector("button[type=submit]");
const escH = (v) => String(v).replace(/[&<>"]/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[ch]);
const withTimeout = (p, ms) => Promise.race([p, new Promise((_, rej) => setTimeout(() => rej(new Error("timeout")), ms))]);
const who = () => {
const v = (k) => (form.elements[k] ? form.elements[k].value.trim() : "");
return { firstName: v("firstName"), lastName: v("lastName"), email: v("email"), mobile: v("mobile"), organisation: v("organisation") };
};
const askScript = (extra) => fetch(FORM_ENDPOINT, { method: "POST", body: new URLSearchParams({ ...who(), ...extra }) }).then((r) => r.json());
let dupAsked = { key: "", req: null };
const dupCheck = () => {
const w = who();
if (!FORM_ENDPOINT || !w.firstName || !w.lastName || !(w.email || w.mobile)) return null;
const key = JSON.stringify(w);
if (dupAsked.key !== key) dupAsked = { key, req: withTimeout(askScript({ formType: "check" }), 12000).catch(() => null) };
return dupAsked.req;
};
let dupTimer;
["firstName", "lastName", "email", "mobile", "organisation"].forEach((n) => form.elements[n] && form.elements[n].addEventListener("change", () => {
clearTimeout(dupTimer);
dupTimer = setTimeout(dupCheck, 900);
}));
const showDuplicate = (d) => {
const paid = d.status === "paid", to = d.email ? escH(d.email) : "the email address you registered with";
alertBox.innerHTML = (paid
? `<b>You’re already registered for the summit.</b> Each delegate can register once, and your delegate pass was emailed to ${to}.`
: `<b>You’ve already started a registration with these details.</b> It’s waiting for payment, so there’s no need to register again: complete it with the payment link we emailed to ${to}.`)
+ `<span class="dup-acts"><button type="button" class="btn ghost" data-dup-send>${paid ? "Email my pass again" : "Email me the payment link"}</button>`
+ `${paid ? "" : '<a href="pay.html">I have my reference</a>'}</span>`;
alertBox.classList.add("show", "is-info");
alertBox.querySelector("[data-dup-send]").addEventListener("click", async (e) => {
const b = e.currentTarget;
b.disabled = true;
b.textContent = "Sending…";
let r = null;
try { r = await withTimeout(askScript({ formType: "remind" }), 40000); } catch (err) {  }
const ok = r && r.result === "sent";
b.textContent = ok ? `Sent to ${r.email}` : "Couldn’t send it. Please try again";
b.disabled = ok;
});
alertBox.scrollIntoView({ block: "center", behavior: reduceMotion ? "auto" : "smooth" });
};
const bars = (ref) => {
let x = 0, out = "";
for (const ch of ref.replace(/-/g, "")) {
const c = ch.charCodeAt(0);
[1 + (c % 3), 1 + ((c >> 2) % 3), 1 + ((c >> 4) % 2)].forEach((w, k) => { if (k !== 1) out += `<rect x="${x}" y="0" width="${w}" height="46"/>`; x += w + 1.6; });
}
return { svg: out, w: x };
};
const fillPass = (d) => {
const q = (k) => document.querySelector(`[data-pass="${k}"]`);
q("name").textContent = `${d.firstName} ${d.lastName}`.trim();
q("role").textContent = d.designation;
q("org").textContent = d.organisation;
q("ref").textContent = d.ref;
q("ref2").textContent = d.ref;
document.querySelectorAll('[data-pass="email"]').forEach((n) => (n.textContent = d.email));
const b = bars(d.ref), svg = q("bars");
svg.setAttribute("viewBox", `0 0 ${b.w.toFixed(1)} 46`);
svg.querySelector("g").innerHTML = b.svg;
};
const save = (blob, name) => {
const a = document.createElement("a");
a.href = URL.createObjectURL(blob); a.download = name;
document.body.appendChild(a); a.click(); a.remove();
setTimeout(() => URL.revokeObjectURL(a.href), 4000);
};
let passData = null;
document.querySelector("[data-print-pass]")?.addEventListener("click", () => printAlone(document.querySelector(".reg-confirm .my-pass").outerHTML
+ "<p>Delegate pass &middot; CIPS International Procurement &amp; Supply Chain Summit 2027<br>Thursday, 07 January 2027 &middot; ITC Maratha, Mumbai &middot; Please bring a photo ID</p>",
"", passData ? "CIPS-Summit-2027-Delegate-Pass-" + passData.ref : "CIPS-Summit-2027-Delegate-Pass"));
document.querySelector("[data-ics]")?.addEventListener("click", () => {
if (!passData) return;
const stamp = new Date().toISOString().replace(/[-:]/g, "").replace(/\.\d+/, "");
const ics = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//CIPS//Summit 2027//EN", "BEGIN:VEVENT", `UID:${passData.ref}@cips2027.online`, `DTSTAMP:${stamp}`,
"DTSTART;VALUE=DATE:20270107", "DTEND;VALUE=DATE:20270108", "SUMMARY:CIPS International Procurement & Supply Chain Summit 2027",
"LOCATION:ITC Maratha\\, Mumbai\\, India", `DESCRIPTION:Delegate pass ${passData.ref}. Bring your pass and photo ID.`, "URL:https://www.cips2027.online",
"END:VEVENT", "END:VCALENDAR"].join("\r\n");
save(new Blob([ics], { type: "text/calendar" }), "CIPS-Summit-2027.ics");
});
form.addEventListener("submit", async (e) => {
e.preventDefault();
alertBox.classList.remove("show", "is-info");
const results = Object.keys(rules).map(check);
if (results.includes(false)) {
const first = form.querySelector(".field.invalid input, .field.invalid select");
first && first.focus();
return;
}
if (form.elements.website.value) return;
btn.disabled = true;
const label = btn.firstElementChild;
label.textContent = "Checking your details…";
const dup = await dupCheck();
if (dup && dup.result === "duplicate") {
btn.disabled = false;
label.textContent = "Submit Registration";
showDuplicate(dup);
return;
}
const data = Object.fromEntries(new FormData(form).entries());
delete data.website;
data.ref = "CIPS27-DEL-" + refCode();
data.attending = form.elements.attending.checked ? "Yes" : "No";
data.consent = form.elements.consent.checked ? "Yes" : "No";
data.submittedAt = new Date().toISOString();
label.textContent = "Submitting…";
try {
const send = () => (FORM_ENDPOINT ? fetch(FORM_ENDPOINT, { method: "POST", mode: "no-cors", body: new URLSearchParams(data) })
: Promise.resolve(console.warn("[CIPS Summit] FORM_ENDPOINT is not set in js/config.js: this registration was NOT sent anywhere.", data)));
const ready = keepOpen(send());
form.hidden = true;
form.parentElement.querySelectorAll(".form-intro").forEach((n) => (n.hidden = true));
const ok = document.getElementById("register-success"), name = `${data.firstName} ${data.lastName}`.trim();
const stepPay = ok.querySelector('[data-reg-step="pay"]'), stepDone = ok.querySelector('[data-reg-step="done"]');
ok.querySelectorAll("[data-ref]").forEach((n) => (n.textContent = data.ref));
ok.querySelectorAll("[data-sum-name]").forEach((n) => (n.textContent = data.designation ? `${name}, ${data.designation}` : name));
ok.querySelectorAll("[data-sum-org]").forEach((n) => (n.textContent = data.organisation));
passData = data;
fillPass(data);
ok.querySelector("[data-pay-later]").href = "pay.html?ref=" + encodeURIComponent(data.ref);
stepPay.hidden = false;
stepDone.hidden = true;
CIPSPay.mount(ok.querySelector("[data-paybox]"), { ref: data.ref, kind: "delegate", email: data.email, ready, resend: () => keepOpen(send()),
prefill: { name, email: data.email, contact: data.mobile },
onSuccess: (d) => {
fillReceipt(stepDone, { name, org: [data.designation, data.organisation].filter(Boolean).join(", "), email: data.email,
item: "Delegate pass", itemSub: "CIPS International Procurement & Supply Chain Summit 2027, Thursday 07 January 2027, ITC Maratha, Mumbai",
total: d.amount || 11800, pid: d.payment_id, when: paidOn() });
stepDone.querySelectorAll('[data-conf="first"]').forEach((n) => (n.textContent = data.firstName));
const tick = ok.querySelector(".flow-steps .done span").innerHTML;
ok.querySelectorAll('[data-flow="pay"], [data-flow="done"]').forEach((li) => { li.className = "done"; li.querySelector("span").innerHTML = tick; });
stepPay.hidden = true;
stepDone.hidden = false;
stepDone.focus({ preventScroll: true });
ok.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
} });
ok.classList.add("show");
ok.setAttribute("tabindex", "-1");
ok.focus({ preventScroll: true });
ok.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
} catch (err) {
alertBox.textContent = "Sorry, we couldn't submit your registration just now. Please check your connection and try again.";
alertBox.classList.add("show");
btn.disabled = false;
label.textContent = "Submit Registration";
}
});
})();
(() => {
const form = document.getElementById("pay-form");
if (!form) return;
const input = form.elements.ref, field = input.closest(".field"), btn = form.querySelector("button[type=submit]"), label = btn.firstElementChild;
const out = document.querySelector(".pay-out"), po = (k) => out.querySelector(`[data-po="${k}"]`);
const esc = (v) => String(v).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const KIND = { DEL: "delegate", IND: "individual", COM: "company" };
const FEE = CIPSPay.FEE;
const LABEL = { delegate: "Delegate registration", individual: "Individual award nomination", company: "Company award nomination" };
const parse = (v) => {
const m = String(v).toUpperCase().replace(/[^A-Z0-9]/g, "").match(/^CIPS27(DEL|IND0[1-4]|COM0[1-8])([A-Z0-9]{5})$/);
return m ? `CIPS27-${m[1]}-${m[2]}` : null;
};
const setErr = (msg) => { field.classList.toggle("invalid", !!msg); field.querySelector(".err").textContent = msg; input.setAttribute("aria-invalid", msg ? "true" : "false"); };
const lookup = async (ref) => {
if (!FORM_ENDPOINT) return null;
const ctl = new AbortController(), t = setTimeout(() => ctl.abort(), 12000);
try { return await (await fetch(`${FORM_ENDPOINT}?ref=${encodeURIComponent(ref)}`, { signal: ctl.signal })).json(); }
catch (err) { return null; }
finally { clearTimeout(t); }
};
const show = (ref, kind, info) => {
const st = info ? info.status : "unknown", fee = FEE[kind], payable = st === "pending" || st === "unknown";
po("kind").textContent = LABEL[kind] + (info && info.award ? " · " + info.award : "");
po("ref").textContent = ref;
po("paybox").hidden = !payable;
if (payable) CIPSPay.mount(po("paybox").querySelector("[data-paybox]"), { ref, kind, email: info && info.email });
const email = info && info.email ? ` (<b>${esc(info.email)}</b>)` : "";
po("msg").innerHTML = {
pending: `Pay <strong>&#8377;${fee[1]}</strong> (&#8377;${fee[0]} + 18% GST) securely online.${info && info.email ? ` Your confirmation goes to <b>${esc(info.email)}</b>.` : ""}`,
unknown: `We couldn&rsquo;t check this reference just now, but you can still try to pay <strong>&#8377;${fee[1]}</strong> (&#8377;${fee[0]} + 18% GST).`,
paid: `This reference is already paid. ${kind === "delegate" ? "Your delegate pass" : "Your payment confirmation"} was emailed to you${email}. Can&rsquo;t find it? Check your spam folder, or reply to the email you received from us.`,
refunded: "The payment for this reference was refunded, so the booking is no longer active. Reply to any email from us if you need help.",
closed: "This booking is no longer active. Reply to any email from us if you think this is a mistake.",
}[st];
po("note").textContent = !payable ? "" : kind === "delegate" ? "Your delegate pass is emailed to you as soon as the payment is confirmed."
: "We email a payment confirmation as soon as the payment is confirmed.";
form.hidden = true;
out.hidden = false;
out.focus({ preventScroll: true });
out.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "center" });
};
input.addEventListener("input", () => field.classList.contains("invalid") && setErr(""));
form.addEventListener("submit", async (e) => {
e.preventDefault();
const ref = parse(input.value);
if (!ref) { setErr("Please enter a reference like CIPS27-DEL-AB12C."); input.focus(); return; }
input.value = ref;
setErr("");
btn.disabled = true;
label.textContent = "Checking…";
const info = await lookup(ref);
btn.disabled = false;
label.textContent = "Find My Booking";
if (info && info.result === "notfound") {
setErr("We couldn’t find that reference. Please check it against your confirmation email (a booking made a moment ago can take a minute to appear).");
input.focus();
return;
}
const found = info && info.result === "found";
show(ref, (found && info.kind) || KIND[ref.slice(7, 10)], found ? info : null);
});
po("again").addEventListener("click", () => {
out.hidden = true;
form.hidden = false;
input.value = "";
history.replaceState(null, "", location.pathname);
input.focus();
});
const pre = new URLSearchParams(location.search).get("ref");
if (pre) { input.value = pre; form.requestSubmit(); }
})();