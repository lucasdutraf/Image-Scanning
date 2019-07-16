from PIL import Image
import pytesseract as ocr

phrase = ocr.image_to_string(Image.open('easy.jpeg'))
print(phrase)
