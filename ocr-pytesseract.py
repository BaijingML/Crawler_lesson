from PIL import Image
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'
#tessdata_dir = '--tessdata-dir "D:\Tesseract-OCR\tessdata"'
img = Image.open("C:/Users/26708/Desktop/showphone.gif")
text = pytesseract.image_to_string(img)
print(text)

