import io
import numpy as np

from google.cloud import vision
from google.cloud.vision import types

fileName = "output.png"
client = vision.ImageAnnotatorClient()

with io.open(fileName, 'rb') as image_file:
        content = image_file.read()

image = types.Image(content=content)
response = client.text_detection(image=image)
texts = response.text_annotations

text = texts[0].description
print('Texts:', text)

with io.open('imageText.txt', 'w') as imageText:
    imageText.write(text)
