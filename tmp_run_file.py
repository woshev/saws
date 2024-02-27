#
import time
import os
import subprocess
import shutil

task_description={'task id':'',
                'ege type':'17',
                'topic':'',
                'task type id':'',
                'author':'',
                'number kpolyakov':'',
                'task description': '',
                'input data':'',
                'input file':'17-test.txt',
                'answer':'',
                'solve text Python':'None',
                'solve file Python':'17-test.py',
                'solve text Pascal':'',
                'solve file Pascal':'',                               
                'solve youtube':''
                }

def copy_code_and_data(path_code_student,task_description):
    #student -- путь к текущей задаче ученика котороуб необходимо выполнить
    #task_description -- описание данной задачи (словарь из файла yaml)
    # копирует файл ученика,файл решения и файл с входными данными во временную папку
    tmp_dir='tmp'
    os.makedirs(tmp_dir, exist_ok=True)
    #copy code student to tmp folder
    try:
        shutil.copy(path_code_student,tmp_dir)
        #copy code solution Python
        if task_description['solve file Python'] != 'None':
            path_code_solve= os.path.join(task_description['ege type']+'solve',task_description['solve file Python'])
            print(path_code_solve)
            shutil.copy(path_code_solve,tmp_dir)

        #copy input file to tmp folder
        if task_description['input file'] != 'None':
            path_input_file=os.path.join(task_description['ege type']+'data',task_description['input file'])
            shutil.copy(path_input_file,tmp_dir)
        return True
    except FileNotFoundError:
        return False



copy_code_and_data('D:\\База\\YandexDisk\\Школа\\10БДЗ\\Белов Максим\\02_Февраль\\2024.02.12\\17-1.py',task_description)

# Создаем временный файл с тестовыми данными в папке tmp
tmp_dir = 'tmp'
os.makedirs(tmp_dir,exist_ok=True)
data_file_path = os.path.join(tmp_dir, 'data.txt')

src_file='17data\\17-test.txt'
dst_folder='tmp'
shutil.copy(src_file,dst_folder)

timeout=10
function_file_path = 'D:\\База\\YandexDisk\\Школа\\ЕГЭ_1\\tmp\\17-1.py'
#print(function_file_path)
start_time = time.time()
process=subprocess.Popen(["python", os.path.basename(function_file_path)],cwd = 'D:\\База\\YandexDisk\\Школа\\ЕГЭ_1\\tmp', text=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Запускаем функцию из function.py
try:
    stdout,stderr=process.communicate(timeout=timeout)
    return_code=process.returncode
    end_time=time.time()
    execution_time=end_time-start_time
    print("stdout:", stdout)
    print("stderr:", stderr)
    print("return code:", return_code)
    print("execution time:", execution_time, "s")
except subprocess.TimeoutExpired:
    process.kill()
    print('Time limit')
    stdout,stderr=process.communicate()
    return_code=process.returncode
    end_time=time.time()
    execution_time=end_time-start_time
print(stdout)
if stdout == "2151 9630"+"\n":
    print(True)

# Удаляем временные файлы после использования
#os.remove(data_file_path)
#os.remove(function_file_path)

