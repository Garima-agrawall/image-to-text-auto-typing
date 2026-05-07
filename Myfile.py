import pytesseract
from PIL import Image
import pyautogui
import time
import cv2
import os

# ==== Tesseract Path ====
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ==== IMAGE PATH (Full Path Use Karna Better Hai) ====
image_path = r"C:\Users\DELL\Desktop\auto_type\sample_image.jpeg"

# ==== Check Image Exists ====
if not os.path.exists(image_path):
    print("Image not found. Check file name or path.")
    exit()

# ==== IMAGE PREPROCESSING ====
image = cv2.imread(image_path)

if image is None:
    print("Image could not be loaded.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cv2.imwrite("processed.png", thresh)

# ==== OCR PROCESS ====
text = pytesseract.image_to_string("processed.png", lang='eng')

print("===== Extracted Text =====")
print(text)

# ==== WAIT BEFORE TYPING ====
print("Typing will start in 5 seconds...")
time.sleep(5)

# ==== AUTO TYPE ====
pyautogui.write(text, interval=0.02)

print("Done.")