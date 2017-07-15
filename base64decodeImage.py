# https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
import base64
img = open('in.jpg', 'rb')
img_read = img.read()
img_64_encode = base64.encodestring(img_read) # bytes type
img_64_decode = base64.decodestring(img_64_encode) # bytes type
img_result = open('out_decode.jpg', 'wb') # create a writable image and write the decoding result
img_result.write(img_64_decode)