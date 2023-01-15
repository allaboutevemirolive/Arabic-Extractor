import cv2
import pytesseract

# Set Tesseract data path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read image
image = cv2.imread("image.jpg")

# Generate OCR text
text = pytesseract.image_to_string(image, lang='ara')

print(text)
