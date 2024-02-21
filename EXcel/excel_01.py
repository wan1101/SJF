import csv


def csv_file(new_file, old_file, column):
    """

    :param new_file: 提取后保存的新文件路径
    :param old_file: 需要提取内容的文件路径
    :param column: 内容所在的行
    :return:
    """
    new = open(new_file, 'a', encoding='utf-16')

    with open(old_file, encoding='utf-16') as f:
        reader = csv.reader(f)  # 读取当前文件的列表
        print(type(reader))  # 文件的类型
        #   获取某一列
        for i in reader:
            print(i[column]) # 第四列
            num = i[column][0:7]   # 分割字符串
            print(num)
            new.write(num + '\n')

    # new.close()
    #   获取每一行
    # for row in reader:
    #     print(row)

    #   获取某一行
    # result = list(reader)
    # print(result[1])


csv_file(r"C:\Users\pc\Desktop\道闸编号4.csv", r"E:\64大华园区\文档\停车场道闸.csv", 4)
