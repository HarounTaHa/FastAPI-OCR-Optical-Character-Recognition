from fastapi import FastAPI, File, UploadFile
import shutil
import pytesseract

# pytesseract depends tesseract on If used Windows OS \
# you should to install tesseract from https://github.com/UB-Mannheim/tesseract/wiki
# and after installed put the path and set the tesseract path in the script
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = FastAPI()


@app.post('/ocr')
def ocr(image: UploadFile = File(...)):
    """
    Take Image and make process to extract text from
    :param image: File
    :return: result of a Tesseract OCR run on the provided image to string
    """
    file_path = 'txt_file'
    with open(file_path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return pytesseract.image_to_string(file_path, lang='eng')
