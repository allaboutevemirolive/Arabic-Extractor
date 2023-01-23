# Arabic OCR and TTS: 
> Extract Text from Images and Convert it to Speech

This project aims to extract Arabic text from images and convert it to speech. This can be useful in a variety of applications, such as accessibility for visually impaired individuals or language learning. The end result is that it will output an audio file with the text spoken in Arabic.

# Installation

To install the required libraries, you can use the following commands:
```
pip install pydotplus
```
```
pip install pytesseract
```
```
pip install gTTS
```

# Usage

Here are the steps to use pytesseract:

1. Download the trained language data file (tessdata) that you want. For example, "ara.traineddata" stands for Arabic, from the following link:
```
https://github.com/tesseract-ocr/tessdata
```
2. Download the latest Windows installer from this link:
```
https://github.com/UB-Mannheim/tesseract/wiki
```
3. Once the installer is downloaded, install it on your computer.

4. Locate the installation path of Tesseract-OCR, it should be something like:
```
C:\Program Files\Tesseract-OCR
```
5. Place the downloaded "tessdata" into the installation path, under the "tessdata" folder.
```
C:\Program Files\Tesseract-OCR\tessdata
```

Once you have completed these steps, pytesseract should be set up and ready to use.

Note: The installation path may be different in your computer based on your installation settings. But the above path is the default path of installation.




***

# Convert Image to Text

```
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
```

***

# Convert Image to Speech
```
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
```

