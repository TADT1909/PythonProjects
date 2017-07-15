# TAP image base64 encoder version 1.0
# Work perfectly
# 15 July 2017
# use with any image file type
# output to .txt file and clipboard
# Preference:
# https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
import base64
import pyperclip
# get input file path
fileName = input("Type in your picture path:\n")
fileType = input("Type in your file type:\n")
# read input file
img = open(fileName, 'rb') #open binary file in read mode
img_read = img.read()
# encode file
img_64_encode = base64.encodestring(img_read)
img_64_encode_string = img_64_encode.decode(encoding='UTF-8')
# get full format text
full_string = ""
full_string = "data:image/"
full_string += fileType
full_string += ";base64,"
full_string += img_64_encode_string
# copy text to clipboard
pyperclip.copy(full_string)
# write text to .txt file
with open("Base64output.txt", "w") as txt_file:
	txt_file.write(full_string)

