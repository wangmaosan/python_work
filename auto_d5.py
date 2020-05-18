import os

folder = r'C:\Users\WXS\Desktop\Test_files\auto_drs'
script = os.path.join(folder, 'auto_launcher.bat')


def update_drs():
    with open(script, 'w') as file:
        file.writelines('SET d5exe="E:/D5 Render Preview 701 auto/d5_launcher.exe"' + '\n' + '\n')
        for root, dirs, files in os.walk(folder):
            for file_name in files:
                file_name_group = file_name.split('.')
                if file_name_group[1] == 'drs':
                    line = r'start "" /wait %d5exe% -startFile=' + '"%s"' % os.path.join(folder, file_name_group[0], file_name)
                    file.writelines(line + '\n')
                    file.writelines('ping -n 3 127.0.0.1>nul' + '\n' + '\n')


if __name__ == '__main__':
    # update_drs()
    print('脚本文件位置: ' + '\n' + script)
    os.system(command=script)
