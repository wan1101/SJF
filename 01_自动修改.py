# coding:utf-8
import os


def updateFile(file, new_shunxu,new_anshi):
    """
    将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
    :param new_anshi: 按时执行任务
    :param new_shunxu: 顺序执行任务
    :param file: 文件路径
    :return: None
    """

    with open(file, "r") as f1, open("%s.bak" % file, "w") as f2:
        for line in f1:
            if "顺序执行任务=" in line:
                line = line.replace(line, new_shunxu)

            elif "||"in line:
                line=line.replace(line,'')

            elif "按时执行任务=" in line:
                line = line.replace(line, new_anshi)

            f2.write(line)
    os.remove(file)
    os.rename("%s.bak" % file, file)


updateFile(r"C:\Users\pc\Desktop\浅笑迷离←.ini", "顺序执行什么了\n","按时执行个p\n")
