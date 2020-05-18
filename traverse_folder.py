#  遍历文件夹文件名，写入文件

import os
path = "C:/Windows/System32/"

with open("D:/test.txt", 'w') as test:
    for root, dirs, files in os.walk(path):
        for f in files:
            print(os.path.join(root, f))
            test.writelines(os.path.join(root, f) + '\n')
