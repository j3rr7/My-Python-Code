import urllib.request


inos="https://store.line.me/search/en?q=something"

stickerID = input("Input sticker id")
url = 'http://dl.stickershop.line.naver.jp/products/0/0/1/{}/iphone/stickerpack@2x.zip'.format(stickerID)
file_name = "data.zip"

'''
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8') # a `str`; this step can't be used if data is binary

# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve(url, file_name)
'''

# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    data = response.read() # a `bytes` object
    out_file.write(data)