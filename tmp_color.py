from tkinter import *
import os
import yaml
from tkinter import ttk, filedialog
from functools import partial
from tmp_path import Task
from application_table import Table
from codeview import ViewCode
# Table class

class Application(Tk):
    def __init__(self):
        super().__init__()
        

        self.title("Мое приложение")
        self.t = Task(self)
     
        with open(os.getcwd()+'\\setting.yml','r',encoding='utf-8') as file:
            setting_data=yaml.safe_load(file)
        self.folder_path=setting_data["folder_path"]
        self.date = setting_data["date"]
        self.month= setting_data["month"]
        self.class_name = setting_data["class"]

        self.create_widgets()

    def open_directory_dialog(self):
        self.filename = filedialog.askdirectory()
        if self.filename:
            self.entry_student_folder.delete(0, END)  # Очищаем поле ввода
            self.entry_student_folder.insert(0, self.filename)  # Вставляем выбранный путь в поле ввода
            elements=os.listdir(self.filename)
            self.class_number_combobox['values']=elements
      
    def on_class_number_combobox_change(self,event):
        elements = os.listdir(self.folder_path+'\\'+self.class_number_combobox.get())
        for i in elements:
            if i != "task and data" and i != "tmp":
                elements=os.listdir(self.folder_path+'\\'+self.class_number_combobox.get()+'\\'+i)
                self.tmp_student=i
                break
        self.month_number_combobox['values'] = elements

    def on_month_number_combobox_change(self,event):
        elements=os.listdir(self.folder_path+'\\'+self.class_number_combobox.get()+'\\'+self.tmp_student+'\\'+self.month_number_combobox.get())
        self.date_combobox["value"]=elements

    def on_date_combobox_change(self,event):
        self.date = self.date_combobox.get()
 
    def create_combobox(self):
        if self.folder_path != None:
            self.entry_student_folder.insert(0, self.folder_path)  # Вставляем выбранный путь в поле ввода
            elements=os.listdir(self.folder_path)
            self.class_number_combobox['values']=elements
            if self.class_name != None:
                self.on_class_number_combobox_change(None)
                if self.month != None:
                    self.on_month_number_combobox_change(None)

    def print_student_comment(self):
        self.t.safe_comment_grade()

    def submit(self):
        
        class_number = self.class_number_combobox.get()
        month_number =  self.month_number_combobox.get()
        date = self.date_combobox.get()
        print("Номер класса:", class_number)
        print("Номер месяца:", month_number)
        print("Дата:", date)
        with open(os.getcwd()+'\\setting.yml','r',encoding='utf-8') as file:
            setting_data=yaml.safe_load(file)
        setting_data["class"] = class_number
        setting_data["month"] = self.month_number_combobox.get()
        setting_data["date"] = self.date_combobox.get()
        setting_data["folder_path"] = str(self.folder_path)
        if class_number not in setting_data["task_list"]:
            setting_data["task_list"][class_number] = {}
            setting_data["task_list"][class_number][self.date_combobox.get()] = ['']
        try:
            setting_data["current"] = [setting_data["current"][0],setting_data["month"],setting_data["date"],setting_data["task_list"][self.class_name][self.date][0]]
        except:
            setting_data["current"] = [setting_data["current"][0],setting_data["month"],setting_data["date"],setting_data["task_list"]]
        with open(os.getcwd()+'\\setting.yml','w',encoding='utf-8') as file:
            yaml.dump(setting_data,file,allow_unicode=True)
        self.employee_list = self.t.create_list_task()
        print(self.employee_list["task"])
        self.student_task_text.delete(1.0,END)
        self.student_task_text.insert(END,self.employee_list["task"])
        self.table.update_table_list(self.employee_list)
        self.table.update_table(self.employee_list)
    
    def update_student(self):
        self.employee_list=self.t.get_employee()
        self.student_task_text.delete(1.0,END)
        self.student_task_text.insert(END,self.employee_list["task"])
        #student = Task(self).run_student_code_all()
        #self.student_name_label_progress.config(text="Ученик :" + student)

    def safe_srudent_response(self):
        self.t.safe_comment_grade()

    def update(self,emp,date_list=None) -> None:
        self.employee_list = emp
        print("list task",self.employee_list["task"])
        self.table.update_table(self.employee_list,date_list)

    def load_task(self):
        #print(list(self.employee_list.items())[1][1][self.employee_list["task"][2-1]]["teacher_comment"])
        task_list=self.student_task_text.get(1.0,END).split()
        print(task_list)
        class_number = self.class_number_combobox.get()
        date = self.date_combobox.get()
        print("Номер класса:", class_number)
        print("Дата:", date)
        with open(os.getcwd()+'\\setting.yml','r',encoding='utf-8') as file:
            setting_data=yaml.safe_load(file)
        setting_data["class"] = class_number
        setting_data["task_list"][class_number][date]=task_list
        with open(os.getcwd()+'\\setting.yml','w',encoding='utf-8') as file:
            yaml.dump(setting_data,file,allow_unicode=True)

        self.employee_list = self.t.create_list_task()
        self.student_task_text.delete(1.0,END)
        self.student_task_text.insert(END,self.employee_list["task"])
        self.table.update_table_list(self.employee_list)
        self.table.update_table(self.employee_list)

    def check_task(self):
        self.employee_list=self.t.run_student_code_all()
        self.table.update_table(self.employee_list)

    def run_code(self):
        code = self.frame.program_text.get(1.0,END)
        stdout,stderr,return_code,execution_time = self.t.run_code_text(code)
        print(stdout,stderr,return_code,execution_time)

    def open_result_all(self):
        date = self.open_date_response_text.get(1.0,END).split()
        print(date)
        self.t.open_result_all(date)

    def open_result_all_run(self):
        date = self.open_date_response_text.get(1.0,END).split()
        print(date)
        self.t.open_result_all_run(date)

    def create_widgets(self):
        #folder_path = 'D:\\База\\YandexDisk\\Школа\\10БДЗ'
        #folder_path = 'C:\Users\Dima\YandexDisk\Школа\10БДЗ'
        # Получаем дерево путей
        self.t=Task(self)
        self.employee_list=self.t.create_list_task()

        frame_top = Frame()
        frame_top.pack(expand=True,side=LEFT)
        self.frame = ViewCode(frame_top,self.t,self)
        # Создаем фрейм для таблицы
        table_frame = LabelFrame(text="Верх")
        font_size=("Arial",12)
        frame_data=Frame()
        class_number_label = Label(frame_data, text="Базовая папка:",font=font_size)
        class_number_label.grid(row=0, column=0, padx=5, pady=5)

        self.entry_student_folder=Entry(frame_data,font=font_size)

        self.entry_student_folder.insert(END,self.folder_path)
        self.entry_student_folder.grid(row=0,column=1,columnspan=5,padx=0,pady=0,sticky=W + E)

        self.button = Button(frame_data, text="Обзор", command=self.open_directory_dialog,font=font_size)
        self.button.grid(row=0,column=6,padx=5, pady=10)

        class_number_label = Label(frame_data, text="Номер класса:",font=font_size)
        class_number_label.grid(row=1, column=0, padx=5, pady=5)
        self.class_number_combobox = ttk.Combobox(frame_data,font=font_size,width=7)
        self.class_number_combobox.set(self.class_name)
        self.class_number_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.class_number_combobox.bind("<<ComboboxSelected>>",self.on_class_number_combobox_change)

        month_number_label = ttk.Label(frame_data, text="Номер месяца:",font=font_size)
        month_number_label.grid(row=1, column=2, padx=5, pady=5)
        self.month_number_combobox = ttk.Combobox(frame_data,font=font_size,width=10)
        self.month_number_combobox.set(self.month)
        self.month_number_combobox.grid(row=1, column=3, padx=5, pady=5)
        self.month_number_combobox.bind("<<ComboboxSelected>>",self.on_month_number_combobox_change)

        # Создание выпадающего списка для даты
        date_label = Label(frame_data, text="Дата:",font=font_size)
        date_label.grid(row=1, column=4, padx=5, pady=5)
        self.date_combobox = ttk.Combobox(frame_data,font=font_size,width=10)
        self.date_combobox.set(self.date)
        self.date_combobox.grid(row=1, column=5, padx=5, pady=5)
        self.date_combobox.bind("<<ComboboxSelected>>",self.on_date_combobox_change)

        
        self.submit_button = Button(frame_data, text="Загрузить", command=self.submit,font=font_size)
        self.submit_button.grid(row=1, column=6, padx=5, pady=5)


        self.student_task_label = Label(frame_data,text="Задачи:",font=font_size)
        self.student_task_label.grid(row=2,column=0)

        self.student_task_text = Text(frame_data,height=1,width=60,font=font_size)
        print(self.employee_list["task"])
        self.student_task_text.insert(END,self.employee_list["task"])
        self.student_task_text.grid(row=2,column=1,columnspan=5,sticky="w")

        self.student_task_entry = Button(frame_data, text="Загрузить", command=self.load_task,font=font_size)
        self.student_task_entry.grid(row=2, column=6, padx=5, pady=5)

        self.student_name_label_progress = Label(frame_data,text="Ученик :",font=font_size)
        self.student_name_label_progress.grid(row=3, column=0,columnspan=2, padx=5, pady=5,sticky="w")
        

        self.task_name_label_progress = Label(frame_data,text="Задача :",font=font_size)
        self.task_name_label_progress.grid(row=3, column=2, padx=5, pady=5)

        self.submit_button = Button(frame_data, text="Проверить", command=self.check_task,font=font_size)
        self.submit_button.grid(row=3, column=4, padx=5, pady=5)

        self.execution_time_limit=Text(frame_data,height=1,width=8,font=font_size)
        self.execution_time_limit.insert(END,2)
        self.execution_time_limit.grid(row=3, column=5, padx=5, pady=5) 

        self.submit_button = Button(frame_data, text="Применить",font=font_size)
        self.submit_button.grid(row=3, column=6, padx=5, pady=5)        
        
        self.run_code = Button(frame_data, text="Run",font=font_size,command=self.run_code)
        self.run_code.grid(row=4, column=6, padx=5, pady=5)  
        
        self.safe_response = Button(frame_data, text="SR",font=font_size,command=self.safe_srudent_response)
        self.safe_response.grid(row=4, column=5, padx=5, pady=5)  

        self.safe_open_response = Button(frame_data, text="OR",font=font_size,command=self.t.open_result)
        self.safe_open_response.grid(row=4, column=4, padx=5, pady=5) 

        self.open_date_response_text = Text(frame_data,height=1,width=60,font=font_size)
        self.open_date_response_text.grid(row=4,column=0,columnspan=3,padx=5,pady=5)


        self.safe_open_response = Button(frame_data, text="OR all",font=font_size,command=self.open_result_all)
        self.safe_open_response.grid(row=4, column=3, padx=5, pady=5) 

        self.safe_open_response = Button(frame_data, text="OR all run",font=font_size,command=self.open_result_all_run)
        self.safe_open_response.grid(row=5, column=3, padx=5, pady=5) 

        self.safe_open_response = Button(frame_data, text="CW",font=font_size,command=self.t.open_c_work)
        self.safe_open_response.grid(row=5, column=4, padx=5, pady=5) 

        self.create_combobox()

        frame_data.pack(expand=True,fill=BOTH)
        table_frame.pack(expand=True,side=LEFT,fill=BOTH)

        # Создаем таблицу
        self.table = Table(table_frame,self.employee_list,self.frame,self,self.t)
        self.table.pack(expand=True,side=RIGHT)


if __name__== "__main__":
    app=Application()
    app.mainloop()
