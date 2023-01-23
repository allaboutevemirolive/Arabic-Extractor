# Extracting Arabic Text from Images with Python

In this repository, you will find a guide on how to extract Arabic text from an image using Python. You will need to install the necessary libraries using the pip package manager.

## Installation

To install the required libraries, you can use the following commands:
```
!pip install pydotplus
!pip install pytesseract
!pip install gTTS
```

## Convert tmage to text



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



# Set Tesseract data path
```
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
```
To read the image and generate OCR text using Tesseract, you can use the following code:

# Read image
```
image = cv2.imread("image.png")
```
# Generate OCR text
 ```
text = pytesseract.image_to_string(image, lang='ara')
print(text)
```
Note that you will need to replace "image.png" with the path to the image file on your computer.

You can then use the gTTS library to convert the OCR text to speech. Here is an example of how to do this:

# Convert OCR text to speech
```
tts = gTTS(text, lang='ar')
```
# Save audio file
```
tts.save("output.mp3")
```
# Play audio file
```
ipd.Audio("output.mp3")
```
I hope this helps! Let me know if you have any questions.

