from tkinter import *
import os
import yaml
from tkinter import ttk, filedialog
from tmp_path import Task
import tkinter as tk
from tkhtmlview import HTMLScrolledText
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from pygments import highlight
import pygments.lexers as pl
import pygments.formatters as pf
from pygments.formatters import Terminal256Formatter
import tkhtmlview as th

class ViewCode(Frame):
    def __init__(self,parent,task,app):
        self.app = app
        self.t=task
        super().__init__(parent)
        self.create_widget()
        self.data = None
        self.row = None
        self.column = None

    def create_widget(self):   
        frame_top=self
        font_size_label=('Arial',14)
        font_size_text= ('Arial',12)

        self.problem_text_label = Label(frame_top,text="Задача :",font=font_size_label)
        self.problem_text_label.grid(row=0,column=0,columnspan=2,padx=10,sticky="w")

        self.problem_text=Text(frame_top,width=80, height=5,font=font_size_text)
        self.problem_text.grid(row=1,column=0)

        self.problem__answer_text_label = Label(frame_top,text="Ответ: ",font=('Arial',14))
        self.problem__answer_text_label.grid(row=2,column=0,columnspan=2,padx=10,sticky="w")

        self.problem__answer_text=Text(frame_top,width=80, height=1,font=font_size_text)
        self.problem__answer_text.grid(row=3,column=0)


        self.program_problem_text_label = Label(frame_top,text="Решение ученика:",font=font_size_label)
        self.program_problem_text_label.grid(row=4,column=0,columnspan=2,padx=10,sticky="w")

        self.program_text = HTMLScrolledText(frame_top,width = 80, height =15,font=font_size_text)
        self.program_text.grid(row=5, column=0, padx=5, pady=5, sticky="we")

        self.program_text.configure(bg="#1d2331")
        self.program_text.configure(insertbackground="white")
        self.program_text.bind("<KeyRelease>",lambda event:self.change(self.program_text))
        #print(1)
        #print(repr( self.program_text.get(1.0,tk.END)))
        #print(2)
        #highlighted_code = self.highlight_python_code(python_code)
        #self.program_text.set_html(highlighted_code,strip=False)


        #self.program_text = Text(frame_top, width=80, height=15,font=font_size_text)
        #self.program_text.grid(row=5, column=0, padx=5, pady=5, sticky="we")

        #self.program_scroll = Scrollbar(frame_top, orient="vertical")
        #self.program_scroll.grid(row=5, column=1, sticky="ns")
        #self.program_text.config(yscrollcommand=self.program_scroll.set)

        #self.program_scroll = Scrollbar(frame_top,orient="horizontal")
        #self.program_scroll.grid(row=6,column=0,columnspan=2,sticky="we")
        #self.program_text.config(xscrollcommand=self.program_scroll.set)
        
        self.program_text_stdout_label = Label(frame_top,text="Вывод программы:",font=font_size_label)
        self.program_text_stdout_label.grid(row=7,column=0,columnspan=2,padx=10,sticky="w")

        self.program_stdout = Text(frame_top,width=80,height=3,font=font_size_text)
        self.program_stdout.grid(row=8,column=0,padx=5,pady=5,sticky="we")

        self.program_text_stderr = Label(frame_top,text="Ошибки:",font=font_size_label)
        self.program_text_stderr.grid(row=9,column=0,columnspan=2,padx=10,sticky="w")

        self.program_stderr = Text(frame_top,width=80,height=3,font=font_size_text)
        self.program_stderr.grid(row=10,column=0,padx=5,pady=5,sticky="we")

        self.progeram_text_return_code=Label(frame_top,text="Код возврата:",font=font_size_label)
        self.progeram_text_return_code.grid(row=11,column=0,columnspan=2,padx=10,sticky="w")

        self.program_return_code = Text(frame_top,width=80,height=1,font=font_size_text)
        self.program_return_code.grid(row=12,column=0,padx=5,pady=5,sticky="we")

        self.program_text_teacher_comment=Label(frame_top,text="Комментарий учителя:",font=font_size_label)
        self.program_text_teacher_comment.grid(row=13,column=0,columnspan=2,padx=10,sticky="w")

        self.program_teacher_comment_entry = Entry(frame_top, width=80,font=font_size_text)
        self.program_teacher_comment_entry.grid(row=14,column=0,padx=5,pady=5,sticky="we")
        #self.program_teacher_comment_entry.bind('<Enter>', self.set_teacher_comment)

        #self.program_teacher_comment = Text(frame_top,width=80,height=5,font=font_size_text)
        #self.program_teacher_comment.grid(row=14,column=0,padx=5,pady=5,sticky="we")

        frame_top.pack(side=LEFT)

    def update(self,employee_list):
        self.data = None
        self.employee_list=employee_list

    def safe_teacher_comment(self):
        teacher_comment = self.program_teacher_comment_entry.get()
        list(self.employee_list.items())[self.row][1][self.employee_list["task"][self.column-1]]["teacher_comment"] = self.program_teacher_comment_entry.get()
        self.t.set_employee(self.employee_list)
        print(self.program_teacher_comment_entry.get())

    def highlight_python_code(self,python_code):
        # Определяем лексер для Python
        lexer = pl.PythonLexer()
        # Получаем выделенный код
        highlighted_code = highlight(python_code, lexer, pf.HtmlFormatter(style="lightbulb",noclasses=True))
        return highlighted_code

    def change(self,html_label):
        cursor = html_label.index(tk.INSERT)
        # Получаем стиль текста вокруг курсора
        code = html_label.get("1.0","end-1c")
        h_code = self.highlight_python_code(code)
        html_label.set_html(h_code,strip = False)
        html_label.mark_set(tk.INSERT,cursor)
        style_tags = html_label.tag_names(cursor)

    def update_code_student(self,row,column):
        self.app.update_student()
        
        #print(self.row,self.column)
        print(row,column)
        if self.row != None and self.column!= None:
            if self.column>0 and self.column< len(self.employee_list["task"])+1:
                employee_list = self.t.get_employee()
                list(self.employee_list.items())[self.row][1][self.employee_list["task"][self.column-1]]["teacher_comment"] = self.program_teacher_comment_entry.get()
                self.t.set_employee(employee_list)
                self.program_teacher_comment_entry.delete(0,END)
        self.employee_list=self.t.get_employee()
        self.program_text.delete(1.0,END)
        self.row=row
        self.column=column
        if self.column <1 and self.column > len(self.employee_list["task"]):
            return
        self.problem_text_label.config(text="Задача :  "+ self.employee_list["task"][column-1])

        code = list(self.employee_list.items())[row][1][self.employee_list["task"][column-1]]
        highlighted_code = self.highlight_python_code(code["student_code"] if code["student_code"] != None else '')
        self.program_text.set_html(highlighted_code,strip=False)
        self.max_len_student_name = 0
        for i in self.employee_list.keys():
            if len(i) > self.max_len_student_name:
                self.max_len_student_name=len(i)
        self.student_name = list(self.employee_list.keys())[row]

        if self.data == None:
            self.data = self.t.get_yaml_data()
        execution_time=code["execution_time"]
        if execution_time == None:
            execution_time=''
        elif execution_time == False:
            execution_time="TL"
        else:
            execution_time=str(round(execution_time,5))
        self.program_problem_text_label.config(text ="Решение  {:{l}} : {:8}".format(self.student_name,code["task_path_name"],l=self.max_len_student_name))

        self.program_text_stdout_label.config(text="Вывод программы:"+" "*30+"Время :"+execution_time)

        problem_answer = list(self.data.items())[column-1][1]["answer"]
        self.problem__answer_text.delete(1.0,END)
        self.problem__answer_text.insert(END,problem_answer)

        problem = list(self.data.items())[column-1][1]["task description"]
        self.problem_text.delete(1.0,END)
        self.problem_text.insert(END,problem)

        stdout = list(self.employee_list.items())[row][1][self.employee_list["task"][column-1]]["student_stdout"] 
        self.program_stdout.delete(1.0,END)
        self.program_stdout.insert(END, stdout if stdout != None else '')

        stderr = list(self.employee_list.items())[row][1][self.employee_list["task"][column-1]]["student_stderr"] 
        self.program_stderr.delete(1.0,END)
        self.program_stderr.insert(END, stderr if stderr != None else '')

        return_code=list(self.employee_list.items())[row][1][self.employee_list["task"][column-1]]["student_return_code"] 
        self.program_return_code.delete(1.0,END)
        self.program_return_code.insert(END, return_code if return_code != None else '')

        teacher_comment = list(self.employee_list.items())[row][1][self.employee_list["task"][column-1]]["teacher_comment"] 
        self.program_teacher_comment_entry.delete(0,END)
        self.program_teacher_comment_entry.insert(0,teacher_comment if teacher_comment != None else "")



        # Создаем фрейм для таблицы
        
    def set_teacher_comment(self):
        if self.row != None:
            print(1)
            employee_list = self.t.get_employee()
            list(employee_list.items())[self.row][1][self.employee_list["task"][self.column-1]]["teacher_comment"] = self.program_teacher_comment_entry.get()
            self.t.set_employee(employee_list)
            print(self.program_teacher_comment_entry.get())

