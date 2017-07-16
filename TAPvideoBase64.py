import base64
import pyperclip
import urllib.request

url = input("Url? ")
fileName = input("Type in your picture path:\n")
with urllib.request.urlopen(url) as response, open(fileName, 'wb') as out_file:
      data = response.read() # a `bytes` object
      out_file.write(data)
fileType = input("Type in your file type:\n")
img = open(fileName, 'rb') #open binary file in read mode
img_read = img.read()
img_64_encode = base64.encodestring(img_read)
img_64_encode_string = img_64_encode.decode(encoding='UTF-8')
full_string = ""
full_string = "data:video/"
full_string += fileType
full_string += ";base64,"
full_string += img_64_encode_string
# copy text to clipboard
pyperclip.copy(full_string)
# write text to .txt file
with open("Base64output.txt", "w") as txt_file:
  txt_file.write(full_string)

