# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:26:42 2019

@author: Administrator
"""


import requests
import hmac
import hashlib
import base64
import time
import random
import json


def TencentOCR(picture):
    appid = '1259246971'
    secret_id = 'AKIDQ9f9RhGKgmgK9k85nGSyMVSHuHPHJ14M'
    secret_key = 'sZ3HE2gEtMdBVvjnAlKgoxtd5HD3dDZi'
    bucket = 'BUCKET'

    expired = time.time() + 2592000
    current = time.time()
    rdm = ''.join(random.choice("0123456789") for i in range(10))

    info = "a=" + appid + "&b=" + bucket + "&k=" + secret_id + "&e=" + \
        str(expired) + "&t=" + str(current) + "&r=" + str(rdm) + "&u=0&f="

    signindex = hmac.new(bytes(secret_key, 'utf-8'),
                         bytes(info, 'utf-8'), hashlib.sha1).digest()  # HMAC-SHA1加密
    # base64转码，也可以用下面那行转码
    sign = base64.b64encode(signindex + bytes(info, 'utf-8'))
    # sign=base64.b64encode(signindex+info.encode('utf-8'))

    url = "http://recognition.image.myqcloud.com/ocr/general"
    headers = {'Host': 'recognition.image.myqcloud.com',
               "Authorization": sign,
               }
    files = {'appid': (None, appid),
             'bucket': (None, bucket),
             'image': ('1.jpg', open(picture, 'rb'), 'image/jpeg')
             }

    r = requests.post(url, files=files, headers=headers)

    responseinfo = r.content
    data = responseinfo.decode('utf-8')

    json_data = json.loads(data)
    datas = json_data['data']['items']
    recognise = {}
    for obj in datas:
        recognise[obj['itemstring']] = obj
    return recognise


if __name__ == '__main__':
    beg = time.time()
    connect = TencentOCR(r'C:\Users\Administrator\Desktop\1.jpg')
    end = time.time()
    print(end - beg)
