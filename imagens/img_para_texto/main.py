import pytesseract
import cv2

# image reading
image = cv2.imread('deus_e_fiel.jpg')
pathProgram = r"C:\Users\User\AppData\Local\Programs\Tesseract-OCR"

# extracting text from image
pytesseract.pytesseract.tesseract_cmd = pathProgram + r"\tesseract.exe"
text = pytesseract.image_to_string(image, lang='por')

print(text)
