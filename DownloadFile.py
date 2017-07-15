# Download a file
# 15 July 2017
# https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
import urllib.request
url = "https://www.google.com.vn/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
file_name = "google.png"
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    data = response.read() # a `bytes` object
    out_file.write(data)