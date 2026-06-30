import pkg from '/Users/louisdean/Projects/chalk-motion-app-main/node_modules/playwright-core/index.js';
const { chromium } = pkg;
import { readFileSync } from 'node:fs';

const OUT = '/Users/louisdean/Projects/ron-email-signature/assets';
const shieldB64 = readFileSync('/Users/louisdean/Projects/kwoter-website/public/media/kwoter-mark.png').toString('base64');
const greenerB64 = readFileSync('/Users/louisdean/Downloads/greener-travel-export/greener-travel/apps/frontend/public/gt-logos/greener-travel-logo.svg').toString('base64');
const SHIELD = `data:image/png;base64,${shieldB64}`;
const GREENER = `data:image/svg+xml;base64,${greenerB64}`;

const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 3 });

// --- kwoter lockup ---
const kwoterHTML = `<!doctype html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&display=swap" rel="stylesheet">
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  html,body{background:transparent}
  #lockup{display:inline-flex;align-items:center;gap:14px;padding:6px}
  #lockup img{height:104px;width:auto;display:block}
  #lockup span{font-family:'Sora',sans-serif;font-weight:700;font-size:78px;
    color:#1e2c7b;letter-spacing:-0.02em;line-height:1;position:relative;top:2px}
</style></head>
<body><div id="lockup"><img src="${SHIELD}"><span>kwoter</span></div></body></html>`;
await page.setContent(kwoterHTML, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(300);
await page.locator('#lockup').screenshot({ path: `${OUT}/_raw-kwoter.png`, omitBackground: true });

// --- greener travel (transparent re-render of the SVG) ---
const greenerHTML = `<!doctype html><html><head><meta charset="utf-8">
<style>*{margin:0;padding:0}html,body{background:transparent}#g{display:inline-block;padding:6px}#g img{height:120px;width:auto;display:block}</style>
</head><body><div id="g"><img src="${GREENER}"></div></body></html>`;
await page.setContent(greenerHTML, { waitUntil: 'networkidle' });
await page.waitForTimeout(200);
await page.locator('#g').screenshot({ path: `${OUT}/_raw-greener.png`, omitBackground: true });

await browser.close();
console.log('rendered');
