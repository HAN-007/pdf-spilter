
from pdf2image import convert_from_path
from PIL import Image 
import PIL 
import cv2
from fpdf import FPDF
import img2pdf
pdf = FPDF()
counter = 0
pages = convert_from_path("testt.pdf",500,poppler_path="C:\\poppler-22.01.0\\Library\\bin")
for i, image in enumerate(pages):
    fname = 'image'+str(i)+'.png'
    image.save(fname, "PNG")
    counter += 1
for i in range(1,counter):
    fname = 'image'+str(i)
    img = cv2.imread(fname+".png")
    dim = (700, 1000)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    y = 0
    x = 0
    h = 250
    w = 700

    for j in range(1,5):
        crop_img = img[h*(j-1):(h)*j, x:x+w]
        cv2.imshow("crop_img",crop_img)
        cv2.waitKey(0)
        cv2.imwrite("temp.png",crop_img)
        image = Image.open("temp.png")
        pdf_bytes = img2pdf.convert(image.filename)
        file = open("result/result"+str(i)+str(j)+".pdf", "wb")
        file.write(pdf_bytes)



    cv2.imshow("test",img)
    cv2.waitKey(0)


