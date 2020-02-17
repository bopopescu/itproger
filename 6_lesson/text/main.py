from PIL import Image

from pytesseract import image_to_string as conv

text = conv(Image.open("images/rus.jpg"), lang="rus")  # , lang = "rus"
print(text)

# поместит файл rus.traineddata в testdata
# sudo apt install tesseract-ocr-ukr