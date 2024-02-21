# encoding=gb18030
import os
import datetime
import json
import requests


def ini_file(path, hou_zui, new_zudui):
    """

    :param hou_zui: �ļ���׺
    :param path:�ļ���·��
    :param new_zudui:�޸ĵ����ģʽ
    :return:
    """

    files = os.listdir(path)  # �������ڷ���ָ�����ļ��а������ļ����ļ��е����ֵ��б�
    for file in files:

        if os.path.isfile(path + "/" + file):
            filename, extension = os.path.splitext(file)  # �ָ�·��������·�������ļ���չ����Ԫ��

            if extension == hou_zui:
                ctime = os.path.getmtime(path + filename + hou_zui)  # ·���޸�ʱ�䣬���ظ���������ʾ��Ԫ����������
                create = datetime.date.fromtimestamp(ctime)  # �Ѽ�Ԫ����ת�������ڶ���
                now_date = datetime.date.today()  # ��ȡϵͳ��������

                if now_date == create:
                    with open(path + filename + hou_zui, "r", encoding='gb18030', errors='ignore') as f1, \
                            open("%s.bak" % path + filename + hou_zui, "w", encoding='gb18030',
                                 errors='ignore') as f2:

                        for line in f1:
                            if "���ģʽ=2" in line:
                                line = line.replace(line, new_zudui)
                            f2.write(line)
                    os.remove(path + filename + hou_zui)
                    os.rename("%s.bak" % path + filename + hou_zui, path + filename + hou_zui)

                url = 'https://oapi.dingtalk.com/robot/send?access_token=65611048d23ba36d7f4bafea75539fa3caf61f3553569dbfe90dcd60a05f8c3c'
                pagrem = {
                    "msgtype": "text",
                    "text": {
                        "content": "qw���ͣ�" + "��ʼ���ˣ�" + filename + hou_zui
                    },
                    "at": {
                        "atMobiles": [
                            "15757185534"  # ��Ҫ��д�Լ����ֻ��ţ�����ͨ���ֻ���@��Ӧ��
                        ],
                        "isAtAll": False  # �Ƿ�@�����ˣ�Ĭ�Ϸ�
                    }
                }
                headers = {
                    'Content-Type': 'application/json'
                }
                requests.post(url, data=json.dumps(pagrem), headers=headers)


ini_file(r"D:\�½��ļ���\�ж�ʱ���޸�\��ɫ����\\", '.ini', '���ģʽ=3\n')
