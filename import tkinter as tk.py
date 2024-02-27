import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import os
import subprocess
from glob import glob
from datetime import datetime

class CodeRunnerApp:
    def __init__(self, master):
        self.master = master
        master.title("Code Runner")

        self.files_list = []
        self.current_file_index = 0
        self.base_folder_path = None
        self.current_student_index = 0
        self.students = []

        self.create_widgets()
        self.load_code_from_file()

    def create_widgets(self):
        # Верхнее поле для ввода кода
        self.code_text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=50, height=10)
        self.code_text_area.pack(expand=True, fill='both')

        # Поле для ввода входных данных
        self.input_text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=50, height=5)
        self.input_text_area.pack(expand=True, fill='both')
        self.input_text_area.insert(tk.END, "Enter input data here...")

        # Нижнее поле для вывода результатов
        self.result_text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=50, height=10)
        self.result_text_area.pack(expand=True, fill='both')

        # Кнопки
        self.run_button = tk.Button(self.master, text="Run Code", command=self.run_code)
        self.run_button.pack()

        self.load_button = tk.Button(self.master, text="Load Code from File", command=self.load_code_from_file)
        self.load_button.pack()

        self.next_task_button = tk.Button(self.master, text="Next Task", command=self.next_task)
        self.next_task_button.pack()

    def load_code_from_file(self):
        self.base_folder_path = self.ask_folder_path()
        if self.base_folder_path:
            self.students = [name for name in os.listdir(self.base_folder_path) if os.path.isdir(os.path.join(self.base_folder_path, name))]
            self.load_next_student()

    def ask_folder_path(self):
        folder_path = filedialog.askdirectory(title="Select a folder")
        return folder_path

    def load_next_student(self):
        if self.students and 0 <= self.current_student_index < len(self.students):
            current_student_name = self.students[self.current_student_index]
            current_student_folder = os.path.join(self.base_folder_path, current_student_name)

            self.files_list = glob(os.path.join(current_student_folder, '*.py'))
            self.current_file_index = 0
            self.load_current_file()

    def load_current_file(self):
        if self.files_list and 0 <= self.current_file_index < len(self.files_list):
            file_path = self.files_list[self.current_file_index]
            with open(file_path, 'r', encoding='utf-8') as file:
                code_content = file.read()
                self.code_text_area.delete("1.0", tk.END)
                self.code_text_area.insert(tk.END, code_content)

    def next_task(self):
        self.current_file_index += 1
        if self.current_file_index >= len(self.files_list):
            self.current_student_index += 1
            self.load_next_student()
        else:
            self.load_current_file()

    def run_code(self):
        code = self.code_text_area.get("1.0", tk.END)
        input_data = self.input_text_area.get("1.0", tk.END)

        try:
            current_student_name = self.students[self.current_student_index]
            print(self.)
            current_student_folder = os.path.join(self.base_folder_path, current_student_name)
            current_month_folder = os.path.join(current_student_folder, "01_Январь")  # замените "01_Январь" на текущий месяц
            current_date_folder = os.path.join(current_month_folder, datetime.now().strftime("%Y.%m.%d"))

            os.chdir(current_date_folder)

            result = subprocess.run(['python', '-c', code], input=input_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.returncode != 0:
                raise subprocess.CalledProcessError(returncode=result.returncode, cmd=['python', '-c', code], output=result.stderr)

            self.result_text_area.delete("1.0", tk.END)
            self.result_text_area.insert(tk.END, f"Code executed successfully!\n\nOutput:\n\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            self.result_text_area.delete("1.0", tk.END)
            self.result_text_area.insert(tk.END, f"Error while executing code:\n\n{e.output}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeRunnerApp(root)
    root.mainloop()
