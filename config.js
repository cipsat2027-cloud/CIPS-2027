/* Registration form endpoint.
   Paste the Web app URL of your deployed Google Apps Script between the quotes
   (see google-sheet/SETUP.md), then upload this file. Leave "" to run in demo mode:
   the form validates and shows the thank-you message but sends nothing. */
window.CIPS_FORM_ENDPOINT = "https://script.google.com/macros/s/AKfycbwXr_8tkJJqGLs-v8VNOPUFV7n03avB1IDtQpxW9ZcrB9GhOxmb5pdrbTpkK3oblStptQ/exec";

/* Payments: the Pay button opens Razorpay Checkout through the Google Sheet script above. The Razorpay key lives in
   that script's Script properties (RAZORPAY_KEY_ID / RAZORPAY_KEY_SECRET), never in this file: see google-sheet/SETUP.md. */
