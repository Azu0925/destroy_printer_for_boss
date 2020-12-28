import random
import sys
import requests
import json

jp = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん"]

user = ''
for i in range(0, 3):
    user += jp[random.randint(0, len(jp) - 1)]

text = ''
for i in range(0, 100):
    text += jp[random.randint(0, len(jp) - 1)]

def send(user, text):
    url = 'http://hirosuke-pi.iobb.net:8880/print'
    params = {
       'user': user,
       'text': text, 
       'state': 'Web Service'
    }

    header = {
        'Content-Type': 'application/json'
    }

    r_post = requests.post(url, data=json.dumps(params), headers=header)
    data_lists = json.loads((r_post.text))

    return data_lists

print(send(user, text))