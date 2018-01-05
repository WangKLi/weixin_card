import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
req = requests.get("https://pic1.zhimg.com/v2-a673dfe57ae53344194fdb8d4d5d6199_r.jpg",headers=headers)
img=req.content
with open('v2-a673dfe57ae53344194fdb8d4d5d6199_r.jpg','wb') as f:
    f.write(img)
