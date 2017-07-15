# https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
import base64
image = open('in.jpg', 'rb')
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
image_64_decode = base64.decodestring(image_64_encode) 
image_result = open('out_decode.jpg', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)