import cv2
import pytesseract
from gtts import gTTS
import IPython.display as ipd

# Set Tesseract data path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read image
image = cv2.imread("image.jpg")

# Generate OCR text
text = pytesseract.image_to_string(image, lang='ara')

# Convert OCR text to speech
tts = gTTS(text, lang='ar')

# Save audio file
tts.save("output.mp3")

# Play audio file
ipd.Audio("output.mp3")
