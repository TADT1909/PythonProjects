#TAP image base64 encoder
#Work perfectly
# https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
import base64
import pyperclip
fileName = input("Type in your picture path:\n")
img = open(fileName, 'rb') #open binary file in read mode
img_read = img.read()
img_64_encode = base64.encodestring(img_read)
img_64_encode_string = img_64_encode.decode(encoding='UTF-8')
pyperclip.copy(img_64_encode_string)
with open("Base64output.txt", "w") as text_file:
    text_file.write(img_64_encode_string)