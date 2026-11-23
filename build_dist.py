"""Builds the optimised, upload-ready site into upload-ready/ (source files are never modified)."""
import os, re, shutil, hashlib, subprocess, glob, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = ROOT + "/" + os.environ.get("DIST_NAME", "upload-ready")
PROD_URL = "https://www.cips2027.online"
SITE_URL = os.environ.get("SITE_URL", PROD_URL).rstrip("/")
CLEAN_URLS = DIST.endswith("upload-vercel")   # the Vercel build uses extension-less page addresses (vercel.json cleanUrls)
CONFIG_DIR = ROOT + "/server-config"
import tempfile
STAGE = tempfile.mkdtemp(prefix="cips-stage-")
PAGES = ["index", "about-cips", "about-summit", "speakers", "awards", "nominate", "register", "pay", "privacy", "terms", "cancellation", "404"]

def rd(p): return open(p, encoding="utf-8").read()
def wr(p, s, mode="w"):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, mode).write(s)
def sh(*a): subprocess.run(a, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# ------------------------------------------------------------------ minifiers
def min_css(src):
    out, i, n = [], 0, len(src)
    depth = 0
    while i < n:
        ch = src[i]
        if src.startswith("/*", i):
            j = src.find("*/", i + 2); i = n if j < 0 else j + 2; continue
        if ch in "\"'":
            j = i + 1
            while j < n and src[j] != ch:
                j += 2 if src[j] == "\\" else 1
            out.append(src[i:j + 1]); i = j + 1; continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch.isspace():
            j = i
            while j < n and src[j].isspace(): j += 1
            out.append(" "); i = j; continue
        out.append(ch); i += 1
    s = "".join(out)
    # tokens that never need surrounding spaces (outside of strings we split by quotes)
    parts = re.split(r'("(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')', s)
    for k in range(0, len(parts), 2):
        q = parts[k]
        q = re.sub(r"\s*([{};,>])\s*", r"\1", q)
        q = re.sub(r"\s*:\s*", ":", q)
        q = re.sub(r"\(\s+", "(", q); q = re.sub(r"\s+\)", ")", q)
        q = re.sub(r"(?<![\d.])0\.(\d)", r".\1", q)
        q = q.replace(";}", "}")
        parts[k] = q
    s = "".join(parts)
    # space-sensitive: ' :' inside selectors like 'a :hover' is rare here; verified by visual diff
    return s.strip()

def min_js(src):
    out, i, n = [], 0, len(src)
    prev = ""          # last significant char, for regex detection
    while i < n:
        ch = src[i]
        if src.startswith("//", i):
            j = src.find("\n", i); i = n if j < 0 else j; continue
        if src.startswith("/*", i):
            j = src.find("*/", i + 2); i = n if j < 0 else j + 2; continue
        if ch in "\"'`":
            j = i + 1
            while j < n and src[j] != ch:
                j += 2 if src[j] == "\\" else 1
            out.append(src[i:j + 1]); prev = ch; i = j + 1; continue
        if ch == "/" and prev in "(,=:[!&|?{};" + "":
            j = i + 1; incls = False
            while j < n:
                c = src[j]
                if c == "\\": j += 2; continue
                if c == "[": incls = True
                elif c == "]": incls = False
                elif c == "/" and not incls: break
                j += 1
            j += 1
            while j < n and src[j].isalpha(): j += 1
            out.append(src[i:j]); prev = "/"; i = j; continue
        if ch.isspace():
            j = i; nl = False
            while j < n and src[j].isspace():
                nl = nl or src[j] == "\n"; j += 1
            out.append("\n" if nl else " "); i = j; continue
        out.append(ch); prev = ch; i += 1
    s = "".join(out)
    s = re.sub(r"[ \t]*\n[ \t\n]*", "\n", s)
    s = re.sub(r"[ ]*([{}();,=:+\-*/<>!&|?\[\]])[ ]*", r"\1", s) if False else s   # keep ASI-safe: only trim whitespace
    return s.strip()

def min_html(src):
    src = re.sub(r"[ \t]*\n[ \t]*", " ", src)         # newline + indent -> one space (identical rendering)
    src = re.sub(r">\s{2,}<", "> <", src)
    src = re.sub(r"\s{2,}", " ", src)
    return src.strip()

def min_svg(src):
    src = re.sub(r"<\?xml[^>]*\?>", "", src)
    src = re.sub(r"\s*\n\s*", "", src)
    return src.strip()

# ------------------------------------------------------------------ 1. clean + stage images
shutil.rmtree(DIST, ignore_errors=True)
os.makedirs(STAGE + "/img"); os.makedirs(DIST)

img = ROOT + "/assets/img/"
# logos: shown at <=64px tall -> 130px tall (2x) is plenty
for f in ["cips-logo-dark.png", "cips-logo-light.png"]:
    sh("sips", "-Z", "390", img + f, "--out", STAGE + "/img/" + f)   # wide logos: 390px wide = 2.7x the 145px header size
sh("sips", "-Z", "320", img + "powered-by-navi-mumbai.png", "--out", STAGE + "/img/powered-by-navi-mumbai.png")
shutil.copy(img + "cips-emblem.png", STAGE + "/img/cips-emblem.png")
sh("sips", "-Z", "96", img + "favicon.png", "--out", STAGE + "/img/favicon.png")
sh("sips", "-Z", "180", img + "apple-touch-icon.png", "--out", STAGE + "/img/apple-touch-icon.png")
# speaker photos: 800x1000 masters shown up to ~370x460 css px -> keep full size for 2x screens, quality 86
for f in sorted(f for f in os.listdir(img) if f.endswith(".jpg")):
    sh("sips", "-Z", "1000", "-s", "format", "jpeg", "-s", "formatOptions", "86", img + f, "--out", STAGE + "/img/" + f)
# ...and WebP copies at 480 and 800 px wide (about a quarter of the JPEG's size); the pages offer them through <picture> srcset
from PIL import Image as _Img
for f in sorted(f for f in os.listdir(img) if f.endswith(".jpg")):
    with _Img.open(img + f) as im:
        im = im.convert("RGB")
        for w in (480, 800):
            v = im if im.width <= w else im.resize((w, round(im.height * w / im.width)), _Img.LANCZOS)
            v.save(STAGE + "/img/" + f[:-4] + f"-{w}.webp", "WEBP", quality=80, method=6)
# logos: re-saved as optimised palette PNGs (same look, a fraction of the bytes)
for f in ["cips-logo-dark.png", "cips-logo-light.png", "powered-by-navi-mumbai.png", "cips-emblem.png"]:
    with _Img.open(STAGE + "/img/" + f) as im:
        im.load()
        q = im.convert("RGBA").quantize(colors=128, method=_Img.Quantize.FASTOCTREE, dither=_Img.Dither.NONE)
        q.save(STAGE + "/img/" + f, optimize=True)
# share image -> jpeg
sh("sips", "-s", "format", "jpeg", "-s", "formatOptions", "84", ROOT + "/assets/og-image.png", "--out", STAGE + "/og-image.jpg")
wr(STAGE + "/globe-editorial.svg", min_svg(rd(ROOT + "/assets/globe-editorial.svg")))

# ------------------------------------------------------------------ 2. hashed assets
def h8(b): return hashlib.sha256(b).hexdigest()[:8]
assets = {}   # source-ref -> dist-ref
def emit(ref, data, keep_name=False, binary=False):
    """ref is the public path used in the HTML source, e.g. assets/img/x.jpg"""
    b = data if binary else data.encode("utf-8")
    base, ext = os.path.splitext(ref)
    out = ref if keep_name else f"{base}.{h8(b)}{ext}"
    wr(DIST + "/" + out, b if binary else data, "wb" if binary else "w")
    assets[ref] = out
    return out

for f in sorted(os.listdir(STAGE + "/img")):
    b = open(STAGE + "/img/" + f, "rb").read()
    emit("assets/img/" + f, b, keep_name=(f in ("favicon.png", "apple-touch-icon.png")), binary=True)
emit("assets/og-image.jpg", open(STAGE + "/og-image.jpg", "rb").read(), keep_name=True, binary=True)
emit("assets/email/cips-logo-light.png", open(STAGE + "/img/cips-logo-light.png", "rb").read(), keep_name=True, binary=True)   # fixed name: the pass emails load it
emit("assets/email/cips-logo-dark.png", open(STAGE + "/img/cips-logo-dark.png", "rb").read(), keep_name=True, binary=True)    # fixed name: the receipt PDF loads it
emit("assets/globe-editorial.svg", rd(STAGE + "/globe-editorial.svg"))

css = min_css(rd(ROOT + "/css/site.css"))
js = min_js(rd(ROOT + "/js/site.js"))
# rewrite asset refs inside css/js (none expected, but keep generic)
for src_ref, dst_ref in assets.items():
    css = css.replace(src_ref, dst_ref); js = js.replace(src_ref, dst_ref)
emit("css/site.css", css)
emit("js/site.js", js)
emit("js/config.js", rd(ROOT + "/js/config.js"), keep_name=True)   # left readable: this is the file you edit

# ------------------------------------------------------------------ 3. html
def rewrite(html, root_abs=False):
    html = html.replace("assets/og-image.png", "assets/og-image.jpg")
    html = re.sub(r"(assets/globe-editorial\.svg)\?v=\d+", r"\1", html)
    for src_ref, dst_ref in sorted(assets.items(), key=lambda kv: -len(kv[0])):
        html = html.replace(src_ref, dst_ref)
    return html

for p in PAGES:
    html = rewrite(rd(f"{ROOT}/{p}.html"))
    html = min_html(html)
    if p == "404":   # served from any path -> root-absolute references
        html = re.sub(r'(href|src)="((?!https?:|data:|mailto:|#|/)[^"]+)"', r'\1="/\2"', html)
    if CLEAN_URLS:   # Vercel serves /register for register.html (and redirects .html): link straight to the final address
        names = "|".join(n for n in PAGES if n != "404")
        html = re.sub(r'href="/?index\.html(?=[#?"])', 'href="/', html)
        html = re.sub(re.escape(SITE_URL) + r'/(' + names + r')\.html', SITE_URL + r'/\1', html)    # absolute: canonical, og:url, structured data
        html = re.sub(r'href="/?(' + names + r')\.html(?=[#?"])', r'href="/\1', html)              # links between pages
    wr(f"{DIST}/{p}.html", html)

# ------------------------------------------------------------------ 4. static extras
for _f in ("robots.txt", "sitemap.xml"):
    wr(DIST + "/" + _f, rd(ROOT + "/" + _f).replace(PROD_URL, SITE_URL))
if CLEAN_URLS:
    wr(DIST + "/sitemap.xml", re.sub(r"\.html</loc>", "</loc>", rd(DIST + "/sitemap.xml")))
if SITE_URL != PROD_URL:   # preview host: keep it out of search engines
    wr(DIST + "/robots.txt", "User-agent: *\nDisallow: /\n")

HTACCESS = r'''# CIPS Summit 2027 - Apache config (upload with the site). Requires mod_rewrite, mod_headers, mod_expires, mod_deflate.
Options -Indexes
DirectoryIndex index.html
ErrorDocument 404 /404.html

# Force HTTPS
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteCond %{HTTPS} !=on
  RewriteCond %{HTTP:X-Forwarded-Proto} !https
  RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</IfModule>

# Compression
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript text/javascript image/svg+xml application/xml text/xml text/plain
</IfModule>
<IfModule mod_brotli.c>
  AddOutputFilterByType BROTLI_COMPRESS text/html text/css application/javascript text/javascript image/svg+xml application/xml text/xml text/plain
</IfModule>

<IfModule mod_mime.c>
  AddType application/javascript .js
  AddType image/svg+xml .svg
  AddDefaultCharset UTF-8
</IfModule>

# Caching: fingerprinted files (name.<8 hex>.ext) never change -> cache for a year; everything else revalidates
<IfModule mod_headers.c>
  <FilesMatch "\.[0-9a-f]{8}\.(css|js|jpg|jpeg|png|svg)$">
    Header set Cache-Control "public, max-age=31536000, immutable"
  </FilesMatch>
  <FilesMatch "\.(html|xml|txt)$">
    Header set Cache-Control "no-cache"
  </FilesMatch>
  <FilesMatch "^(config\.js)$">
    Header set Cache-Control "no-cache"
  </FilesMatch>
  <FilesMatch "^(favicon\.png|apple-touch-icon\.png|og-image\.jpg)$">
    Header set Cache-Control "public, max-age=86400"
  </FilesMatch>
  # Security headers
  Header always set X-Content-Type-Options "nosniff"
  Header always set X-Frame-Options "SAMEORIGIN"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set Permissions-Policy "camera=(), microphone=(), geolocation=()"
  Header always set Strict-Transport-Security "max-age=31536000"
</IfModule>
'''
# Content-Security-Policy: scripts only from this site (plus the one inline line, by its hash) and Razorpay Checkout; the forms post
# to the Google Sheet script; no other site may frame the pages (clickjacking). The pages use style attributes, hence 'unsafe-inline' for styles.
import base64 as _b64
_inline = sorted({m for n in PAGES for m in re.findall(r"<script>(.*?)</script>", open(f"{DIST}/{n}.html", encoding="utf-8").read(), re.S)})
_hashes = " ".join("'sha256-" + _b64.b64encode(hashlib.sha256(m.encode("utf-8")).digest()).decode() + "'" for m in _inline)
RZP = "https://checkout.razorpay.com https://*.razorpay.com"
CSP = "; ".join([
    "default-src 'self'", f"script-src 'self' {_hashes} {RZP}", "style-src 'self' 'unsafe-inline'",
    f"img-src 'self' data: blob: {RZP}", "font-src 'self' data:",
    f"connect-src 'self' https://script.google.com https://script.googleusercontent.com {RZP}",
    f"frame-src {RZP}", f"form-action 'self' {RZP}", "frame-ancestors 'self'", "base-uri 'self'", "object-src 'none'",
    "upgrade-insecure-requests"])
PERMS = "camera=(), microphone=(), geolocation=(), usb=(), browsing-topics=()"
HTACCESS = HTACCESS.replace('  Header always set Permissions-Policy "camera=(), microphone=(), geolocation=()"',
                            f'  Header always set Permissions-Policy "{PERMS}"\n  Header always set Content-Security-Policy "{CSP}"')
wr(DIST + "/.htaccess", HTACCESS)
# Vercel: extension-less URLs (/awards -> awards.html), the basic security headers, and long caching for fingerprinted files
import json as _json_v
IMMUTABLE = {"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}
wr(DIST + "/vercel.json", _json_v.dumps({
    "cleanUrls": True, "trailingSlash": False,
    "headers": [
        {"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                                   {"key": "X-Frame-Options", "value": "SAMEORIGIN"}, {"key": "Permissions-Policy", "value": PERMS},
                                   {"key": "Content-Security-Policy", "value": CSP}]},
        # fingerprinted files (name.<8 hex>.ext) never change: browsers keep them for a year and don't re-check them on every page
        {"source": "/css/(.*)", "headers": [IMMUTABLE]},
        {"source": "/js/site.(.*)", "headers": [IMMUTABLE]},
        {"source": "/assets/img/((?!favicon|apple-touch-icon).*)", "headers": [IMMUTABLE]},
        {"source": "/assets/globe-editorial.(.*)", "headers": [IMMUTABLE]},
    ]}, indent=2) + "\n")

NGINX = r'''# CIPS Summit 2027 - nginx server block (use instead of .htaccess). Adjust paths/certs.
server {
    listen 443 ssl http2;
    server_name www.cips2027.online;
    root /var/www/cips2027.online;
    index index.html;
    error_page 404 /404.html;

    gzip on;
    gzip_types text/css application/javascript image/svg+xml application/xml text/plain;
    # brotli on; brotli_types text/css application/javascript image/svg+xml application/xml text/plain;   # if ngx_brotli is installed

    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Strict-Transport-Security "max-age=31536000" always;

    location ~* \.[0-9a-f]{8}\.(css|js|jpg|jpeg|png|svg)$ { add_header Cache-Control "public, max-age=31536000, immutable"; }
    location ~* \.(html|xml|txt)$ { add_header Cache-Control "no-cache"; }
    location / { try_files $uri $uri/ =404; }
}
server { listen 80; server_name cips2027.online www.cips2027.online; return 301 https://www.cips2027.online$request_uri; }
'''
NGINX = NGINX.replace('    add_header Strict-Transport-Security', f'    add_header Permissions-Policy "{PERMS}" always;\n    add_header Content-Security-Policy "{CSP}" always;\n    add_header Strict-Transport-Security')
wr(CONFIG_DIR + "/nginx.conf.example", NGINX)

# ------------------------------------------------------------------ 5. report
def size(p): return os.path.getsize(p)
print("--- dist files")
tot = 0
for dp, _, fs in os.walk(DIST):
    for f in sorted(fs):
        fp = os.path.join(dp, f); s = size(fp); tot += s
        print(f"{s:9,}  {os.path.relpath(fp, DIST)}")
print(f"{tot:9,}  TOTAL")
shutil.rmtree(STAGE, ignore_errors=True)
