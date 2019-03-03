import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from pdf2image import convert_from_path, convert_from_bytes
import io
from google.cloud import vision
from google.cloud.vision import types
import hashlib
import time

# Path
UPLOAD_FOLDER = './media/in/'
CONVERT_FOLDER = './media/out/'
RESULT_FOLDER = './result/'
ALLOWED_EXTENSIONS = set(['pdf'])

# Server
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERT_FOLDER'] = CONVERT_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

# Gcloud 
client = vision.ImageAnnotatorClient()

#Crypto
hash = hashlib.sha1()

def write_txt(content, file):
  file.write(content)


def get_text(jpgFilename, txtFilename):

  with io.open(CONVERT_FOLDER+jpgFilename, 'rb') as image_file:
    content = image_file.read()

  image = types.Image(content=content)

  response = client.text_detection(image=image)
  print(response)
  texts = response.text_annotations

  result_file = open(RESULT_FOLDER+txtFilename,"a+")
  
  write_txt(texts[0].description, result_file)

  result_file.close()

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_pdf(pdf_filename):
  pages = convert_from_path(UPLOAD_FOLDER+pdf_filename)
  page_number = 0

  for page in pages:
    page_number += 1
    page.save(CONVERT_FOLDER+pdf_filename.rsplit('.', 1)[0]+str(page_number)+'.jpg', 'JPEG')

  return page_number


@app.route('/', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      
      page_count = convert_pdf(filename)
      hash.update(str(time.time()).encode('utf-8'))
      result_name = hash.hexdigest()+'.txt'

      for index in range(1,page_count+1):
        get_text(filename.rsplit('.', 1)[0]+str(index)+'.jpg', result_name)

      return send_file(RESULT_FOLDER+result_name, as_attachment=True)

  return '''
  <!doctype html>
  <title>Upload new File</title>
  <h1>Upload new File</h1>
  <form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Upload>
  </form>
  '''