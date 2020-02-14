import sys
import base64

with open('HelloClient.jpg', 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read())
    image_encoded = encoded_string.decode('utf-8')
