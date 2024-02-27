import os

print('start')
if os.path.exists('C:\\Users\\Dima\\YandexDisk\\Школа\\ЕГЭ_1'+'\\17solve\\'+'17-1.pas'):
    f_pas=open('C:\\Users\\Dima\\YandexDisk\\Школа\\ЕГЭ_1'+'\\17solve\\'+'17-1.pas','r')
    print(f_pas.read())
    f_pas.close()

import subprocess

pascal_file_path = 'C:\\Users\\Dima\\YandexDisk\\Школа\\ЕГЭ_1'+'\\17solve\\'+'17-1.pas'

try:
    # Компиляция Pascal файла
    subprocess.check_call(['fpc', pascal_file_path])

    # Запуск исполняемого файла
    executable_path = pascal_file_path.replace('.pas', '')
    result = subprocess.check_output([executable_path], universal_newlines=True)

    print("Результат выполнения программы:")
    print(result)

except subprocess.CalledProcessError as e:
    print(f"Ошибка выполнения программы: {e}")
