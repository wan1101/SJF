#!/usr/bin/env python  
# -*- coding:utf-8 _*-

import json
import time

import requests


def message(sss):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=65611048d23ba36d7f4bafea75539fa3caf61f3553569dbfe90dcd60a05f8c3c'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "qw推送："+sss
        },
        "at": {
            "atMobiles": [
                "15757185534"  # 需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": False  # 是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)


def readtxt():
    f = open(r'C:\Users\pc\Desktop\新建 文本文档.txt', encoding='gb18030', errors='ignore')
    sss = ''.join(f.readlines()[-1])
    f.close()
    nowstr = str(int(time.time()))
    print(nowstr)
    # print (int(nowstr)-int(sss[-11:]))
    if int(nowstr)-int(sss[-11:]) <20:
        message(sss)
    else:
        print("不用返回")


if __name__ == "__main__":
    readtxt()

