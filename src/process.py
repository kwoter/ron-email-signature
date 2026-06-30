from PIL import Image
import json, os

OUT = "/Users/louisdean/Projects/ron-email-signature/assets"

SRC = {
 "addon-exchange":  "/Users/louisdean/Downloads/Add-on Exchange Logo.png",
 "claims-exchange": "/Users/louisdean/Downloads/Claims Exchange Logo.png",
 "kwoter":          f"{OUT}/_raw-kwoter.png",
 "kompare":         "/Users/louisdean/Projects/quote.kompare.co.uk-repo/public/lovable-uploads/9c1b0a49-98c3-465f-b47e-e5271a05bca7.png",
 "kompare-calls":   "/Users/louisdean/Projects/kompare-calls/assets/kompare-calls-logo.png",
 "greener-travel":  f"{OUT}/_raw-greener.png",
}

# display heights in CSS px; retina factor 2
HEADER_H  = 27
PARTNER_H = 22
HEIGHTS = {
 "addon-exchange": HEADER_H, "claims-exchange": HEADER_H,
 "kwoter": PARTNER_H, "kompare": PARTNER_H, "kompare-calls": PARTNER_H, "greener-travel": PARTNER_H,
}
RETINA = 2

def trim(im):
    im = im.convert("RGBA")
    # build alpha-based bbox; if image has no real transparency, trim near-white
    alpha = im.split()[3]
    bbox = alpha.getbbox()
    if bbox is None:  # fully opaque -> trim white
        bg = Image.new("RGBA", im.size, (255,255,255,255))
        from PIL import ImageChops
        diff = ImageChops.difference(im, bg)
        bbox = diff.convert("L").point(lambda p: 255 if p>8 else 0).getbbox()
    return im.crop(bbox) if bbox else im

dims = {}
for name, path in SRC.items():
    im = trim(Image.open(path))
    w, h = im.size
    disp_h = HEIGHTS[name]
    disp_w = round(disp_h * w / h)
    asset_w, asset_h = disp_w*RETINA, disp_h*RETINA
    im = im.resize((asset_w, asset_h), Image.LANCZOS)
    im.save(f"{OUT}/{name}.png", optimize=True)
    dims[name] = {"w": disp_w, "h": disp_h}
    kb = os.path.getsize(f"{OUT}/{name}.png")/1024
    print(f"{name:16s} disp {disp_w}x{disp_h}  asset {asset_w}x{asset_h}  {kb:.1f}KB")

json.dump(dims, open(f"{OUT}/dims.json","w"), indent=2)
print("\nsaved dims.json")
