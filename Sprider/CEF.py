# coding: utf-8
import os  # 引入文件操作库
# import sys

# reload(sys)
# sys.setdefaultencoding("utf-8")  #以上两行代码是设置默认的编码字符

# picpath = r'E:\Python_Doc\Images\Adult'
picpath = r'C:\Users\Administrator\Desktop\5'

def CEF(path):
    os.chdir(path)
    """
    CLean empty files, 清理空文件夹和空文件
    :param path: 文件路径，检查此文件路径下的子文件
    :return: None
    """
    files = os.listdir(path)  # 获取路径下的子文件(夹)列表
    for file in files:
        print 'Traversal at', file
        # filepath = path +"\\"+ file
        if os.path.isdir(file):  # 如果是文件夹
            if not os.listdir(file):  # 如果子文件为空
                os.rmdir(file)  # 删除这个空文件夹
        elif os.path.isfile(file):  # 如果是文件
            if os.path.getsize(file) == 0:  # 文件大小为0
                os.remove(file)  # 删除这个文件
    print path, 'Dispose over!'

if __name__ == "__main__":  # 执行本文件则执行下述代码
    # path = raw_input("Please input the files path:")  # 输入路径
    # CEF(path)
    print os.getcwd()     # 函数得到当前工作目录，
    CEF(picpath)