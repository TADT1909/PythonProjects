# TAP image base64 encoder version 1.1
# Work perfectly
# 15 July 2017
# use with any image file type
# output to .txt file and clipboard
# Preference:
# https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
import base64
import pyperclip
import urllib.request

ans=True
while ans:
    print ("""
    1.Encode Local Image
    2.Encode Online Image
    3.Exit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      	print("\n Encode Local Image")
    	# get input file path*
		filePath = input("Type in your picture path:\n")
      	exit()
    elif ans=="2":
      print("\n Encode Online Image")
      exit()
    elif ans=="3":
      print("\n Goodbye - TAP Team")
      exit()
    elif ans !="":
      print("\n Not Valid Choice Try again")

##########
# get input file link*
url = ""
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    data = response.read() # a `bytes` object
    out_file.write(data)
# get input file name
fileName = input("Picture Name? ")
##########
# get input file type
fileType = input("Picture Type? ")
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