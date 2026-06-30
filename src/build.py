import json

BASE_DIR = "/Users/louisdean/Projects/ron-email-signature"
dims = json.load(open(f"{BASE_DIR}/assets/dims.json"))

CDN  = "https://cdn.jsdelivr.net/gh/kwoter/ron-email-signature@main/assets"
LOCAL = f"file://{BASE_DIR}/assets"

# palette
NAVY="#1F2C5C"; NAME="#16213F"; SLATE="#5B6478"; MUTE="#8B93A7"; FAINT="#AEB4C4"
TEAL="#16B89A"; HAIR="#E7EAF1"; LINK="#1F2C5C"
FONT="-apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

def img(base, name, alt, extra=""):
    d = dims[name]
    return (f'<img src="{base}/{name}.png" width="{d["w"]}" height="{d["h"]}" alt="{alt}" '
            f'style="display:block;border:0;outline:none;text-decoration:none;'
            f'-ms-interpolation-mode:bicubic;height:{d["h"]}px;width:{d["w"]}px;{extra}">')

def contact_row(letter, value_html):
    return f'''<tr>
      <td valign="top" style="width:20px;padding:2px 0;font-family:{FONT};font-size:13px;line-height:18px;font-weight:700;color:{TEAL};">{letter}</td>
      <td valign="top" style="padding:2px 0;font-family:{FONT};font-size:13px;line-height:18px;color:#3A4257;letter-spacing:.1px;">{value_html}</td>
    </tr>'''

def build(base):
    addon  = img(base, "addon-exchange", "Add-On Exchange")
    claims = img(base, "claims-exchange", "Claims Exchange")
    kwoter = img(base, "kwoter", "kwoter")
    komp   = img(base, "kompare", "kompare")
    kcalls = img(base, "kompare-calls", "kompare calls")
    green  = img(base, "greener-travel", "greener travel")
    rule_h = dims["addon-exchange"]["h"]

    contacts = (
        contact_row("m", '+44 (0) 7867 928145')
        + contact_row("e", f'<a href="mailto:ron@ronatkinsonconsultancy.co.uk" style="color:{LINK};text-decoration:none;">ron@ronatkinsonconsultancy.co.uk</a>')
        + contact_row("w", f'<a href="https://ronatkinsonconsultancy.co.uk" style="color:{LINK};text-decoration:none;">ronatkinsonconsultancy.co.uk</a>')
    )

    return f'''<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="560" style="border-collapse:collapse;background:#ffffff;width:560px;max-width:560px;">
  <tr><td style="padding:2px 0 0 0;font-family:{FONT};">

    <!-- name -->
    <div style="font-family:{FONT};font-size:20px;line-height:24px;font-weight:700;color:{NAME};letter-spacing:-.2px;">Ron Atkinson</div>
    <div style="font-family:{FONT};font-size:12.5px;line-height:18px;color:{SLATE};padding-top:3px;">
      <span style="color:{NAVY};font-weight:600;">Director</span>
      <span style="color:{FAINT};padding:0 6px;">&bull;</span>
      <span>Ron Atkinson Consultancy Limited</span>
    </div>
    <div style="font-family:{FONT};font-size:12px;line-height:17px;font-style:italic;color:{MUTE};padding-top:5px;">Connecting people from the insurance industry</div>

    <!-- divider -->
    <div style="height:16px;line-height:16px;font-size:0;">&nbsp;</div>
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="border-collapse:collapse;"><tr><td style="height:1px;line-height:1px;font-size:0;background:{HAIR};">&nbsp;</td></tr></table>
    <div style="height:14px;line-height:14px;font-size:0;">&nbsp;</div>

    <!-- contact -->
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">{contacts}</table>

    <!-- divider -->
    <div style="height:16px;line-height:16px;font-size:0;">&nbsp;</div>
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="border-collapse:collapse;"><tr><td style="height:1px;line-height:1px;font-size:0;background:{HAIR};">&nbsp;</td></tr></table>
    <div style="height:18px;line-height:18px;font-size:0;">&nbsp;</div>

    <!-- twin exchange headline brands -->
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
      <tr>
        <td valign="middle" style="padding:0 20px 0 0;">{addon}</td>
        <td valign="middle" style="width:1px;background:{HAIR};font-size:0;line-height:0;height:{rule_h}px;">&nbsp;</td>
        <td valign="middle" style="padding:0 0 0 20px;">{claims}</td>
      </tr>
    </table>

    <!-- partner strip -->
    <div style="height:18px;line-height:18px;font-size:0;">&nbsp;</div>
    <div style="font-family:{FONT};font-size:9px;line-height:11px;letter-spacing:1.6px;text-transform:uppercase;color:{FAINT};font-weight:600;padding-bottom:10px;">In partnership with</div>
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
      <tr>
        <td valign="middle" style="padding:0 22px 0 0;">{kwoter}</td>
        <td valign="middle" style="padding:0 22px 0 0;">{komp}</td>
        <td valign="middle" style="padding:0 22px 0 0;">{kcalls}</td>
        <td valign="middle" style="padding:0;">{green}</td>
      </tr>
    </table>

  </td></tr>
</table>'''

prod = build(CDN)
prev = build(LOCAL)

open(f"{BASE_DIR}/signature.html","w").write(prod)

preview_doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0;background:#fff;padding:40px;}}</style></head><body>{prev}</body></html>'''
open(f"{BASE_DIR}/preview.html","w").write(preview_doc)
print("built signature.html (CDN) + preview.html (local)")
