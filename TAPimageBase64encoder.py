#TAP Image base64 encoder
# https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
import base64
fileName = input("Type in your picture path:\n")
image = open(fileName, 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
image_64_encode_string = image_64_encode.decode(encoding='UTF-8')
# print(image_64_encode)
with open("Base64Output.txt", "w") as text_file:
    text_file.write(image_64_encode_string)