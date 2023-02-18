import cv2
import docx
import pytesseract

# Set Tesseract data path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read image
image = cv2.imread("input.jpg")

# Generate OCR text
text = pytesseract.image_to_string(image, lang='ara')

# Create a new Microsoft Word document
document = docx.Document()

# Add the OCR text to the document
document.add_paragraph(text)

# Save the document
document.save("output.docx")
