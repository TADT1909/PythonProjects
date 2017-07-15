# https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
import base64
img = open('in.jpg', 'rb') #open binary file in read mode
img_read = img.read()
img_64_encode = base64.encodestring(img_read)
img_64_encode_string = img_64_encode.decode(encoding='UTF-8')
print(img_64_encode)
with open("output.txt", "w") as text_file:
    text_file.write(img_64_encode_string)