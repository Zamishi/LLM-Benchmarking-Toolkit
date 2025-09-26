import pytesseract
from PIL import Image
import mss

def capture_screen(region=None):
    with mss.mss() as sct:
        monitor = sct.monitors[1] if len(sct.monitors) > 1 else sct.monitors[0]
        bbox = monitor if region is None else {
            "left": region[0], "top": region[1], "width": region[2], "height": region[3]
        }
        img = sct.grab(bbox)
        return Image.frombytes("RGB", img.size, img.rgb)

def ocr_image(img):
    return pytesseract.image_to_string(img, lang="eng").strip()
