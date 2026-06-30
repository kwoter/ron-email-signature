import pkg from '/Users/louisdean/Projects/chalk-motion-app-main/node_modules/playwright-core/index.js';
const { chromium } = pkg;
import { readFileSync } from 'node:fs';

const OUT = '/Users/louisdean/Projects/ron-email-signature/assets';
const b64 = (p) => readFileSync(p).toString('base64');
const png = (p) => `data:image/png;base64,${b64(p)}`;
const svg = (p) => `data:image/svg+xml;base64,${b64(p)}`;

const ADDON  = png('/Users/louisdean/Downloads/Add-on Exchange Logo.png');
const CLAIMS = png('/Users/louisdean/Downloads/Claims Exchange Logo.png');
const KOMP   = png('/Users/louisdean/Projects/quote.kompare.co.uk-repo/public/lovable-uploads/9c1b0a49-98c3-465f-b47e-e5271a05bca7.png');
const KCALLS = png('/Users/louisdean/Projects/kompare-calls/assets/kompare-calls-logo.png');
const SHIELD = png('/Users/louisdean/Projects/kwoter-website/public/media/kwoter-mark.png');
const GREEN  = svg('/Users/louisdean/Downloads/greener-travel-export/greener-travel/apps/frontend/public/gt-logos/greener-travel-logo.svg');

const kwoterLockup = `<span style="display:inline-flex;align-items:center;gap:9px;">
  <img src="${SHIELD}" style="height:46px;width:auto;display:block">
  <span style="font-family:'Sora',sans-serif;font-weight:700;font-size:34px;color:#1e2c7b;letter-spacing:-0.02em;line-height:1;position:relative;top:1px;">kwoter</span></span>`;

const logoBlock = (headerH, partnerH, accentBar) => `
<div style="text-align:center;">
  <!-- headline brands -->
  <div style="display:inline-flex;align-items:center;justify-content:center;gap:34px;">
    <img src="${ADDON}" style="height:${headerH}px;width:auto;display:block">
    <span style="width:1px;height:${headerH*0.82}px;background:#D7DCEA;display:inline-block"></span>
    <img src="${CLAIMS}" style="height:${headerH}px;width:auto;display:block">
  </div>
  ${accentBar ? `<div style="width:54px;height:3px;border-radius:3px;margin:26px auto 24px;background:linear-gradient(90deg,#16B89A,#1F2C5C);"></div>` : `<div style="height:34px"></div>`}
  <!-- partner brands -->
  <div style="display:inline-flex;align-items:center;justify-content:center;gap:50px;">
    ${kwoterLockup.replace('height:46px','height:'+partnerH+'px').replace('font-size:34px','font-size:'+Math.round(partnerH*0.74)+'px')}
    <img src="${KOMP}"   style="height:${Math.round(partnerH*0.92)}px;width:auto;display:block">
    <img src="${KCALLS}" style="height:${Math.round(partnerH*0.92)}px;width:auto;display:block">
    <img src="${GREEN}"  style="height:${partnerH}px;width:auto;display:block">
  </div>
</div>`;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1584, height: 396 }, deviceScaleFactor: 2 });

// ---------- LinkedIn cover banner 1584x396 ----------
const banner = `<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@700&display=swap" rel="stylesheet">
<style>
 *{margin:0;padding:0;box-sizing:border-box}
 html,body{width:1584px;height:396px;overflow:hidden;}
 .bg{position:relative;width:1584px;height:396px;
   background:
     radial-gradient(120% 140% at 50% -20%, #ffffff 0%, #F4F7FC 55%, #EBF0F8 100%);}
 .bg:before{content:"";position:absolute;inset:0;
   background:
     radial-gradient(40% 60% at 84% 20%, rgba(22,184,154,.07), transparent 70%),
     radial-gradient(40% 60% at 14% 90%, rgba(31,44,92,.06), transparent 70%);}
 .topbar{position:absolute;top:0;left:0;right:0;height:4px;background:linear-gradient(90deg,#16B89A 0%,#1F2C5C 55%,#D9342B 100%);}
 .frame{position:absolute;inset:18px;border:1px solid rgba(31,44,92,.08);border-radius:14px;}
 .wrap{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;}
 .x{position:absolute;font-family:'Sora';font-weight:700;font-size:520px;color:rgba(31,44,92,.025);right:-40px;top:-120px;line-height:1;user-select:none;}
</style></head>
<body><div class="bg"><div class="topbar"></div><div class="frame"></div>
  <div class="x">&times;</div>
  <div class="wrap">${logoBlock(48, 34, true)}</div>
</div></body></html>`;
await page.setContent(banner, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(400);
await page.screenshot({ path: `${OUT}/_banner2x.png`, clip: { x:0, y:0, width:1584, height:396 } });

// ---------- Transparent logo strip (reusable) ----------
const strip = `<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@700&display=swap" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}html,body{background:transparent}#s{display:inline-block;padding:30px 40px}</style>
</head><body><div id="s">${logoBlock(54, 38, true)}</div></body></html>`;
await page.setContent(strip, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(400);
await page.locator('#s').screenshot({ path: `${OUT}/_strip2x.png`, omitBackground: true });

await browser.close();
console.log('rendered banner + strip');
