import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
  os.path.dirname(__file__),
  'media/out/Assignment_21.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
  content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client. response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')


# for text in texts[0]:
# for text in texts[:(len(texts)//2)]:
print('"{}"'.format(texts[0].description), end=" ")

  # vertices = (['({},{})'.format(vertex.x, vertex.y)
  # for vertex in text.bounding_poly.vertices])
  # print('bounds: {}'.format(','.join(vertices)))
