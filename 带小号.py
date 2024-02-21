# coding:utf-8
import os
import datetime


def updateFile(namelist, new_shunxu, new_anshi, new_duiwu):
    """
    将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
    :param namelist: 角色名称
    :param new_anshi: 按时执行任务
    :param new_shunxu: 顺序执行任务
    :return: None
    """
    global file, name

    for name in namelist:
        file = r"C:\\天龙小蜜\\角色配置\\" + name + ".ini"

    ctime = os.path.getctime(file)  # 路径创建时间，返回浮点数：表示纪元以来的秒数
    create = datetime.datetime.fromtimestamp(ctime)  # 把纪元秒数转换成日期时间对象
    now_date = datetime.datetime.now()  # 读取系统本地时间

    if create == now_date:
        print("文件创建日期和当前时间一致！！")
        with open(file, "r") as f1, open("%s.bak" % file, "w") as f2:
            for line in f1:
                if "顺序执行任务=" in line:
                    line = line.replace(line, new_shunxu)
                elif "按时执行任务=" in line:
                    line = line.replace(line, new_anshi)
                elif "队伍成员=" in line:
                    line = line.replace(line, "队伍成员=" + name + "\n")
                f2.write(line)
        os.remove(file)
        os.rename("%s.bak" % file, file)
    else:
        print("日期不一样，关闭文件！！")


namelist = ["佳梦ゞ若辰", "無み瑺"]
duiwu = "队伍成员=像我这样的人|梨酒．|佳梦ゞ若辰|無み瑺|り．小妮|﹎不知火舞"
updateFile(namelist, "顺序执行任务=挂机打怪\n", "按时执行任务=\n", duiwu)
