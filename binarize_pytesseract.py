import pytesseract as ocr
import numpy as np
import cv2

from PIL import Image

# converting file read to RGB channels
image = Image.open('teste.jpg').convert('RGB')

#converting into an editable numpy array[x, y, CHANNELS]
npimage = np.asarray(image).astype(np.uint8)

# noise reducement before binarizing
npimage[:, :, 0] = 0
npimage[:, :, 2] = 0

# atribution in grey scale
im = cv2.cvtColor(npimage, cv2.COLOR_RGB2GRAY)

# binary truncate application for the intesity
# pixels with color intensity lower than 127 will be converted to 0 (black)
# pixels with color intensity above 127 will be converted to 255 (white)
# the THRESH_OTSU atribution increments a smart analysis on truncate levels
ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# reconverting the threshhold return into a PIL.Image object
binimage = Image.fromarray(thresh)

# tesseract OCR calling by its own wrapper
phrase = ocr.image_to_string(binimage)

print(phrase)
