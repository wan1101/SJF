# encoding=gb18030
import os
import datetime
import json
import requests


def ini_file(path,hou_zui, new_zudui):
    """

    :param hou_zui: 文件后缀
    :param path:文件的路径
    :param new_zudui:修改的组队模式
    :return:
    """

    files = os.listdir(path)  # 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    # print(files)

    for file in files:
        # print(file)
        if os.path.isfile(path + "/" + file):
            # os.path.isfile(path) 判断路径是否为文件
            # print(file+'这是一个文件')
            filename, extension = os.path.splitext(file)
            # 分割路径，返回路径名和文件扩展名的元组

            if extension == hou_zui:
                print(filename + '这是.ini结尾的文件')
                ctime = os.path.getmtime(path + filename + hou_zui)  # 路径修改时间，返回浮点数：表示纪元以来的秒数
                create = datetime.date.fromtimestamp(ctime)  # 把纪元秒数转换成日期时间对象
                now_date = datetime.date.today()  # 读取系统本地时间
                print(now_date)
                print(create)

                if now_date == create:
                    print("文件创建日期和当前时间一致！！")
                    with open(path + filename + hou_zui, "r", encoding='gb18030', errors='ignore') as f1, \
                            open("%s.bak" % path + filename + hou_zui, "w", encoding='gb18030', errors='ignore') as f2:
                        for line in f1:
                            if "组队模式=2" in line:
                                line = line.replace(line, new_zudui)
                            f2.write(line)
                    os.remove(path + filename + hou_zui)
                    os.rename("%s.bak" % path + filename + hou_zui, path + filename + hou_zui)

                url = 'https://oapi.dingtalk.com/robot/send?access_token=65611048d23ba36d7f4bafea75539fa3caf61f3553569dbfe90dcd60a05f8c3c'
                pagrem = {
                    "msgtype": "text",
                    "text": {
                        "content": "qw推送："+"开始打工了：" + filename + hou_zui
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
                print("是否执行")
                requests.post(url, data=json.dumps(pagrem), headers=headers)


ini_file(r"D:\新建文件夹\判断时间修改\角色配置\\",'.ini', '组队模式=3\n')
