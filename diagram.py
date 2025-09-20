import cv2

def convert_to_sketch(img_path, out_path="sketch.png"):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21,21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    cv2.imwrite(out_path, sketch)
    return out_path
