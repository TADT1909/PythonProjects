"""
TAP image base64 encoder version 1.2
Being Developed
16 July 2017
  add encode Video both local and offline
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

def getFilePath():
  filePath = input("Your file path? \n")
def getFileName():
  fileName = input("File Name? ")
def getFileType():
  fileType = input("File Type? ")
def getUrl():
  url = input("Url? ")
def Download(url, fileName):
  with urllib.request.urlopen(url) as response, open(fileName, 'wb') as out_file:
      data = response.read() # a `bytes` object
      out_file.write(data)
def Base64encode(filePath):
  # read input file
  img = open(filePath, 'rb') #open binary file in read mode
  img_read = img.read()
  # encode file
  img_64_encode = base64.encodestring(img_read)
  img_64_encode_string = img_64_encode.decode(encoding='UTF-8')
  # get full format text
  full_string = "data:"
  full_string += mediaType
  full_string += "/"
  full_string += fileType
  full_string += ";base64,"
  full_string += img_64_encode_string
  # copy text to clipboard
  pyperclip.copy(full_string)
  # write text to .txt file
  with open("Base64output.txt", "w") as txt_file:
    txt_file.write(full_string)
def DeleteFiles():
  delete_option = input("Do you want to delete temp files? [y/n] ")
  if delete_option=="y" or delete_option=="yes" or delete_option=="Y" or delete_option=="Yes":
    os.remove("Base64output.txt")
    os.remove(fileName)
  if delete_option=="n" or delete_option=="no" or delete_option=="N" or delete_option=="No":
    exit()

ans = True
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
      mediaType = "image"
      filePath = getFilePath()
      fileName = getFileName()
      fileType = getFileType()
      Base64encode(filePath)
      DeleteFiles()
    elif ans=="2":
      print("\n Encode Online Image")
      mediaType = "image"
      fileName =getFileName()
      fileType =getFileType()
      url = getUrl()
      Download(url, fileName)
      Base64encode(filePath)
      DeleteFiles()
    elif ans=="3":
      print("\n Encode Local Video")
      mediaType = "video"
      filePath = getFilePath()
      fileName =getFileName()
      fileType =getFileType()
      Base64encode(filePath)
      DeleteFiles()
    elif ans=="4":
      print("\n Encode Online Image")
      mediaType = "video"
      fileName =getFileName()
      fileType =getFileType()
      url = getUrl()
      Download(url, fileName)
      Base64encode(filePath)
      DeleteFiles()
    elif ans=="5":
      print("\n Goodbye - TAP Team")
      exit()
    elif ans !="":
      print("\n Not Valid Choice!\nTry again")