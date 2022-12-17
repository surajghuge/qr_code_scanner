import fitz
import base64
from PIL import Image
from pyzbar.pyzbar import decode
from flask import Flask,request
from flask_cors import CORS
import cv2
import os
import pandas as pd 


app = Flask(__name__)
CORS(app)

#  ------- api point to scan only images ------------

@app.route('/upload/img', methods = ['POST'])
def upload():
    file = request.files['file_upload']
    print(file)
    filename = file.filename

    img = cv2.imread(filename)

    decoded_list = decode(img)
    print(decoded_list)
    image_64_decoded = [] #------- list to store decoded text

    #  ----- looping through to image page to scan qr images
    for i in range(len(decoded_list)):
        print(f"Encoded data in QR{i} = {decoded_list[i][0].decode()}")
        print(f"Encoded Data in QR{i} = {base64.b64decode(decoded_list[i][0]).decode('utf-8')}")
        image_64_decoded.append(base64.b64decode(decoded_list[i][0]).decode('utf-8'))
        print('\n')
    
    print(image_64_decoded)

    # --------------- forming dataframe ----------------
    data = pd.DataFrame(image_64_decoded)
    
    # --------------- storing into the excel file ------------------
    excel_output_filename = "output.xlsx"
    if os.path.exists(excel_output_filename):
        with pd.ExcelWriter(excel_output_filename, mode='a',engine="openpyxl",if_sheet_exists="overlay") as writer:data.to_excel(writer, sheet_name="Sheet1",header=None, startrow=writer.sheets["Sheet1"].max_row,index=False)
    else:
        with pd.ExcelWriter(excel_output_filename,mode='w',engine="openpyxl") as writer:data.to_excel(writer, sheet_name="Sheet1",header=None,index=False)

    return image_64_decoded #---returning list to UI for display


# ----- api to scan pdf .... convert to image and scan ----------

@app.route('/upload/pdf', methods = ['POST'])
def uploadPdf():
    file = request.files.get('file_upload')
    print(file)
    filename = file.filename
    doc = fitz.open(filename)
    list_of_images = []
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap()  # render page to an image
        pix.save(f"img-{page.number}.png")
        list_of_images = f"img-{page.number}.png"
    
    print(list_of_images)
    img = cv2.imread(list_of_images)

    decoded_list = decode(img)
    print(decoded_list)

    image_64_decoded = [] #------- list to store decoded text

    #  ----- looping through image to scan qr images
    for i in range(len(decoded_list)):
        print(f"Encoded data in QR{i} = {decoded_list[i][0].decode()}")
        print(f"Encoded Data in QR{i} = {base64.b64decode(decoded_list[i][0]).decode('utf-8')}")
        image_64_decoded.append(base64.b64decode(decoded_list[i][0]).decode('utf-8')) #---appending the data in the list
        print('\n')
    
    print(image_64_decoded)

    # --------------- forming dataframe ----------------
    data = pd.DataFrame(image_64_decoded)
    
    # --------------- storing into the excel file ------------------
    excel_output_filename = "output.xlsx"
    if os.path.exists(excel_output_filename):
        with pd.ExcelWriter(excel_output_filename, mode='a',engine="openpyxl",if_sheet_exists="overlay") as writer:data.to_excel(writer, sheet_name="Sheet1",header=None, startrow=writer.sheets["Sheet1"].max_row,index=False)
    else:
        with pd.ExcelWriter(excel_output_filename,mode='w',engine="openpyxl") as writer:data.to_excel(writer, sheet_name="Sheet1",header=None,index=False)

    return image_64_decoded #---returning list to UI for display

    

@app.route('/')
def hello():
    return "Hello Im connected"
if __name__ == '__main__':
    app.run(debug=True)