#TAP image base64 decoder
#Work perfectly
import base64
txt_file_path = input("Type in your txt file path:\n")
txt_file = open(txt_file_path, 'rb') #open binary file in read mode
txt_file_read = txt_file.read()
img_64_decode = base64.b64decode(txt_file_read)
img_result = open('out_decoded.jpg', 'wb') # create a writable image and write the decoding result
img_result.write(img_64_decode)