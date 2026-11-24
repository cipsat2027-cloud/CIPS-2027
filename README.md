# CIPS International Procurement & Supply Chain Summit 2027 website

Live site: https://www.comingsoon.com

## What's in this package

| Folder | What it is |
|---|---|
| `website/` | The finished site, ready to upload to any web host. This is what runs at www.comingsoon.online. |
| `source/` | The editable source: page generator, stylesheet, script and images. Use it to make changes and rebuild `website/`. |
| `google-sheet/` | The Google Apps Script (`Code.gs`) that receives registrations, nominations and payments, plus its setup guide (`SETUP.md`). |

## Pages
Home, About CIPS, About the Summit, Speakers, Awards, Nominate, Register, Pay, Privacy Policy, Terms & Conditions, Cancellation & Refund Policy and a 404 page.

## Hosting the site
Upload everything inside `website/` to the web root, including the hidden `.htaccess` file. `index.html` must be at the top level.

- **Apache:** `.htaccess` turns on the HTTPS redirect, compression, caching and security headers, and sets the 404 page.
- **nginx:** use `source/server-config/nginx.conf.example`.
- **Vercel:** deploy the `website/` folder as-is. `vercel.json` sets the clean page addresses (`/register`, `/awards` and so on) and the headers.
- **Other static hosts:** set the 404 page to `/404.html` and force HTTPS.

The site must be served over HTTPS.

## Forms, payments and emails
Registrations and award nominations are saved to a Google Sheet by the Apps Script in `google-sheet/`. Payments are taken with Razorpay Checkout, and passes, confirmations and receipts are emailed by the same script.

- The script's Web app URL is set in `website/js/config.js` (and `source/js/config.js`).
- The Razorpay API keys are stored in the script's **Script properties**, never in the website files.
- `google-sheet/SETUP.md` covers setup, managing the data, payment reconciliation and the automatic payment check.

## Making changes
Requirements: macOS with Python 3 and Pillow (`pip3 install pillow`).

1. Edit the content in `source/_build/build_site.py`. Page text, speakers (`PEOPLE`), awards (`IND_AWARDS`, `COM_AWARDS`), SEO titles and descriptions (`SEO`) and the legal-page details are all defined there.
2. Edit the styling in `source/css/site.css`. Colours, type and spacing are the `:root` variables at the top. Edit behaviour in `source/js/site.js`.
3. Rebuild from inside `source/`:
   ```
   python3 _build/build_site.py
   python3 _build/build_dist.py
   ```
   This writes a fresh, optimised copy of the site to `source/upload-ready/`. Upload that folder's contents.
   For Vercel, run `DIST_NAME=upload-vercel python3 _build/build_dist.py` instead. This builds `source/upload-vercel/`, with page links in the `/register` form.
4. If the date or venue on the share image changes, run `python3 _build/make_og.py` before step 3.

If you add or rename an award, update the `AWARDS` list in `google-sheet/Code.gs` to match.

Images: speaker portraits are 800×1000 JPEGs in `source/assets/img/`. `cips-logo-dark.png` is for light backgrounds and `cips-logo-light.png` is for dark ones.

## Placeholders
These details on the legal pages still need confirming. Each is marked `DEMO` in `source/_build/build_site.py`:

- The refund schedule on the Cancellation & Refund Policy page.
- The data retention period on the Privacy Policy ("12 months after the Summit").
- The governing law and courts in the Terms & Conditions (India / New Delhi).
