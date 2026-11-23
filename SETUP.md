# Connect registrations and award nominations to a Google Sheet

**Live setup (Nov 2026):** spreadsheet "CIPS Summit 2027 – Registrations" and Apps Script project "cips2027-DB", both in the `cipsat2027@gmail.com` Drive. The Web app URL is already in `js/config.js`. The steps below are only needed to rebuild it from scratch. To change the script, follow **Notes** below.

## 1. Create the sheet and script
1. Go to [sheets.google.com](https://sheets.google.com) and create a new blank spreadsheet. Name it something like **"CIPS Summit 2027 – Registrations"**.
2. In the sheet: **Extensions → Apps Script**. This opens a code editor in a new tab.
3. Delete the placeholder `function myFunction() {}` code, then paste in the entire contents of `Code.gs` (in this folder). Save (⌘S / Ctrl+S) and name the project "CIPS Summit registration handler" if asked.
4. At the top of the Apps Script editor, pick **setup** from the function dropdown (next to Run/Debug) and click **Run**. The first time, Google will ask you to authorize the script: click through **Advanced → Go to (project name)** and allow it (this is your own script, running only in your own sheet). If you created the script from [script.google.com](https://script.google.com) instead of from the sheet's menu, set `SHEET_ID` at the top of `Code.gs` to the sheet's ID first; `Code.gs` in this folder is set to the live sheet, so change it if you make a new one.
5. Switch back to the spreadsheet tab. You should now see a **Registrations** tab and a **Nominations** tab, each with formatted headers, a **Status** dropdown and a **Payment Status** dropdown (Pending / Paid / Refunded / Waived). In Google Drive (My Drive) there is now a folder called **"CIPS India Awards 2027 - Nomination files"**; every nomination's attachments go into their own subfolder there, linked from the **Files Folder** column.
   - The script asks for Google Drive permission because it saves nomination attachments. The files stay private to your Google account unless you share the folder.
   - If you had already set up an older version of this sheet, delete its **Registrations** tab before running `setup` again: the columns have changed (Reference and Payment Status were added).

## 2. Deploy it as a Web app
1. Back in the Apps Script editor: **Deploy → New deployment**.
2. Click the gear icon next to "Select type" and choose **Web app**.
3. Set:
   - **Execute as:** Me
   - **Who has access:** Anyone
4. Click **Deploy**, and approve the permissions prompt again if asked.
5. Copy the **Web app URL** (it ends in `/exec`). Opening it in a browser should show `{"result":"ok","message":"CIPS Summit registration endpoint is live"}`.

## 3. Connect the website
1. Open `website/js/config.js` (the copy on your web server).
2. Paste the URL from step 2 between the quotes:
   ```js
   window.CIPS_FORM_ENDPOINT = "https://script.google.com/macros/s/XXXXXXXX/exec";
   ```
3. Upload just that one file to the server (it isn't fingerprinted, so nothing else needs to change).
4. Submit a real test registration on `https://www.cips2027.online/register` and confirm a new row appears in the **Registrations** tab within a few seconds.

You can also test without the website: in the Apps Script editor, pick **testSubmission** (registration) or **testNomination** (award nomination) from the function dropdown and click **Run**. Each posts one fake row so you can see the format before going live.

The same Web app URL handles both forms: `register.html` and `nominate.html` both use `CIPS_FORM_ENDPOINT`.

## 4. How to access and manage the data
- **Open it any time** at [sheets.google.com](https://sheets.google.com). It's a normal Google Sheet, so anything you can do in Sheets (filter, sort, search, export) works on it.
- **Give your team access:** click **Share** (top right of the sheet) and add colleagues by email. Use **Viewer** for people who just need to see registrations, **Editor** for anyone updating the Status column. You don't need to touch the Apps Script for this. Sharing the spreadsheet is separate from the Web app deployment.
- **Track progress:** use the **Status** column (New / Awaiting Payment / Paid / Confirmed / Waitlist / Declined / Cancelled) to mark each registration as your team reviews it. This is the "Our team will review your details" step from the confirmation message.
- **Filter and search:** the header row has a filter already turned on (the funnel icons): use it to view, e.g., only delegates from a country, or only "New" status.
- **Get emailed for every new registration:** in `Code.gs`, set `NOTIFY_EMAIL = "you@yourdomain.com"` near the top, save, then **Deploy → Manage deployments → Edit (pencil) → New version → Deploy** (the URL stays the same, so nothing on the website needs to change).
- **Export a copy:** **File → Download → Comma-separated values (.csv)** or **Microsoft Excel (.xlsx)**, e.g. to share a delegate list or run it through another tool.
- **Search a specific person:** Ctrl+F / ⌘F inside the sheet, or use the filter on the Email column.

## Notes

- **Security checks in the script:** the award type, name and fee are always taken from the `AWARDS` list in Code.gs, never from the browser, and a nomination's reference must match its award (`CIPS27-IND01-…`, `CIPS27-COM03-…`), so nobody can pay a lower fee by editing the form. References must be in the form `CIPS27-XXX-12345` and unique. If you add or rename an award on the website, update `AWARDS` too.
- If you edit `Code.gs` later, always use **Deploy → Manage deployments → Edit (pencil icon) → New version → Deploy**. The Web app URL stays the same, so `config.js` on the website never needs to change.
- The website cannot read the Apps Script reply (browser cross-origin rules), so it shows the "Thank You" message as soon as the request is sent, regardless of whether the row was actually saved. Check the sheet after launch, and again after any change to the script.
- The script rejects a submission missing a required field or with an invalid email, and silently drops anything caught by the hidden honeypot field (a sign of an automated bot, not a real visitor).
- **One registration per delegate:** a registration is refused when the same full name is already in the Registrations tab with the same email, mobile (last 10 digits) or organisation. Cancelled and declined rows don't count, and different names sharing an office email or company are fine. The form checks this before submitting and shows the visitor a message instead: if that registration is unpaid it offers to email the payment link again, and if it is paid, the delegate pass. Both go only to the email already on the registration, at most once an hour and 3 times in 6 hours. To let someone register again, set the old row's **Status** to Cancelled.
- **One entry per nominee:** an Individual Award nomination is refused when the same nominee (same name, with the same nominee email or organisation) is already in the Nominations tab for **any** individual category, as each nominee may enter only one. A Company Award nomination is refused when the same organisation is already entered for the **same** award (it can still enter other company categories). Withdrawn entries don't count, and being a registered delegate makes no difference either way. The form checks this on the nominee page, before any files are uploaded. If the same nominator asks, it offers to resend the payment link (unpaid) or the confirmation (paid) to the nominator's email on file. Anyone else is only told the nominee is already entered. To allow a new entry, set the old row's **Status** to Withdrawn.
- Cell values from the form are stored as plain text (so `+91...` numbers and leading zeros stay intact), and any value starting with `=`, `+`, `-` or `@` is prefixed with `'` so it can never run as a spreadsheet formula.
- Nomination uploads: photos and scanned images of any size are resized in the visitor's browser before upload (long side 2000 px, JPEG), so they arrive at well under 1 MB each. PDFs are uploaded as they are, up to 30 MB in total per nomination (Google accepts about 45 MB per submission). The script stores only PDF, JPEG and PNG files, checked by their content (not just the name); anything else is skipped. Limits: 40 MB of attachments per nomination and 750 MB a day in all (`MAX_UPLOAD_BYTES`, `DAILY_UPLOAD_BYTES`), so the form can't be used to fill this Drive. A Drive folder is made only when a file is kept, and is moved to the bin if the nomination isn't saved.
- The Sheet holds personal data (names, emails, phone numbers, organisations). Keep sharing limited to people who need it, per the site's Privacy Policy.

## 5. Payments (Razorpay Checkout) and how to reconcile them
Both forms end with a **reference number** (for example `CIPS27-DEL-4K2QX` for a delegate, `CIPS27-IND01-7HD2M` for an Individual Award nomination), saved in the **Reference** column.

The payment is taken inside the form, with Razorpay Checkout (no Payment Buttons are needed):
1. After the form, the visitor sees a payment page with the order (fee, 18% GST, total) and a **Pay securely** button.
2. The button asks this script for a Razorpay order (`doGet?action=order&ref=…`). The amount always comes from `FEES_PAID` in `Code.gs`, never from the browser.
3. After payment, the website sends Razorpay's signature to `doGet?action=verify`. The script checks it and marks the row **Paid**, and the website shows the confirmation page. The website then calls `doGet?action=send`, which makes and emails the pass or the nomination confirmation (kept out of the verify step so the visitor's wait stays short; it only ever emails a Paid row that hasn't had its email yet).
4. If the visitor closes the page before that, the 5-minute check (section 6) records the payment anyway.

Fees (GST-inclusive): delegate &#8377;11,800 (&#8377;10,000 + GST), Individual Awards &#8377;29,500 (&#8377;25,000 + GST), Company Awards &#8377;59,000 (&#8377;50,000 + GST).

For anything the script can't match, find the payment in Razorpay → **Transactions → Payments** and set **Payment Status** to **Paid** on the right row by hand. The email then goes out on the next check.

**Receipts:** the confirmation page has **Save or print receipt** (one A4 page), and the pass email or nomination email has the same receipt attached as a PDF: billed-to details, fee, 18% GST, total in figures and words, and the Razorpay payment ID. It is a payment receipt, not a GST tax invoice (that needs the organiser's legal name, address and GSTIN, plus consecutive invoice numbers).

## 6. Automatic payment check, delegate pass and confirmation emails
Flow: the visitor submits the form → pays on the payment page → the script confirms it with Razorpay, marks the row **Paid** and emails the **delegate pass** (pass PDF, receipt PDF and calendar file) or the **nomination confirmation** (receipt PDF), from this Google account. The 5-minute check is the safety net for payments the website couldn't confirm.

**One-time setup**
1. Razorpay Dashboard → **Account & Settings → API Keys** → generate a **live** key. Keep the Key Secret private (it is shown once).
2. Apps Script editor → **Project Settings** (gear) → **Script properties** → add `RAZORPAY_KEY_ID` and `RAZORPAY_KEY_SECRET` with those values → Save. Only this Google account can see them; they are never in the website or in this folder.
3. Editor → pick **installPaymentCheck** → **Run**. Approve the new permissions (Razorpay connection, sending email, running on a schedule). It runs a first check straight away and then every 5 minutes.
4. Optional: run **previewPass** to save a sample pass PDF and a sample receipt PDF in the Drive folder without emailing anyone.

**How matching works:** only captured payments of exactly ₹11,800 / ₹29,500 / ₹59,000 (set in `FEES_PAID`) are considered; other payments on the same Razorpay account are ignored. Each is matched to a **Pending** row by the reference the payer typed (if the button has a Reference field) or else by email. Every payment considered is logged in the **Payments** tab with its result; "match it by hand" means no Pending row had that reference or email, so find the right row, set **Payment Status** to Paid, and the email follows on the next check.

**On submission:** straight after a registration or nomination is saved, the visitor gets a "received" email with their reference and a **Complete your payment** button (it opens `pay.html?ref=…`). To protect this Gmail account, that email goes at most once per address every 6 hours, and is skipped when fewer than 25 sends are left for the day (passes come first). These "received" emails and the reminders together are also capped at 12 an hour (`MAIL_PER_HOUR`).

**Complete your payment page (`pay.html`):** anyone who closed the page or whose payment failed enters their reference; the page asks this script (`doGet?ref=…`) for the type, payment status and a masked email only (for example `as***@gmail.com`), then shows the right payment button, "already paid", or "not found". It is linked from both thank-you screens, the register and nominate pages, the footer and the "received" email.

**Emails:** sent to every row whose Payment Status is **Paid** (or **Waived**, for complimentary delegate passes) and whose **Email Sent (IST)** cell is empty, then that cell gets the time. If sending fails, the cell says why; clear it to retry. To resend a pass, clear the cell. A free Gmail account can send about 100 emails a day: anything over that goes out the next day. Razorpay also emails its own payment receipt to the payer.

**After changing `Code.gs`:** paste it in, save, then **Deploy → Manage deployments → Edit → New version → Deploy** (the website URL stays the same). The 5-minute check always runs the saved code.
