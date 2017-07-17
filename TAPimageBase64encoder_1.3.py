"""
TAP image base64 encoder version 1.3
Being Developed
17 July 2017
  fix error
  run perfectly
16 July 2017
  use functions
  add encode video function
  error:
      Traceback (most recent call last):
    File "TAPimageBase64encoder_1.2.py", line 71, in <module>
      EncodeBase64(fileName, fileType, mediaType)
    File "TAPimageBase64encoder_1.2.py", line 39, in EncodeBase64
      file = open(fileName, 'rb')
TypeError: expected str, bytes or os.PathLike object, not NoneType
15 July 2017
  use with any image file type
  output to .txt file and clipboard

Preference:
https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
"""
import os
import base64
import pyperclip
import urllib.request

def GetUrl():
  url = input("Url:\n")
  return url
def GetFileName():
  fileName = input("Picture Name?\n")
  return fileName
def GetFileType():
  fileType = input("Picture Type?\n")
  return fileType
def DownloadFile(url):
  with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
      data = response.read() # a `bytes` object
      out_file.write(data)
def DeleteFile():
  prompt = input("Do you want to delete files? [y/n]\t")
  if prompt == "y" or prompt == "Y" or prompt == "yes" or prompt == "Yes":
    os.remove(fileName)
    os.remove("Base64output.txt")
    print("Files deleted!")
  elif prompt == "n" or prompt == "N" or prompt == "no" or prompt == "No":
    print("Files NOT deleted!")
  else :
    print("\n Not Valid Choice!\n Files NOT deleted!")
def Completed():
  print("\nTask Completed!")
def EncodeBase64(fileName, fileType, mediaType):
  # read input file
  file = open(fileName, 'rb') #open binary file in read mode
  file_read = file.read()
  # encode file
  file_64_encode = base64.encodestring(file_read)
  file_64_encode_string = file_64_encode.decode(encoding='UTF-8')
  # get full format text
  full_string = "data:"
  full_string += mediaType
  full_string += "/"
  full_string += fileType
  full_string += ";base64,"
  full_string += file_64_encode_string
  # copy text to clipboard
  pyperclip.copy(full_string)
  # write text to .txt file
  with open("Base64output.txt", "w") as txt_file:
    txt_file.write(full_string)
ans=True
while ans:
    print ("""
    1.Encode Local Image
    2.Encode Online Image
    3.Encode Local Video
    4.Encode Online Video
    5.Exit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      print("\n Encode Local Image")
      fileName = GetFileName()
      fileType = GetFileType()
      mediaType = "image"
      EncodeBase64(fileName, fileType, mediaType)
      DeleteFile()
      Completed()
      exit()
    elif ans=="2":
      print("\n Encode Online Image")
      fileName = GetFileName()
      fileType = GetFileType()
      mediaType = "image"
      url = GetUrl()
      DownloadFile(url, fileName)
      EncodeBase64(fileName, fileType, mediaType)
      DeleteFile()
      Completed()
      exit()
    elif ans=="3":
      print("\n Encode Local Video")
      fileName = GetFileName()
      fileType = GetFileType()
      mediaType = "video"
      EncodeBase64(fileName, fileType, mediaType)
      DeleteFile()
      Completed()
      exit()
    elif ans=="4":
      print("\n Encode Online Video")
      fileName = GetFileName()
      fileType = GetFileType()
      mediaType = "video"
      url = GetUrl()
      DownloadFile(url, fileName)
      EncodeBase64(fileName, fileType, mediaType)
      DeleteFile()
      Completed()
      exit()
    elif ans=="5":
      print("\n Goodbye - TAP Team")
      exit()
    elif ans !="":
      print("\n Not Valid Choice! Try again")"""
TAP image base64 encoder version 1.3
Being Developed
17 July 2017
  fix error
  run perfectly
16 July 2017
  use functions
  add encode video function
  error:
      Traceback (most recent call last):
    File "TAPimageBase64encoder_1.2.py", line 71, in <module>
      EncodeBase64(fileName, fileType, mediaType)
    File "TAPimageBase64encoder_1.2.py", line 39, in EncodeBase64
      file = open(fileName, 'rb')
TypeError: expected str, bytes or os.PathLike object, not NoneType
15 July 2017
  use with any image file type
  output to .txt file and clipboard

Preference:
https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
"""
import os
import base64
import pyperclip
import urllib.request

def GetUrl():
  url = input("Url:\n")
  return url
def GetFileName():
  fileName = input("Picture Name?\n")
  return fileName
def GetFileType():
  fileType = input("Picture Type?\n")
  return fileType
def DownloadFile(url):
  with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
      data = response.read() # a `bytes` object
      out_file.write(data)
def DeleteFile():
  prompt = input("Do you want to delete files? [y/n]\n")
  if prompt == "y" or prompt == "Y" or prompt == "yes" or prompt == "Yes":
    os.remove(fileName)
    os.remove("Base64output.txt")
    print("Files deleted!")
  elif prompt == "n" or prompt == "N" or prompt == "no" or prompt == "No":
    print("Files NOT deleted!")
  else :
    print("\n Not Valid Choice!\n Files NOT deleted!")

def EncodeBase64(_fileName, _fileType, _mediaType):
  # read input file
  file = open(_fileName, 'rb') #open binary file in read mode
  file_read = file.read()
  # encode file
  file_64_encode = base64.encodestring(file_read)
  file_64_encode_string = file_64_encode.decode(encoding='UTF-8')
  # get full format text
  full_string = "data:"
  full_string += mediaType
  full_string += "/"
  full_string += fileType
  full_string += ";base64,"
  full_string += file_64_encode_string
  # copy text to clipboard
  pyperclip.copy(full_string)
  # write text to .txt file
  with open("Base64output.txt", "w") as txt_file:
    txt_file.write(full_string)
ans=True
while ans:
    print ("""
    1.Encode Local Image
    2.Encode Online Image
    3.Encode Local Video
    4.Encode Online Video
    5.Exit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      print("\n Encode Local Image")
      fileName = GetFileName()
      fileType = GetFileType()
      mediaType = "image"
      EncodeBase64(fileName, fileType, mediaType)
      DeleteFile()
      exit()
    elif ans=="2":
      print("\n Encode Online Image")
      fileName = GetFileName()
      fileType = GetFileType()
      mediaType = "image"
      url = GetUrl()
      DownloadFile(url, fileName)
      EncodeBase64(fileName, fileType, mediaType)
      DeleteFile()
      exit()
    elif ans=="3":
      print("\n Encode Local Video")
      fileName = GetFileName()
      fileType = GetFileType()
      mediaType = "video"
      EncodeBase64(fileName, fileType, mediaType)
      DeleteFile()
      exit()
    elif ans=="4":
      print("\n Encode Online Video")
      fileName = GetFileName()
      fileType = GetFileType()
      mediaType = "video"
      url = GetUrl()
      DownloadFile(url, fileName)
      EncodeBase64(fileName, fileType, mediaType)
      DeleteFile()
      exit()
    elif ans=="5":
      print("\n Goodbye - TAP Team")
      exit()
    elif ans !="":
      print("\n Not Valid Choice! Try again")