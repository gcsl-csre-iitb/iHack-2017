import io
import numpy as np
# from google.cloud import vision_client
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

fileName = "train_test.jpg"

with io.open(fileName, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
response = client.text_detection(image=image)
# print(type(response))
texts = response.text_annotations
# print('Texts:', texts)

# for text in texts:
       	# print(type(text.description))
    # print('\t"{}"'.format(text.description))

    # vertices = (['({},{})'.format(vertex.x, vertex.y)
        # for vertex in text.bounding_poly.vertices])


    # print('bounds: {}'.format(','.join(vertices)))
