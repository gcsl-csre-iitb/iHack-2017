import io
import numpy as np

from google.cloud import vision
from google.cloud.vision import types

fileName = "sign.jpg"
client = vision.ImageAnnotatorClient()

with io.open(fileName, 'rb') as image_file:
        content = image_file.read()

image = types.Image(content=content)
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')



for label in labels:
    print(label.description)

# for label in labels:
#     print(label.description)
