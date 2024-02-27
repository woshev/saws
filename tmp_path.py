import os
import shutil
import re
import time
import subprocess
import yaml
import tkinter as tk
import datetime

class Task():
    def __init__(self,app=None):
        if app != None:
            self.app=app
        #super().__init__(parent)
        with open(os.getcwd()+'\\setting.yml','r',encoding='utf-8') as file:
            setting_data=yaml.safe_load(file)

        self.folder_data_base=os.getcwd()
        self.folder_path = setting_data["folder_path"]+'\\'+setting_data["class"]
        self.folder_data=setting_data["folder_data"]
        self.tmp_folder = setting_data["tmp_folder"]
        #folder_path = 'C:\\Users\\Dima\\YandexDisk\\Школа\\10БДЗ'
        self.list_stop_path_name=['task and data']
        # Получаем дерево путей
        self.path_tree = self.build_path_tree(self.folder_path)


        self.employee_list=None
        self.current=setting_data["current"]
        self.student_list=[i for i in self.path_tree.keys()]
        self.data=None
        self.month=setting_data["month"]
        self.date=setting_data["date"]
        self.class_name=setting_data["class"]
        try:
            if self.date in setting_data["task_list"][self.class_name].keys():
                self.task_list=setting_data["task_list"][self.class_name][self.date]
        except:
            self.task_list=['17-1']
        #self.run_code('D:\\База\\YandexDisk\\Школа\\10БДЗ\\Белов Максим\\02_Февраль\\2024.02.12\\17-1.py')

    def build_path_tree(self,folder_path):
        path_tree = {}
        with os.scandir(folder_path) as entries:
            for entry in entries:
                if entry.is_dir() and entry.name not in self.list_stop_path_name:
                    subfolder_path = os.path.join(folder_path, entry.name)
                    path_tree[entry.name] = self.build_path_tree(subfolder_path)
                elif entry.name not in self.list_stop_path_name:
                    path_tree.setdefault('files', []).append(entry.name)
        return path_tree

    def current_file(self,paths,current,task_list):
        if task_list == ['']:
            return False,current,None    
        if task_list.index(current[-1])< len(task_list):
            if paths[current[0]][current[1]][current[2]] !={}:
                task_name=None
                for i in paths[current[0]][current[1]][current[2]]['files']:
                    task,topic= self.extract_task_and_topic_numbers(i)
                    if task != None and topic != None and str(topic)+'-'+str(task) == current[-1]: 
                        task_name=i
                        break
                    elif topic == None and current[-1].split('-')[1]== str(task):
                        task_name =i
                        break
                
            else:
                task_name=None
        else:
            return False,current,task_name
        return True,current,task_name

    def current_file_c_work(self,paths,current,task_list):
        if task_list == ['']:
            return False,current,None    
        if task_list.index(current[-1])< len(task_list):
            if paths[current[0]] !={}:
                task_name=None
                for i in paths[current[0]]['files']:
                    task,topic= self.extract_task_and_topic_numbers(i)
                    if task != None and topic != None and str(topic)+'-'+str(task) == current[-1]: 
                        task_name=i
                        break
                    elif topic == None and current[-1].split('-')[1]== str(task):
                        task_name =i
                        break
                
            else:
                task_name=None
        else:
            return False,current,task_name
        return True,current,task_name
    

    def next_file(self, paths: dict,current:list,task_list:list):
        student_list=[i for i in self.path_tree.keys()]
        if task_list.index(current[-1])+1< len(task_list):
            current[-1]=task_list[task_list.index(current[-1])+1]
            if paths[current[0]][current[1]][current[2]] !={}:
                task_name=None
                for i in paths[current[0]][current[1]][current[2]]['files']:
                    task,topic= self.extract_task_and_topic_numbers(i)  
                    if task != None and topic != None and str(topic)+'-'+str(task) == current[-1]: 
                        task_name=i
                        break
                    elif topic == None and current[-1].split('-')[1]== str(task):
                        task_name =i
                        break

                
            else:
                task_name=None
        else:
            if student_list.index(current[0])+1 < len(student_list):
                current[0] = student_list[student_list.index(current[0])+1]
                current[-1] = task_list[0]
                if paths[current[0]][current[1]][current[2]] !={}:
                    task_name=None
                    for i in paths[current[0]][current[1]][current[2]]['files']:
                        task,topic= self.extract_task_and_topic_numbers(i)
                        if task != None and topic != None and str(topic)+'-'+str(task) == current[-1]: 
                            task_name=i
                            break
                        elif topic == None and current[-1].split('-')[1]== str(task):
                            task_name =i
                            break

                else:
                    task_name=None
            else:
                if current[-1] == task_list[-1]:
                    return False,current,''
                if paths[current[0]][current[1]][current[2]] !={} and paths[current[0]][current[1]][current[2]]['files'] != ['result.txt']:
                    task_name=paths[current[0]][current[1]][current[2]]['files'][task_list.index(current[-1])]
                else:
                    task_name=''

                
                return True,current,task_name
        return True,current,task_name

    def next_file_c_work(self, paths: dict,current:list,task_list:list):
        student_list=[i for i in self.path_tree.keys()]
        if task_list.index(current[-1])+1< len(task_list):
            current[-1]=task_list[task_list.index(current[-1])+1]
            if paths[current[0]] !={}:
                task_name=None
                for i in paths[current[0]]['files']:
                    task,topic= self.extract_task_and_topic_numbers(i)  
                    if task != None and topic != None and str(topic)+'-'+str(task) == current[-1]: 
                        task_name=i
                        break
                    elif topic == None and current[-1].split('-')[1]== str(task):
                        task_name =i
                        break

                
            else:
                task_name=None
        else:
            if student_list.index(current[0])+1 < len(student_list):
                current[0] = student_list[student_list.index(current[0])+1]
                current[-1] = task_list[0]
                if paths[current[0]] !={}:
                    task_name=None
                    for i in paths[current[0]]['files']:
                        task,topic= self.extract_task_and_topic_numbers(i)
                        if task != None and topic != None and str(topic)+'-'+str(task) == current[-1]: 
                            task_name=i
                            break
                        elif topic == None and current[-1].split('-')[1]== str(task):
                            task_name =i
                            break

                else:
                    task_name=None
            else:
                if current[-1] == task_list[-1]:
                    return False,current,''
                if paths[current[0]] !={} and paths[current[0]]['files'] != ['result.txt']:
                    task_name=paths[current[0]]['files'][task_list.index(current[-1])]
                else:
                    task_name=''

                
                return True,current,task_name
        return True,current,task_name

    def next_student(self,paths: dict,current:list,task_list:list):
        student_list=[i for i in self.path_tree.keys()]
        if student_list.index(current[0])+1 < len(student_list):
            current[0] = student_list[student_list.index(current[0])+1] 
        else:
            if task_list.index(current[-1]) +1< len(task_list):
                current[-1]=task_list[task_list.index(current[-1])+1]
                current[0] = student_list[0]
            else:
                return False,current
        return True,current  

    def copy_code_and_data(self,path_code_student,task_description):
        # return True если удалось скопировать указанный файл иначе возвращает False
        #student -- путь к текущей задаче ученика котороуб необходимо выполнить
        #task_description -- описание данной задачи (словарь из файла yaml)
        # копирует файл ученика,файл решения и файл с входными данными во временную папку
        
        os.makedirs(self.tmp_folder, exist_ok=True)
        #copy code student to tmp folder
        try:
            shutil.copy(path_code_student,self.tmp_folder)
            print("good")
            #copy code solution Python
            '''if task_description['solve file Python'] != None:
                path_code_solve= os.path.join(str(task_description['ege type'])+'solve',task_description['solve file Python'])
                print(path_code_solve)
                shutil.copy(path_code_solve,self.tmp_folder)'''

            #copy input file to tmp folder
            if task_description['input file'] != None:
                path_input_file=os.path.join(str(task_description['ege type'])+'data',task_description['input file'])
                print("input_file",path_input_file)
                shutil.copy(path_input_file,self.tmp_folder)
            return True
        except FileNotFoundError:
            return False

    def extract_task_and_topic_numbers(self,string):
        # Шаблон для поиска номера задачи и номера темы
        #pattern = r'(\d+)(?:-(\d+))?.py'
        pattern = r'(\d+)[^\d]*(\d+)?\.py'
        # Поиск совпадений по шаблону в строке
        match = re.search(pattern, string)
        if match:
            number=match.groups()
            if match.group(2) == None:
                topic_number = None
                task_number = int(match.group(1))
                #print(task_number)
            elif match.group(1) != None and match.group(2) != None:
                topic_number = int(match.group(1))
                task_number = int(match.group(2))
            return task_number, topic_number
        else:
            # Номер задачи не найден
            return None, None
    
    def run_student_code_all(self,data=None):
        if data != None:
            #запускает код студента и записывает полученные результаты и сам код в employee_list
            print("wait", data)
            count=0
            count_all=0
            for student_name,student_value in self.employee_list.items():
                if student_name != "task":
                    for task_name in student_value.values():
                        if task_name["task_path_name"] != None:
                            count_all+=1
            for student_name,student_value in self.employee_list.items():
                if student_name == "task":
                    task_list=student_value
                else:
                    for task_name,task in student_value.items():
                        if task['task_path_name'] != None:
                            current=[student_name,self.month,task['task date'],task_name,task['task_path_name']]
                            auto_check,stdout,stderr,return_code,execution_time,correct_ans,code=self.run_student_code(current,task_list)
                            print("Ученик {:<15}  Задача  {:<20}  Прогресс {:7.2f}".format(student_name,task_name,count/count_all*100))
                            count+=1
                            print( repr(stdout),repr(correct_ans))
                            if execution_time == False:
                                task["execution_time"]=execution_time
                                task["student_code"] = code
                            else:
                                task["execution_time"]=execution_time
                                task["correct_answer"]=correct_ans
                                task["student_stdout"]=stdout
                                task["student_stderr"]=stderr
                                task["student_return_code"]=return_code
                                task["student_code"] = code
                                if auto_check:
                                    task["auto_check"]=auto_check
                                    task["grade"]=1
                                else:
                                    task["auto_check"]=auto_check
                                    task["grade"]=0

            print("good")
            return self.employee_list
        else:
            #запускает код студента и записывает полученные результаты и сам код в employee_list
            print("wait")
            count=0
            count_all=0
            for student_name,student_value in self.employee_list.items():
                if student_name != "task":
                    for task_name in student_value.values():
                        if task_name["task_path_name"] != None:
                            count_all+=1
            for student_name,student_value in self.employee_list.items():
                if student_name == "task":
                    task_list=student_value
                else:
                    for task_name,task in student_value.items():
                        if task['task_path_name'] != None:
                            current=[student_name,self.month,self.date,task_name,self.employee_list[student_name][task_name]['task_path_name']]
                            auto_check,stdout,stderr,return_code,execution_time,correct_ans,code=self.run_student_code(current,task_list)
                            print("Ученик {:<15}  Задача  {:<20}  Прогресс {:7.2f}".format(student_name,task_name,count/count_all*100))
                            count+=1
                            print( repr(stdout),repr(correct_ans))
                            if execution_time == False:
                                task["execution_time"]=execution_time
                                task["student_code"] = code
                            else:
                                task["execution_time"]=execution_time
                                task["correct_answer"]=correct_ans
                                task["student_stdout"]=stdout
                                task["student_stderr"]=stderr
                                task["student_return_code"]=return_code
                                task["student_code"] = code
                                if auto_check:
                                    task["auto_check"]=auto_check
                                    task["grade"]=1
                                else:
                                    task["auto_check"]=auto_check
                                    task["grade"]=0

            print("good")
            return self.employee_list
        

    def run_student_code_all_c_work(self,data=None):
        if data != None:
            #запускает код студента и записывает полученные результаты и сам код в employee_list
            print("wait", data)
            count=0
            count_all=0
            for student_name,student_value in self.employee_list.items():
                if student_name != "task":
                    for task_name in student_value.values():
                        if task_name["task_path_name"] != None:
                            count_all+=1
            for student_name,student_value in self.employee_list.items():
                if student_name == "task":
                    task_list=student_value
                else:
                    for task_name,task in student_value.items():
                        if task['task_path_name'] != None:
                            current=[student_name,task_name,task['task_path_name']]
                            auto_check,stdout,stderr,return_code,execution_time,correct_ans,code=self.run_student_code_c_work(current,task_list)
                            print("Ученик {:<15}  Задача  {:<20}  Прогресс {:7.2f}".format(student_name,task_name,count/count_all*100))
                            count+=1
                            print( repr(stdout),repr(correct_ans))
                            if execution_time == False:
                                task["execution_time"]=execution_time
                                task["student_code"] = code
                            else:
                                task["execution_time"]=execution_time
                                task["correct_answer"]=correct_ans
                                task["student_stdout"]=stdout
                                task["student_stderr"]=stderr
                                task["student_return_code"]=return_code
                                task["student_code"] = code
                                if auto_check:
                                    task["auto_check"]=auto_check
                                    task["grade"]=1
                                else:
                                    task["auto_check"]=auto_check
                                    task["grade"]=0

            print("good")
            return self.employee_list
        else:
            #запускает код студента и записывает полученные результаты и сам код в employee_list
            print("wait")
            count=0
            count_all=0
            for student_name,student_value in self.employee_list.items():
                if student_name != "task":
                    for task_name in student_value.values():
                        if task_name["task_path_name"] != None:
                            count_all+=1
            for student_name,student_value in self.employee_list.items():
                if student_name == "task":
                    task_list=student_value
                else:
                    for task_name,task in student_value.items():
                        if task['task_path_name'] != None:
                            current=[student_name,task_name,self.employee_list[student_name][task_name]['task_path_name']]
                            auto_check,stdout,stderr,return_code,execution_time,correct_ans,code=self.run_student_code_c_work(current,task_list)
                            print("Ученик {:<15}  Задача  {:<20}  Прогресс {:7.2f}".format(student_name,task_name,count/count_all*100))
                            count+=1
                            print( repr(stdout),repr(correct_ans))
                            if execution_time == False:
                                task["execution_time"]=execution_time
                                task["student_code"] = code
                            else:
                                task["execution_time"]=execution_time
                                task["correct_answer"]=correct_ans
                                task["student_stdout"]=stdout
                                task["student_stderr"]=stderr
                                task["student_return_code"]=return_code
                                task["student_code"] = code
                                if auto_check:
                                    task["auto_check"]=auto_check
                                    task["grade"]=1
                                else:
                                    task["auto_check"]=auto_check
                                    task["grade"]=0

            print("good")
            return self.employee_list                        
                            #employee_list[student_name][task_name][""]

    def run_student_code(self,current:list,task_list:list):
        #запускает код студента и 
        if self.data==None:
            self.data=self.open_yaml(task_list)
        path_code_student=self.folder_path+'\\'+current[0]+'\\'+current[1]+'\\'+current[2]+'\\'+current[-1]
        task_description=self.data[current[3]]

        if self.copy_code_and_data(path_code_student,task_description):
            with open(self.tmp_folder+'\\'+current[-1],'r',encoding="utf-8") as tmp:
                code = tmp.read()
            stdout,stderr,return_code,execution_time = self.run_code(self.tmp_folder+'\\'+current[-1],2)
            if execution_time==False:
                return False,stdout,stderr,return_code,execution_time,self.data[current[3]]["answer"],code
            else:
                if self.data[current[3]]["answer"]+'\n'==stdout:
                    return True,stdout,stderr,return_code,execution_time,self.data[current[3]]["answer"],code
                else:
                    return False,stdout,stderr,return_code,execution_time,self.data[current[3]]["answer"],code
        else:
            print(path_code_student)
            print(self.copy_code_and_data(path_code_student,task_description))

    def run_student_code_c_work(self,current:list,task_list:list):
        #запускает код студента и 
        if self.data==None:
            self.data=self.open_yaml(task_list)
        path_code_student=self.folder_path+'\\'+current[0]+'\\'+current[-1]
        task_description=self.data[current[1]]

        if self.copy_code_and_data(path_code_student,task_description):
            print(self.tmp_folder)
            with open(self.tmp_folder+'\\'+current[-1],'r',encoding="utf-8") as tmp:
                code = tmp.read()
            stdout,stderr,return_code,execution_time = self.run_code(self.tmp_folder+'\\'+current[-1],2)
            if execution_time==False:
                return False,stdout,stderr,return_code,execution_time,self.data[current[1]]["answer"],code
            else:
                if self.data[current[1]]["answer"]+'\n'==stdout:
                    return True,stdout,stderr,return_code,execution_time,self.data[current[1]]["answer"],code
                else:
                    return False,stdout,stderr,return_code,execution_time,self.data[current[1]]["answer"],code
        else:
            print(path_code_student)
            print(self.copy_code_and_data(path_code_student,task_description))
            
    def run_code(self,path_code,timeout=2):
        #запускает код по пути path_code с ограничением по времени timeout
        #return stdout,stderr,return_code,time
        start_time = time.time()
        process=subprocess.Popen(["python", os.path.basename(path_code)],cwd = self.tmp_folder, text=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Запускаем функцию из function.py
        try:
            stdout,stderr=process.communicate(timeout=timeout)
            return_code=process.returncode
            end_time=time.time()
            execution_time=end_time-start_time
        except subprocess.TimeoutExpired:
            process.kill()
            stdout,stderr=process.communicate()
            return_code=process.returncode
            end_time=time.time()
            execution_time=False
        return stdout,stderr,return_code,execution_time

    def run_code_text(self,code,timeout=2):
        path_code = self.tmp_folder+'\\'+'tmp.py'
        with open(path_code,'w',encoding="utf-8") as file:
            file.write(code)

        start_time = time.time()
        process=subprocess.Popen(["python", os.path.basename(path_code)],cwd = self.tmp_folder, text=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Запускаем функцию из function.py
        try:
            stdout,stderr=process.communicate(timeout=timeout)
            return_code=process.returncode
            end_time=time.time()
            execution_time=end_time-start_time
        except subprocess.TimeoutExpired:
            process.kill()
            stdout,stderr=process.communicate()
            return_code=process.returncode
            end_time=time.time()
            execution_time=False
        return stdout,stderr,return_code,execution_time

    def safe_comment_grade(self):
        count_all=0
        #сохраняем каждому ученику верно или неверно решена задача (пока во временную папку)
        for student_name,student_value in self.employee_list.items():
            if student_name == "task":
                task_list=student_value
                count_all+=len(student_value)
            else:
                if os.path.exists(self.folder_path+'\\'+student_name+'\\'+self.month+'\\'+self.date+"\\result.txt"):
                    flag=True
                    with open(self.folder_path+'\\'+student_name+'\\'+self.month+'\\'+self.date+"\\result.txt","r",encoding="utf-8") as file:
                        e = file.readline().split()
                        
                        print(e) 
                        if e[0] == "\ufeff":
                            e=e[1:]
                            print(e)
                        if not(e[0] == "№"):
                            file.readline()
                            datetime_object = datetime.datetime.strptime(file.readline().replace("\n",'').split("   ")[1], "%Y-%m-%d %H:%M:%S")
                            print(datetime_object.date())
                            print(datetime_object.time())
                            file.readline()
                        i=0
                        count_done = 0
                        count_grade=0
                        text=student_name+"\n"
                        for task_name,task in student_value.items():
                                if task["done"] != None:
                                    count_grade +=float(task["grade"]) if task["grade"] != None else 0.0
                                    count_done+= 1 if task["done"] else 0
                                    tmp = [task_name]
                                    if task["task_path_name"] != None:
                                        tmp.append(task["task_path_name"])
                                    if task["done"] == True:
                                        tmp.append("+")
                                    else:
                                        tmp.append("-")
                                    if task["grade"] != None:
                                        tmp.append(str(float(task["grade"])))
                                    else:
                                        tmp.append("0.0")
                                    if task["teacher_comment"] != None:
                                        tmp.append(task["teacher_comment"])
                                    tmp_line = file.readline().replace("\n","").split()

                                    if tmp == tmp_line:
                                        print(True)
                                    else:
                                        flag=False
                                        print(tmp,tmp_line)
                                        text += " ".join(tmp)+"    "+" ".join(tmp_line)+'\n'
                                        #print(tmp,tmp_line)
                        if not flag:
                            print(text)
                                    #if file.readline.split() == tmp:
                                    #    print(True)
                            if tk.messagebox.askyesno("Перезаписать result.txt",text):
                                with open(self.folder_path+'\\'+student_name+'\\'+self.month+'\\'+self.date+"\\result.txt","w",encoding="utf-8") as file:
                                    file.write("Дз на "+self.date+'\n')
                                    file.write("Ученик "+student_name+'\n')
                                    file.write("Проверено   "+str(datetime.datetime.now().replace(microsecond=0))+'\n')
                                    count_done = 0
                                    count_grade=0
                                    l=[]
                                    for task_name,task in student_value.items():
                                        l.append(len(task["task_path_name"] if task["task_path_name"] != None else " "))
                                    len_file_name = int(max(l))
                                    if len_file_name <5: len_file_name=5
                                    file.write("{:^6} {:^{len_file_name}}   {:^5}   {:^4}   {:<10}\n".format(
                                        "№",
                                        "Файл",
                                        "Сдано",
                                        "Балл",
                                        "Комментарий учителя",
                                        len_file_name = len_file_name
                                        ))
                                    
                                    print("teacher com",task["teacher_comment"])
                                    for task_name,task in student_value.items():
                                        if task["done"] != None:
                                            count_grade +=task["grade"] if task["grade"] != None else 0
                                            count_done+= 1 if task["done"] else 0
                                            file.write("{:<6} {:^{len_file_name}}   {:^5}   {:4.1f}   {:<10}\n".format(
                                                task_name,
                                                task["task_path_name"] if task["task_path_name"] != None else "",
                                                "+" if task["done"]==True else "-",
                                                task["grade"] if task["grade"] != None else 0,
                                                task["teacher_comment"] if task["teacher_comment"] != None else "",
                                                len_file_name=len_file_name
                                            ))
                                    file.write("  {:^{l}}{:{ldc}d}/{:{lda}d}   {:3.1f}/{:3.1f}\n".format(
                                        "",
                                        count_done,
                                        count_all,
                                        count_grade,
                                        count_all,
                                        l=9+len_file_name,
                                        lda = len(str(count_all)),
                                        ldc = len(str(count_done))
                                        ))
                            else:
                                pass
        
        
                else:
                    with open(self.folder_path+'\\'+student_name+'\\'+self.month+'\\'+self.date+"\\result.txt","w",encoding="utf-8") as file:
                        file.write("Дз на "+self.date+ '\n')
                        file.write("Ученик "+student_name+'\n')
                        file.write( "Проверено   "+str(datetime.datetime.now().replace(microsecond=0))+'\n')
                        count_done = 0
                        count_grade=0
                        l=[]
                        for task_name,task in student_value.items():
                            l.append(len(task["task_path_name"] if task["task_path_name"] != None else " "))
                        len_file_name = int(max(l))
                        if len_file_name <5: len_file_name=5
                        file.write("{:^6} {:^{len_file_name}}   {:^5}   {:^4}   {:<10}\n".format(
                            "№",
                            "Файл",
                            "Сдано",
                            "Балл",
                            "Комментарий учителя",
                            len_file_name = len_file_name
                            ))

                        for task_name,task in student_value.items():
                            if task["done"] != None:
                                count_grade +=task["grade"] if task["grade"] != None else 0
                                count_done+= 1 if task["done"] else 0
                                file.write("{:<6} {:^{len_file_name}}   {:^5}   {:4.1f}   {:<10}\n".format(
                                    task_name,
                                    task["task_path_name"] if task["task_path_name"] != None else "",
                                    "+" if task["done"]==True else "-",
                                    task["grade"] if task["grade"] != None else 0,
                                    task["teacher_comment"] if task["teacher_comment"] != None else "",
                                    len_file_name=len_file_name
                                ))
                        file.write("  {:^{l}}{:{ldc}d}/{:{lda}d}   {:3.1f}/{:3.1f}\n".format(
                                "",
                                count_done,
                                count_all,
                                count_grade,
                                count_all,
                                l=9+len_file_name,
                                lda = len(str(count_all)),
                                ldc = len(str(count_done))
                                ))

        for student_name in os.listdir(self.folder_path):
            if student_name not in ["task and data","tmp"]:
                pass
                #print(os.listdir(self.folder_path +"\\"+student_name + "\\"+self.current[1]+"\\"+self.current[2]))


    def open_yaml(self,task_list):
        #открывает соотвествующие файлыы yaml для задний егэ и возвращает словарь с задачи которые переданы в task_list= ["17-1","18-2"]
        type_ege={}
        data={}
        for i in task_list:
            if int(i.split('-')[0]) not in type_ege.keys():
                type_ege[int(i.split("-")[0])]=[]
            type_ege[int(i.split("-")[0])].append(int(i.split("-")[1]))
        print(type_ege)
        for task_type in type_ege.keys(): 
            with open(self.folder_data+'\\'+str(task_type)+'.yaml','r',encoding='utf-8') as file:
                    yaml_data=yaml.safe_load(file)
            for task_number in type_ege[task_type]:
                value=yaml_data.get(task_type)[task_number-1]
                data[str(task_type)+'-'+str(task_number)] = value
            print(data.keys())
        return data

    def get_employee(self):
        print(self.employee_list["task"] if self.employee_list != None else "None")
        if self.employee_list == None:
            self.employee_list=self.create_list_task()
        return self.employee_list
        
    def get_yaml_data(self):
        if self.data == None:
            self.data=self.open_yaml(self.task_list)
        return self.data

    def set_employee(self,employee_list):
        self.employee_list=employee_list
        return True

    def create_list_task(self):
        # функция создает словарь с задачами учеников (без проверки решения) для передачи данных на отрисовку таблицы  '
        self.employee_list=None
        with open(os.getcwd()+'\\setting.yml','r',encoding='utf-8') as file:
            setting_data=yaml.safe_load(file)
        self.folder_data_base=os.getcwd()
        self.folder_path = setting_data["folder_path"]+'\\'+setting_data["class"]
        self.folder_data=setting_data["folder_data"]
        self.tmp_folder = setting_data["tmp_folder"]
        #folder_path = 'C:\\Users\\Dima\\YandexDisk\\Школа\\10БДЗ'
        self.list_stop_path_name=['task and data']
        # Получаем дерево путей
        self.path_tree = self.build_path_tree(self.folder_path)
        self.current=setting_data["current"]
        self.student_list=[i for i in self.path_tree.keys()]
        self.data=None
        self.month=setting_data["month"]
        self.date=setting_data["date"]
        self.class_name=setting_data["class"]
        if self.class_name in setting_data["task_list"]:
            if self.date in setting_data["task_list"][self.class_name].keys():
                self.task_list=setting_data["task_list"][self.class_name][self.date]
            else:
                self.task_list=['']
        else:
            setting_data
        student_task={'task':self.task_list}
        self.current[-1]=self.task_list[0]

        current=self.current
        tmp = current[0]
        tmp_list={}
        b,current,task=self.current_file(self.path_tree,current,self.task_list)
        while b:
            #if current[0] == 'Дикаева Дарья':
            #    break
            if task == None:
                tmp_list[current[-1]]={'task_path_name' : None,
                                                'done':False,
                                                'auto_check':None,
                                                'teacher_check':None,
                                                'teacher_comment':None,
                                                'grade':None,
                                                'task date':self.date,
                                                'check_date':None,
                                                'correct_amswer':None,
                                                'student_code':None,
                                                'student_stdout':None,
                                                'student_stderr':None,
                                                'student_return_code':None,
                                                'execution_time':None
                                                }
            else:
                with open(self.folder_path+'\\'+current[0]+'\\'+current[1]+'\\'+current[2]+'\\'+task,'r',encoding="utf-8") as file:
                    code=file.read()
                tmp_list[current[-1]]={'task_path_name':str(task),
                                                'done':True,
                                                'auto_check':None,
                                                'teacher_check':None,
                                                'teacher_comment':None,
                                                'grade':None,
                                                'task date':self.date,
                                                'check_date':None,
                                                'correct_amswer':None,
                                                'student_code':code,
                                                'student_stdout':None,
                                                'student_stderr':None,
                                                'student_return_code':None,
                                                'execution_time':None
                                                }
            b,current,task= self.next_file(self.path_tree,current,self.task_list)
            if current[0]!=tmp or not b:
                student_task[tmp]=tmp_list
                tmp=current[0]
                tmp_list={}
        return student_task


    def create_list_task_all(self,list_date):
        #self.employee_list=None
        with open(os.getcwd()+'\\setting.yml','r',encoding='utf-8') as file:
            setting_data=yaml.safe_load(file)
        self.folder_data_base=os.getcwd()
        self.folder_path = setting_data["folder_path"]+'\\'+setting_data["class"]
        self.folder_data=setting_data["folder_data"]
        self.tmp_folder = setting_data["tmp_folder"]
        #folder_path = 'C:\\Users\\Dima\\YandexDisk\\Школа\\10БДЗ'
        self.list_stop_path_name=['task and data']
        # Получаем дерево путей
        self.path_tree = self.build_path_tree(self.folder_path)

        self.current=setting_data["current"]
        self.student_list=[i for i in self.path_tree.keys()]
        self.data=None
        self.month=setting_data["month"]
        self.date=setting_data["date"]
        self.class_name=setting_data["class"]
        
        self.current[-1]=self.task_list[1]
        #надо создать список задач изначально по всем датам
        self.task_list=[]
        self.amount={}
        for cur_date in list_date:
            if self.class_name in setting_data["task_list"]:
                if self.date in setting_data["task_list"][self.class_name].keys():
                    l=0
                    for i in setting_data["task_list"][self.class_name][cur_date]:
                        self.task_list.append(i)
                        l+=1
                    self.amount[cur_date] = l
        student_task={'task':self.task_list}
        t=0
        for cur_date in list_date:
            self.current=setting_data["current"]
            self.date=cur_date
            self.current[0] = self.student_list[1]
            self.current[2] = cur_date
            self.current[-1] = self.task_list[t] 
            current=self.current
            tmp = current[0]
            tmp_list={}
            count=1
            count_t=1
            b,current,task=self.current_file(self.path_tree,current,self.task_list)
            while b:
                #if current[0] == 'Дикаева Дарья':
                #   break
                if task == None:
                    tmp_list[current[-1]]={'task_path_name' : None,
                                                    'done':False,
                                                    'auto_check':None,
                                                    'teacher_check':None,
                                                    'teacher_comment':None,
                                                    'grade':None,
                                                    'task date':cur_date,
                                                    'check_date':None,
                                                    'correct_amswer':None,
                                                    'student_code':None,
                                                    'student_stdout':None,
                                                    'student_stderr':None,
                                                    'student_return_code':None,
                                                    'execution_time':None
                                                    }
                else:
                    #with open(self.folder_path+'\\'+current[0]+'\\'+current[1]+'\\'+current[2]+'\\'+task,'r',encoding="utf-8") as file:
                    #    code=file.read()
                    code=''
                    tmp_list[current[-1]]={'task_path_name':str(task),
                                                'done':True,
                                                'auto_check':None,
                                                'teacher_check':None,
                                                'teacher_comment':None,
                                                'grade':None,
                                                'task date':cur_date,
                                                'check_date':None,
                                                'correct_amswer':None,
                                                'student_code':code,
                                                'student_stdout':None,
                                                'student_stderr':None,
                                                'student_return_code':None,
                                                'execution_time':None
                                                }
                
                b,current,task= self.next_file(self.path_tree,current,self.task_list)
                if count_t == self.amount[cur_date]:
                    '''if task == None:
                        tmp_list[current[-1]]={'task_path_name' : None,
                                                    'done':False,
                                                    'auto_check':None,
                                                    'teacher_check':None,
                                                    'teacher_comment':None,
                                                    'grade':None,
                                                    'task date':cur_date,
                                                    'check_date':None,
                                                    'correct_amswer':None,
                                                    'student_code':None,
                                                    'student_stdout':None,
                                                    'student_stderr':None,
                                                    'student_return_code':None,
                                                    'execution_time':None
                                                    }
                    else:
                        #with open(self.folder_path+'\\'+current[0]+'\\'+current[1]+'\\'+current[2]+'\\'+task,'r',encoding="utf-8") as file:
                        #    code=file.read()
                        code=''
                        tmp_list[current[-1]]={'task_path_name':str(task),
                                                'done':True,
                                                'auto_check':None,
                                                'teacher_check':None,
                                                'teacher_comment':None,
                                                'grade':None,
                                                'task date':cur_date,
                                                'check_date':None,
                                                'correct_amswer':None,
                                                'student_code':code,
                                                'student_stdout':None,
                                                'student_stderr':None,
                                                'student_return_code':None,
                                                'execution_time':None
                                                }'''
                    if current[0] == self.student_list[-1]:
                        if b:
                            try:
                                if current[-1] == self.task_list[t+self.amount[cur_date]]:
                                    b=False
                                    current[-1]=self.task_list[self.amount[cur_date]]
                                    current[0]=self.student_list[1]
                            except:
                                if current[-1] == self.task_list[-1]:
                                    b= False
                                else:
                                    current[-1] = self.task_list[t]
                        
                        else:
                            pass

                    else:
                        current[-1]=self.task_list[t]
                        current[0] = self.student_list[count+1]
                        b,current,task=self.current_file(self.path_tree,current,self.task_list)



                   
                    if tmp in student_task:
                        tmp_l={}
                        for i,val in student_task[tmp].items():
                            tmp_l[i] = val
                        for i,val in tmp_list.items():
                            tmp_l[i] = val
                        student_task[tmp] = tmp_l
                    else:
                        student_task[tmp]=tmp_list
                    tmp=current[0]
                    tmp_list={}
                    count +=1
                    count_t=1
                else:
                    count_t+=1
                
                
            t+=self.amount[cur_date]
        return student_task

    def open_result(self,date = None):
        #self.run_student_code_all()
        
        if date == None:
            self.amount={}
            date=[self.date]
            self.amount[self.date] = len(self.task_list)
        for cur_date in date:
            self.date=cur_date
            for student_name,student_value in self.employee_list.items():
                if os.path.exists(self.folder_path+'\\'+student_name+'\\'+self.month+'\\'+self.date+"\\result.txt"):
                    flag=True
                    with open(self.folder_path+'\\'+student_name+'\\'+self.month+'\\'+self.date+"\\result.txt","r",encoding="utf-8") as file:
                        e = file.readline().split()
                        print("open",e)
                        if e[0] == '\ufeff':
                            e=e[1:]
                            print(e)
                        print(self.folder_path+'\\'+student_name+'\\'+self.month+'\\'+self.date+"\\result.txt") 
                        if e[0] != "№":
                            print(file.readline())
                            datetime_object = datetime.datetime.strptime(file.readline().replace("\n",'').split("   ")[1], "%Y-%m-%d %H:%M:%S")
                            print(datetime_object.date())
                            print(datetime_object.time())
                            file.readline()
                        i=0
                        count=0
                        sm=0
                        sl=0
                        for k,v in self.amount.items():
                            sm+=int(v)
                            if k == cur_date:
                                sl=sm-v
                                break
                        for task_name,task in student_value.items():
                            if count >= sm:
                                break
                            else:
                                count+=1
                            if count >sl:
                                tmp_line = file.readline().split("   ")
                                if len(tmp_line[0].split()) >1:
                                    task["task_path_name"] = " ".join(tmp_line[0].split()[1:])
                                    t = [tmp_line[0].split()[0]," ".join(tmp_line[0].split()[1:])]
                                else:
                                    if tmp_line[1] !='':
                                        if task["task_path_name"]==None:
                                            task["task_path_name"] = tmp_line[1].split()[0]
                                            t = [tmp_line[0].split()[0],tmp_line[1].split()[0]]
                                        else:
                                            t = [tmp_line[0].split()[0],task["task_path_name"]]
                                            print(task['task_path_name'])
                                    else:
                                        if task['task_path_name'] == None:
                                            task["task_path_name"] = None
                                        t = [tmp_line[0].split()[0],'']
                                i=1
                                
                                while True:
                                    if tmp_line[i].replace(" ", "") == "+" or tmp_line[i].replace(" ", "") == "-":
                                        if tmp_line[i].replace(" ","") == "+":
                                            task["done"] =True
                                        else:
                                            if task["done"] !=True:
                                                task["done"] = False
                                        t.append(tmp_line[i].replace(" ", ""))
                                    try:
                                        t.append(float(tmp_line[i].replace(" ","")))

                                        if t[-2] == '+':
                                            task["grade"] = float(tmp_line[i].replace(" ",""))
                                        task["auto_check"] = True
                                        s=''
                                        for j in tmp_line[i+1:]:
                                            if j != '':
                                                s+=j
                                        task["teacher_comment"] = s.replace("\n","")
                                        t.append(s)
                                        break
                                    except ValueError:
                                        pass
                                
                                    i+=1  
        if len(date) ==1:
            self.app.update(self.employee_list)
                                    

    def open_result_all(self,date):
        #date=['2024.02.12','2024.02.13']
        self.employee_list = self.create_list_task_all(date)

        self.open_result(date)
        self.app.update(self.employee_list,date)

    def open_result_all_run(self,date):
        self.employee_list = self.create_list_task_all(date)
        self.run_student_code_all(date)
        self.open_result(date)
        self.app.update(self.employee_list,date)     


    def create_list_task_control_work(self): 
        self.employee_list=None
        with open(os.getcwd()+'\\setting.yml','r',encoding='utf-8') as file:
            setting_data=yaml.safe_load(file)
        self.folder_data_base=os.getcwd()
        self.folder_path = setting_data["folder_path"]+'\\'+"cw"
        self.folder_data=setting_data["folder_data"]
        self.tmp_folder = setting_data["tmp_folder"]
        #folder_path = 'C:\\Users\\Dima\\YandexDisk\\Школа\\10БДЗ'
        self.list_stop_path_name=['task and data']
        # Получаем дерево путей
        self.path_tree = self.build_path_tree(self.folder_path)
        self.current=['','']
        self.student_list=[i for i in self.path_tree.keys()]
        self.data=None
        self.class_name="cw"
        if self.class_name in setting_data["task_list"]:
            self.task_list=setting_data["task_list"][self.class_name]
        print(self.task_list)
        student_task={'task':self.task_list}
        self.current[-1]= self.task_list[0]
        self.current[0] = self.student_list[0]

        current=self.current
        tmp = current[0]
        tmp_list={}
        b,current,task=self.current_file_c_work(self.path_tree,current,self.task_list)
        while b:
            #if current[0] == 'Дикаева Дарья':
            #    break
            if task == None:
                tmp_list[current[-1]]={'task_path_name' : None,
                                                'done':False,
                                                'auto_check':None,
                                                'teacher_check':None,
                                                'teacher_comment':None,
                                                'grade':None,
                                                'task date':self.date,
                                                'check_date':None,
                                                'correct_amswer':None,
                                                'student_code':None,
                                                'student_stdout':None,
                                                'student_stderr':None,
                                                'student_return_code':None,
                                                'execution_time':None
                                                }
            else:
                with open(self.folder_path+'\\'+current[0]+'\\'+task,'r',encoding="utf-8") as file:
                    code=file.read()
                tmp_list[current[-1]]={'task_path_name':str(task),
                                                'done':True,
                                                'auto_check':None,
                                                'teacher_check':None,
                                                'teacher_comment':None,
                                                'grade':None,
                                                'task date':self.date,
                                                'check_date':None,
                                                'correct_amswer':None,
                                                'student_code':code,
                                                'student_stdout':None,
                                                'student_stderr':None,
                                                'student_return_code':None,
                                                'execution_time':None
                                                }
            print(b,current,task)
            b,current,task= self.next_file_c_work(self.path_tree,current,self.task_list)
            if current[0]!=tmp or not b:
                student_task[tmp]=tmp_list
                tmp=current[0]
                tmp_list={}
        return student_task
    
    def open_c_work(self):
        self.employee_list=self.create_list_task_control_work()
        self.run_student_code_all_c_work()
        self.app.update(self.employee_list,'2024.02.27')

    # Указываем путь к папке
    #folder_path = 'D:\\База\\YandexDisk\\Школа\\10БДЗ'
    #folder_path = 'C:\\Users\\Dima\\YandexDisk\\Школа\\10БДЗ'
   