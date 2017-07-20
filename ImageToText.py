#! python3
# Python 3 Image to text
# 20.07.17 fixed bugs
# require to install pillow, numpy
# pip install pillow
# pip install numpy
# -*- coding: UTF-8 -*-
from PIL import Image
import numpy as np
import random
import math
def convert(num) :
    a0 = ['■','■','■','■','■','■','■','■']
    a1 = ['$','#','%','$','&','@','@']
    a2 = ['Q','W','E','R','Y','U','O']
    a3 = ['I','L','I','L','J','I','J']
    a4 = ['a','s','c','v','x','n','i']
    a5 = ['.',',',':',' ','\'',' ','`']
    a6 = ['.',' ','`',' ',' ','`',' ']

    rand = random.randint(0,6)
    if num in range(0,40) :
        return a6[rand]
    if num in range(40,90) :
        return a5[rand]
    if num in range(90,130) :
        return a4[rand]
    if num in range(130,170) :
        return a3[rand]
    if num in range(170,200) :
        return a2[rand]
    if num in range(200,230) :
        return a1[rand]
    if num in range(230,255) :
        return a0[rand]
    return ' '

size = 200 #need to customize

filename = ""
filename = input("Nhap vao ten file (Chu y de cung folder voi chuong trinh) \n Filename : ")

image = Image.open(filename).convert('L')
width, height = image.size
height = int(math.floor(size*width /height))
width = size

image = image.resize((width, height),Image.ANTIALIAS)

image.load()
data = np.asarray( image, dtype="int32" )
out = [["" for x in range(width)] for y in range(height)]

for i in range(height) :
    for j in range(width) :
        out[i][j] = convert(data[i][j])
with open("image.txt",'w', encoding='utf-8') as f:
    string = ""
    for i in range(height) :
        for j in range(width) :
            string += out[i][j]
        string += " \n"
    f.write(string)