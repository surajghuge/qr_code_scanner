
import fitz
import base64
from PIL import Image
import cv2
from pyzbar.pyzbar import decode

 
# ---------- pdf to image generation code-----------
path = "D:/Job_Assignments/EY assignment/test.pdf"
doc = fitz.open(path)


for page in doc:  # iterate through the pages
    pix = page.get_pixmap()  # render page to an image
    pix.save("page-%i.png" % page.number)
print(f"number of pages in pdf : {doc.page_count}")


img = cv2.imread('page-0.png')
decoded_list = decode(img)
print(decoded_list)

for i in range(len(decoded_list)):
    print(f"Data in QR{i} = {decoded_list[i][0].decode()}")

import pandas as pd 


# forming dataframe
data = pd.DataFrame(decode(img)) 
  
# storing into the excel file
data.to_excel("output.xlsx")






# # --------- decoding QR data from image ---------
# import zxing
# reader = zxing.BarCodeReader()
# barcode = reader.decode("page-1.png")
# print(barcode) #----all data from qr code--------


# image_64_decoded = base64.b64decode(barcode.raw) #----decoding raw data encoded in base64 ---------
# print(image_64_decoded) 


# image_64_decode = base64.b64decode(image_read)
# print(image_64_decode)






# for code in decode(img):
#     print(code.type)
# print(decoded_list[0].data.decode('utf-8'))
# print(decoded_list[1].data.decode('utf-8'))


# base64_img = cv2.imread('D:\Job_Assignments\EY assignment\base64_qr.png')
# print(base64_img)


# for i in range(len(decode(img2))):
#     print(decode(img2)[i][0].decode('utf-8'))





# img2 = cv2.imread('D:\Job_Assignments\EY assignment\page-1.png')

# # # --------------to print data in qr code------------
# for code in decode(img2):
#     print(code.type)
#     print(code.data.decode('utf-8'))



# # ---------- pdf to image generation code-----------
# path = "D:/Job_Assignments/EY assignment/test.pdf"
# doc = fitz.open(path)


# for page in doc:  # iterate through the pages
#     pix = page.get_pixmap()  # render page to an image
#     pix.save(f"page-{page.number}.png")
# print(f"number of pages in pdf : {doc.page_count}")


# # # --------- decoding QR data from image ---------
# import zxing
# reader = zxing.BarCodeReader()
# barcode = reader.decode("frooty.png")
# print(f"raw base64 code = {barcode.raw}") #----all data from qr code--------

# image_64_decoded = base64.b64decode(barcode.raw) #----decoding raw data encoded in base64 ---------
# print(f"decoded text = {image_64_decoded.decode()}")


# import pandas as pd 

# image_decoded_data = [image_64_decoded.decode()]

# # forming dataframe
# data = pd.DataFrame(image_decoded_data,columns=['Decoded text'])
  
# # storing into the excel file
# data.to_excel("output2.xlsx")