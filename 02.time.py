import os
import datetime

filePath = r"C:\Users\pc\Desktop\浅笑迷离←.ini"
ctime = os.path.getctime(filePath)  # 路径创建时间，返回浮点数：表示纪元以来的秒数
create = datetime.datetime.fromtimestamp(ctime)  # 把纪元秒数转换成日期时间对象
nowdate = datetime.datetime.now()  # 读取系统本地时间

print(nowdate)
print(create)
print(ctime)


def updateFile(file, new_shunxu, new_anshi):
    if create == create:
        print("两个日期的是一致的~~")

        with open(file, "r") as f1, open("%s.bak" % file, "w") as f2:
            for line in f1:
                if "顺序执行任务=" in line:
                    line = line.replace(line, new_shunxu)

                elif "||" in line:
                    line = line.replace(line, '')

                elif "按时执行任务=" in line:
                    line = line.replace(line, new_anshi)

                f2.write(line)
        os.remove(file)
        os.rename("%s.bak" % file, file)

    else:
        print("创建时间不是当前时间哦！！")


updateFile(r"C:\Users\pc\Desktop\浅笑迷离←.ini", "顺序执行什么了\n", "按时执行个p\n")
