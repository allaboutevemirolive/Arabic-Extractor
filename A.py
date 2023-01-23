import cv2
import docx
import pytesseract
import logging

# Set up logging
logging.basicConfig(filename="ocr_process.log", level=logging.DEBUG)

def image_to_text(input_file, output_file, lang='eng', output_format='docx'):
    try:
        # Set Tesseract data path
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        
        # Read image
        image = cv2.imread(input_file)
        
        # Add pre-processing steps for the input image to improve OCR accuracy
        image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.medianBlur(image, 3)

        # Generate OCR text
        text = pytesseract.image_to_string(image, lang=lang)
        
        # Create a new document
        if output_format == 'docx':
            document = docx.Document()
            document.add_paragraph(text)
            document.save(output_file)
        elif output_format == 'txt':
            with open(output_file, 'w') as f:
                f.write(text)
        else:
            logging.error("Invalid output format")
            return None
        
        return text
    except Exception as e:
        logging.error(e)
        return None

# Example usage
input_file = 'input.jpg'
output_file = 'output.docx'
lang = 'ara'
output_format = 'docx'
ocr_text = image_to_text(input_file, output_file, lang, output_format)

if ocr_text:
    print("OCR text:", ocr_text)
else:
    print("OCR failed")
