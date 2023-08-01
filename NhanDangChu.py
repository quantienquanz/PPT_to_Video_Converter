import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("D:\Python\\goi lang+data+1.3jpg\\xam-7-1770.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(img, lang="vie")
print(text)
with open("dich.txt", "a", encoding="utf-8") as f:
    f.writelines(text)