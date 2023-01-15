import io
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from google.cloud import vision
import docx
import fitz

def extract_text_from_pdf(pdf_file_id, output_type='text'):
    """Extracts text from images in a PDF file stored in Google Drive using OCR.

    Args:
        pdf_file_id (str): The file ID of the PDF file in Google Drive.
        output_type (str, optional): The type of output to create. Can be either 'text' for a plain text file or 'docx' for a Microsoft Word document. Defaults to 'text'.

    Returns:
        None
    """
    # Authenticate with Google Drive
    SCOPES = ['https://www.googleapis.com/auth/drive']
    creds = google.oauth2.credentials.Credentials.from_authorized_user_info(info=None, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)

    # Authenticate with the Google Cloud Vision API
    vision_client = vision.ImageAnnotatorClient(credentials=creds)

    # Download the PDF file from Google Drive
    request = service.files().get_media(fileId=pdf_file_id)
    file = io.BytesIO()
    downloader = MediaIoBaseDownload(file, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()

    # Open the PDF file
    pdf = fitz.open(file)

    # Create the output file or document
    if output_type == 'text':
        output_file = open('output.txt', 'w', encoding='utf-8')
    elif output_type == 'docx':
        output_file = docx.Document()
    else:
        raise ValueError('Invalid output type')

    # Iterate through each page of the PDF
    for page_num in range(pdf.page_count):
        # Get the current page
        page = pdf.load_page(page_num)

        # Extract the images from the page
        images = page.get_image_list()

        # Iterate through each image
        for image in images:
            # Convert the image to a pixmap
            pixmap = fitz.Pixmap(pdf, image)

            # Perform OCR on the pixmap using the Google Cloud Vision API
            image_content = pixmap.get_pixmap_as_jpeg()[2]
            image = vision.types.Image(content=image_content)
            response = vision_client.text_detection(image=image)
            text = response.full_text_
            # Write the OCR text to the output file or document
            if output_type == 'text':
                output_file.write(text)
            elif output_type == 'docx':
                output_file.add_paragraph(text)

    # Close the output file or document
    if output_type == 'text':
        output_file.close()
    elif output_type == 'docx':
        output_file.save('output.docx')

# Example usage
extract_text_from_pdf('PDF_FILE_ID', output_type='docx')
