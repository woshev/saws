from tkinter import *
import tkinter as tk
from codeview import ViewCode
import os
import yaml


class Table(Frame):  # Изменено: Table теперь наследуется от Frame
    def __init__(self, parent, employee_list, code_frame, app, t):
        self.app = app
        self.t = t
        self.Frame = parent
        self.code_frame = code_frame
        super().__init__(parent)

        self.selected_row = None
        self.selected_column = None
        self.table_relief_highlight = "solid"
        self.table_relief_baze = "ridge"
        self.table_borderwidth = 1
        self.table_highlightbackground = "red"
        self.employee_list = employee_list

        self.table_student_grade_criteria = [50, 60, 70, 85]

        self.add_columns_name = ["Балл", "ПВ", "ПВР", "О"]
        self.add_columns = len(self.add_columns_name) + 1

        self.total_rows = len(self.employee_list)
        self.total_columns = len(self.employee_list["task"]) + self.add_columns

        # цвета для выделения ячеек
        self.table_highlight_color = "#00FFFF"

        self.table_cell_color_header = "#4682B4"
        self.table_cell_color_green = "#3CB371"
        self.table_cell_color_yellow = "#FFFF00"
        self.table_cell_color_red = "#FF0000"
        self.table_cell_color_white = "#FFFFFF"
        self.table_cell_color_cian = "#00EEEE"
        with open(os.getcwd() + "\\setting.yml", "r", encoding="utf-8") as file:
            setting_data = yaml.safe_load(file)
        self.date_list = [setting_data["date"]]
        self.create_table()

    # Initialize a constructor
    def show_menu(self, event, row, column):
        # добавить выполне не выполнено
        # добавить получение даты сдачи задачи
        menu = Menu(self.Frame, tearoff=0)
        menu.add_command(
            label="None", command=lambda: self.set_entry_value(None)
        )
        # Получаем путь из виджета Entry, если пусто, то используем текущий рабочий каталог
        path = self.t.folder_path_student_get(row - self.row_add, column)
        files = os.listdir(path)
        for file in files:
            menu.add_command(
                label=file,
                command=lambda f=file: self.set_selected_file(
                    path, f, row - self.row_add, column
                ),
            )

        menu.post(event.x_root, event.y_root)

    def set_entry_value(self, value):
        # добавить передачу файла в employee_list
        print("None")

    def set_selected_file(self, path, file, row, column):
        selected_file = os.path.join(path, file)
        self.employee_list = self.t.get_employee()
        t
        list(self.employee_list.items())[row][1][
            self.employee_list["task"][column - 1]
        ]["task_path_name"] = file
        self.t.set_employee(self.employee_list)
        print("Выбранный файл:", selected_file)

    def create_table(self):
        self.employee_list = self.t.get_employee()
        self.total_rows = len(self.employee_list)
        self.total_columns = len(self.employee_list["task"]) + self.add_columns
        a = [value[0] for value in self.employee_list.items()]
        max_len_column_0 = self.maxlen(a) + 1
        count_cell = 0
        cell_width = 3
        self.row_add = 2
        last = None
        last_col = 1
        # список дат
        for task_name, task_value in self.employee_list[
            list(self.employee_list.keys())[1]
        ].items():
            if last == None:
                last = task_value["task date"]
                last_col = (
                    list(
                        self.employee_list[
                            list(self.employee_list.keys())[1]
                        ].keys()
                    ).index(task_name)
                    + 1
                )
            elif last != task_value["task date"] and len(
                self.employee_list[list(self.employee_list.keys())[1]].keys()
            ) - 1 > list(
                self.employee_list[list(self.employee_list.keys())[1]].keys()
            ).index(
                task_name
            ):
                col_span = (
                    list(
                        self.employee_list[
                            list(self.employee_list.keys())[1]
                        ].keys()
                    ).index(task_name)
                    - last_col
                    + 1
                )
                self.entry = Entry(
                    self,
                    justify="center",
                    width=cell_width * col_span,
                    bg=self.table_cell_color(
                        count_cell // self.total_columns,
                        count_cell % self.total_columns,
                    ),
                    fg="Black",
                    font=("Arial", 16, "bold"),
                    borderwidth=self.table_borderwidth,
                    relief=self.table_relief_baze,
                    highlightbackground=self.table_highlightbackground,
                )
                self.entry.insert(END, last)
                # print(total_columns,total_rows,count_cell,count_cell//total_rows, count_cell%total_columns)
                self.entry.grid(
                    row=0, column=last_col, columnspan=col_span, sticky="nsew"
                )
                last = task_value["task date"]
                last_col = (
                    list(
                        self.employee_list[
                            list(self.employee_list.keys())[1]
                        ].keys()
                    ).index(task_name)
                    + 1
                )
            elif last != task_value["task date"] and len(
                list(
                    self.employee_list[
                        list(self.employee_list.keys())[1]
                    ].keys()
                )
            ) - 1 == list(
                self.employee_list[list(self.employee_list.keys())[1]].keys()
            ).index(
                task_name
            ):
                col_span = (
                    list(
                        self.employee_list[
                            list(self.employee_list.keys())[1]
                        ].keys()
                    ).index(task_name)
                    - last_col
                    + 1
                )
                self.entry = Entry(
                    self,
                    justify="center",
                    width=cell_width * col_span,
                    bg=self.table_cell_color(
                        count_cell // self.total_columns,
                        count_cell % self.total_columns,
                    ),
                    fg="Black",
                    font=("Arial", 16, "bold"),
                    borderwidth=self.table_borderwidth,
                    relief=self.table_relief_baze,
                    highlightbackground=self.table_highlightbackground,
                )
                self.entry.insert(END, last)
                # print(total_columns,total_rows,count_cell,count_cell//total_rows, count_cell%total_columns)
                self.entry.grid(
                    row=0, column=last_col, columnspan=col_span, sticky="nsew"
                )

                self.entry = Entry(
                    self,
                    justify="center",
                    bg=self.table_cell_color(
                        count_cell // self.total_columns,
                        count_cell % self.total_columns,
                    ),
                    fg="Black",
                    width=cell_width,
                    font=("Arial", 16, "bold"),
                    borderwidth=self.table_borderwidth,
                    relief=self.table_relief_baze,
                    highlightbackground=self.table_highlightbackground,
                )
                self.entry.insert(END, task_value["task date"])
                # print(total_columns,total_rows,count_cell,count_cell//total_rows, count_cell%total_columns)
                self.entry.grid(
                    row=0, column=last_col + col_span, sticky="nsew"
                )
                last = task_value["task date"]
                last_col = (
                    list(
                        self.employee_list[
                            list(self.employee_list.keys())[1]
                        ].keys()
                    ).index(task_name)
                    + 1
                )
            elif last == task_value["task date"] and len(
                list(
                    self.employee_list[
                        list(self.employee_list.keys())[1]
                    ].keys()
                )
            ) - 1 == list(
                self.employee_list[list(self.employee_list.keys())[1]].keys()
            ).index(
                task_name
            ):
                col_span = (
                    list(
                        self.employee_list[
                            list(self.employee_list.keys())[1]
                        ].keys()
                    ).index(task_name)
                    - last_col
                    + 2
                )
                self.entry = Entry(
                    self,
                    justify="center",
                    width=cell_width * col_span,
                    bg=self.table_cell_color(
                        count_cell // self.total_columns,
                        count_cell % self.total_columns,
                    ),
                    fg="Black",
                    font=("Arial", 16, "bold"),
                    borderwidth=self.table_borderwidth,
                    relief=self.table_relief_baze,
                    highlightbackground=self.table_highlightbackground,
                )
                self.entry.insert(END, last)
                # print(total_columns,total_rows,count_cell,count_cell//total_rows, count_cell%total_columns)
                self.entry.grid(
                    row=0, column=last_col, columnspan=col_span, sticky="nsew"
                )

        last = None
        last_col = 1
        # cписок тем
        for task_name in self.employee_list["task"]:
            if last == None:
                last = task_name.split("-")[0]
                last_col = self.employee_list["task"].index(task_name) + 1
            elif last != task_name.split("-")[0] and len(
                self.employee_list["task"]
            ) - 1 > self.employee_list["task"].index(task_name):
                col_span = (
                    self.employee_list["task"].index(task_name) - last_col + 1
                )
                self.entry = Entry(
                    self,
                    justify="center",
                    width=cell_width * col_span,
                    bg=self.table_cell_color(
                        count_cell // self.total_columns,
                        count_cell % self.total_columns,
                    ),
                    fg="Black",
                    font=("Arial", 16, "bold"),
                    borderwidth=self.table_borderwidth,
                    relief=self.table_relief_baze,
                    highlightbackground=self.table_highlightbackground,
                )
                self.entry.insert(END, last)
                # print(total_columns,total_rows,count_cell,count_cell//total_rows, count_cell%total_columns)
                self.entry.grid(
                    row=1, column=last_col, columnspan=col_span, sticky="nsew"
                )
                last = task_name.split("-")[0]
                last_col = self.employee_list["task"].index(task_name) + 1
            elif last != task_name.split("-")[0] and len(
                self.employee_list["task"]
            ) - 1 == self.employee_list["task"].index(task_name):
                col_span = (
                    self.employee_list["task"].index(task_name) - last_col + 1
                )
                self.entry = Entry(
                    self,
                    justify="center",
                    width=cell_width * col_span,
                    bg=self.table_cell_color(
                        count_cell // self.total_columns,
                        count_cell % self.total_columns,
                    ),
                    fg="Black",
                    font=("Arial", 16, "bold"),
                    borderwidth=self.table_borderwidth,
                    relief=self.table_relief_baze,
                    highlightbackground=self.table_highlightbackground,
                )
                self.entry.insert(END, last)
                # print(total_columns,total_rows,count_cell,count_cell//total_rows, count_cell%total_columns)
                self.entry.grid(
                    row=1, column=last_col, columnspan=col_span, sticky="nsew"
                )

                self.entry = Entry(
                    self,
                    justify="center",
                    bg=self.table_cell_color(
                        count_cell // self.total_columns,
                        count_cell % self.total_columns,
                    ),
                    fg="Black",
                    width=cell_width,
                    font=("Arial", 16, "bold"),
                    borderwidth=self.table_borderwidth,
                    relief=self.table_relief_baze,
                    highlightbackground=self.table_highlightbackground,
                )
                self.entry.insert(END, task_name.split("-")[0])
                # print(total_columns,total_rows,count_cell,count_cell//total_rows, count_cell%total_columns)
                self.entry.grid(
                    row=1, column=last_col + col_span, sticky="nsew"
                )
                last = task_name.split("-")[0]
                last_col = self.employee_list["task"].index(task_name) + 1
            elif last == task_name.split("-")[0] and len(
                self.employee_list["task"]
            ) - 1 == self.employee_list["task"].index(task_name):
                col_span = (
                    self.employee_list["task"].index(task_name) - last_col + 2
                )
                self.entry = Entry(
                    self,
                    justify="center",
                    width=cell_width * col_span,
                    bg=self.table_cell_color(
                        count_cell // self.total_columns,
                        count_cell % self.total_columns,
                    ),
                    fg="Black",
                    font=("Arial", 16, "bold"),
                    borderwidth=self.table_borderwidth,
                    relief=self.table_relief_baze,
                    highlightbackground=self.table_highlightbackground,
                )
                self.entry.insert(END, last)
                # print(total_columns,total_rows,count_cell,count_cell//total_rows, count_cell%total_columns)
                self.entry.grid(
                    row=1, column=last_col, columnspan=col_span, sticky="nsew"
                )

                """self.entry=Entry(
                            self,
                            justify='center',
                            width=cell_width*col_span,
                            bg=self.table_cell_color(count_cell//self.total_columns,count_cell%self.total_columns),
                            fg="Black",
                            font=("Arial", 16, "bold"),
                            borderwidth=self.table_borderwidth,
                            relief=self.table_relief_baze,
                            highlightbackground=self.table_highlightbackground
                        )
                #self.entry.insert(END,last)
                #print(total_columns,total_rows,count_cell,count_cell//total_rows, count_cell%total_columns)
                self.entry.grid(row=1, column=last_col+col_span,columnspan=self.add_columns, sticky='nsew')
                print(last_col,col_span)"""

        count_cell = 0
        cell_width = 3

        # задачи
        for student_name, task_name in self.employee_list.items():
            if student_name == "task":
                # строка дата

                # строка номера
                self.entry = Entry(
                    self,
                    width=(
                        cell_width
                        if count_cell % (self.total_columns - self.add_columns)
                        != 0
                        else max_len_column_0
                    ),
                    bg=self.table_cell_color(
                        count_cell // self.total_columns + self.row_add,
                        count_cell % self.total_columns,
                    ),
                    fg="Black",
                    font=("Arial", 16, "bold"),
                    borderwidth=self.table_borderwidth,
                    relief=self.table_relief_baze,
                    highlightbackground=self.table_highlightbackground,
                )
                self.entry.insert(
                    END,
                    self.table_cell_text(
                        count_cell // self.total_columns + self.row_add,
                        count_cell % self.total_columns,
                    ),
                )
                # print(total_columns,total_rows,count_cell,count_cell//total_rows, count_cell%total_columns)
                self.entry.grid(
                    row=count_cell // (self.total_columns - self.add_columns),
                    column=count_cell % (self.total_columns - self.add_columns),
                    rowspan=3,
                    sticky="nsew",
                )
                self.event_table(
                    self.entry,
                    count_cell // self.total_columns + self.row_add,
                    count_cell % self.total_columns,
                )

                count_cell += 1
                for i in task_name:
                    self.entry = Entry(
                        self,
                        width=(
                            cell_width
                            if count_cell % self.total_columns != 0
                            else max_len_column_0
                        ),
                        bg=self.table_cell_color(
                            count_cell // self.total_columns + self.row_add,
                            count_cell % self.total_columns,
                        ),
                        fg="Black",
                        font=("Arial", 16, "bold"),
                        justify="center",
                        borderwidth=self.table_borderwidth,
                        relief=self.table_relief_baze,
                        highlightbackground=self.table_highlightbackground,
                    )
                    self.entry.insert(
                        END,
                        self.table_cell_text(
                            count_cell // self.total_columns + self.row_add,
                            count_cell % self.total_columns,
                        ),
                    )
                    # print(i)
                    # print(total_columns,total_rows,count_cell,count_cell//total_columns, count_cell%total_columns)
                    self.entry.grid(
                        row=count_cell // self.total_columns + self.row_add,
                        column=count_cell % self.total_columns,
                        sticky="nsew",
                    )
                    self.event_table(
                        self.entry,
                        count_cell // self.total_columns + self.row_add,
                        count_cell % self.total_columns,
                    )
                    count_cell += 1

                for i in range(self.total_columns - count_cell):
                    self.entry = Text(
                        self,
                        width=len(self.add_columns_name[i]) + 1,
                        height=3,
                        bg=self.table_cell_color(
                            count_cell // self.total_columns + self.row_add,
                            count_cell % self.total_columns,
                        ),
                        fg="Black",
                        font=("Arial", 16, "bold"),
                        borderwidth=self.table_borderwidth,
                        relief=self.table_relief_baze,
                        highlightbackground=self.table_highlightbackground,
                    )
                    self.entry.insert(
                        END,
                        self.table_cell_text(
                            count_cell // self.total_columns + self.row_add,
                            count_cell % self.total_columns,
                        ),
                    )
                    self.entry.tag_configure("center", justify="center")
                    self.entry.tag_add("center", "1.0", "end")
                    # print(total_columns,total_rows,count_cell,count_cell//total_columns, count_cell%total_columns)
                    self.entry.grid(
                        row=count_cell // (self.total_columns),
                        column=count_cell % (self.total_columns),
                        rowspan=3,
                        sticky="nsew",
                    )
                    self.event_table(
                        self.entry,
                        count_cell // self.total_columns + self.row_add,
                        count_cell % self.total_columns,
                    )
                    count_cell += 1
            else:

                self.entry = Entry(
                    self,
                    width=cell_width,
                    bg=self.table_cell_color(
                        count_cell // self.total_columns + self.row_add,
                        count_cell % self.total_columns,
                    ),
                    fg="Black",
                    font=("Arial", 16, "bold"),
                    justify="left",
                    borderwidth=self.table_borderwidth,
                    relief=self.table_relief_baze,
                    highlightbackground=self.table_highlightbackground,
                )
                self.entry.insert(
                    END,
                    self.table_cell_text(
                        count_cell // self.total_columns + self.row_add,
                        count_cell % self.total_columns,
                    ),
                )
                # print(total_columns,total_rows,count_cell,count_cell//total_rows, count_cell%total_columns)
                self.entry.grid(
                    row=count_cell // self.total_columns + self.row_add,
                    column=count_cell % self.total_columns,
                    sticky="nsew",
                )
                self.event_table(
                    self.entry,
                    count_cell // self.total_columns + self.row_add,
                    count_cell % self.total_columns,
                )
                count_cell += 1
                for task_key, task_value in task_name.items():
                    self.entry = Entry(
                        self,
                        width=cell_width,
                        bg=self.table_cell_color(
                            count_cell // self.total_columns + self.row_add,
                            count_cell % self.total_columns,
                        ),
                        fg="Black",
                        font=("Arial", 16, "bold"),
                        justify="center",
                        borderwidth=self.table_borderwidth,
                        relief=self.table_relief_baze,
                        highlightbackground=self.table_highlightbackground,
                    )
                    self.entry.insert(
                        END,
                        self.table_cell_text(
                            count_cell // self.total_columns + self.row_add,
                            count_cell % self.total_columns,
                        ),
                    )
                    # print(total_columns,total_rows,count_cell,count_cell//total_columns, count_cell%total_columns)
                    self.entry.grid(
                        row=count_cell // self.total_columns + self.row_add,
                        column=count_cell % self.total_columns,
                        sticky="nsew",
                    )
                    self.event_table(
                        self.entry,
                        count_cell // self.total_columns + self.row_add,
                        count_cell % self.total_columns,
                    )
                    count_cell += 1

                self.entry = Entry(
                    self,
                    width=(
                        cell_width
                        if count_cell % (self.total_columns) != 0
                        else max_len_column_0
                    ),
                    bg=self.table_cell_color(
                        count_cell // self.total_columns,
                        count_cell % self.total_columns,
                    ),
                    fg="Black",
                    font=("Arial", 16, "bold"),
                    justify="center",
                    borderwidth=self.table_borderwidth,
                    relief=self.table_relief_baze,
                    highlightbackground=self.table_highlightbackground,
                )
                self.entry.insert(
                    END,
                    self.table_cell_text(
                        count_cell // self.total_columns + self.row_add,
                        count_cell % self.total_columns,
                    ),
                )
                # print(total_columns,total_rows,count_cell,count_cell//total_columns, count_cell%total_columns)
                self.entry.grid(
                    row=count_cell // self.total_columns + self.row_add,
                    column=count_cell % self.total_columns,
                    sticky="nsew",
                )
                self.event_table(
                    self.entry,
                    count_cell // self.total_columns + self.row_add,
                    count_cell % self.total_columns,
                )
                count_cell += 1
                for i in range(
                    self.total_columns - (count_cell % self.total_columns)
                ):
                    self.entry = Entry(
                        self,
                        width=(
                            cell_width
                            if count_cell % self.total_columns != 0
                            else max_len_column_0
                        ),
                        bg=self.table_cell_color(
                            count_cell // self.total_columns + self.row_add,
                            count_cell % self.total_columns,
                        ),
                        fg="Black",
                        font=("Arial", 16, "bold"),
                        justify="center",
                        borderwidth=self.table_borderwidth,
                        relief=self.table_relief_baze,
                        highlightbackground=self.table_highlightbackground,
                    )
                    self.entry.insert(
                        END,
                        self.table_cell_text(
                            count_cell // self.total_columns + self.row_add,
                            count_cell % self.total_columns,
                        ),
                    )
                    # print(total_columns,total_rows,count_cell,count_cell//total_columns, count_cell%total_columns)
                    self.entry.grid(
                        row=count_cell // self.total_columns + self.row_add,
                        column=count_cell % (self.total_columns),
                        sticky="nsew",
                    )
                    self.event_table(
                        self.entry,
                        count_cell // self.total_columns + self.row_add,
                        count_cell % self.total_columns,
                    )
                    count_cell += 1

    def open_code_student(self, row, column):
        self.app.update_student()
        self.code_frame.update_code_student(row, column)
        # self.code_frame.update_code_student(list(self.employee_list.items())[row][1][self.employee_list["task"][column-1]])
        # print(list(self.employee_list.items())[row][1][self.employee_list["task"][column-1]]["student_code"])

    def event_table(self, tmp, row, column):
        tmp.bind(
            "<Enter>",
            lambda event, row=row, column=column: self.highlight_row_and_column(
                row, column
            ),
        )
        tmp.bind("<Leave>", self.clear_highlight)
        tmp.bind(
            "<Button-1>",
            lambda event, row=row - self.row_add, column=column: self.open_code_student(
                row, column
            ),
        )
        tmp.bind(
            "<Return>",
            lambda event, row=row, column=column: self.enter_grade(row, column),
        )
        tmp.bind(
            "<Button-3>",
            lambda event, row=row, column=column: self.show_menu(
                event, row, column
            ),
        )

    def enter_grade(self, row, column):
        # изменение значения в ячейке (балл за задание grade)
        self.employee_list = self.t.get_employee()
        tmp = float(self.grid_slaves(row=row, column=column)[0].get())
        list(self.employee_list.items())[row - self.row_add][1][
            self.employee_list["task"][column - 1]
        ]["grade"] = tmp
        self.t.set_employee(self.employee_list)
        print(row, column, self.grid_slaves(row=row, column=column)[0].get())

    def highlight_row_and_column(self, row, column):
        # Удаляем предыдущее выделение
        self.clear_highlight()

        # Выделяем строку и столбец
        for i in range(self.row_add, self.total_rows):
            if self.table_cell_color(i, column) == self.table_cell_color_green:
                self.grid_slaves(row=i)[-(column + 1)].configure(bg="#548B54")
            elif (
                self.table_cell_color(i, column) == self.table_cell_color_yellow
            ):
                self.grid_slaves(row=i)[-(column + 1)].configure(bg="#CDCD00")
            elif self.table_cell_color(i, column) == self.table_cell_color_red:
                self.grid_slaves(row=i)[-(column + 1)].configure(bg="#CD2626")
            elif self.table_cell_color(i, column) == self.table_cell_color_cian:
                self.grid_slaves(row=i)[-(column + 1)].configure(bg="#00CDCD")
            else:
                # self.grid_slaves(row=i)[-(column+1)].configure(relief=self.table_relief_highlight)
                self.grid_slaves(row=i)[-(column + 1)].configure(
                    bg=self.blend_colors(
                        self.table_cell_color(i, column),
                        self.table_highlight_color,
                    )
                )  # Голубой цвет для ячеек
            # self.grid_slaves(row=i)[column].config(bd=1, relief=tk.SOLID, borderwidth=1)  # Границы ячейки
        for j in range(self.total_columns):
            # self.grid_slaves(row=row)[-(j+1)].configure(relief=self.table_relief_highlight)
            if self.table_cell_color(row, j) == self.table_cell_color_green:
                self.grid_slaves(row=row)[-(j + 1)].configure(bg="#548B54")
            elif self.table_cell_color(row, j) == self.table_cell_color_yellow:
                self.grid_slaves(row=row)[-(j + 1)].configure(bg="#CDCD00")
            elif self.table_cell_color(row, j) == self.table_cell_color_red:
                self.grid_slaves(row=row)[-(j + 1)].configure(bg="#CD2626")
            elif self.table_cell_color(row, j) == self.table_cell_color_cian:
                self.grid_slaves(row=row)[-(j + 1)].configure(bg="#00CDCD")
            else:
                self.grid_slaves(row=row)[-(j + 1)].configure(
                    bg=self.blend_colors(
                        self.table_cell_color(row, j),
                        self.table_highlight_color,
                    )
                )  # Голубой цвет для ячеек
        #    self.grid_slaves(row=row)[j].config(bd=1, relief=tk.SOLID, borderwidth=1)  # Границы ячейки

        # Запоминаем выбранную строку и столбец
        self.selected_row = row
        self.selected_column = column

    def clear_highlight(self, event=None):
        if self.selected_row is not None and self.selected_column is not None:
            # Удаляем выделение из предыдущей строки и столбца
            for i in range(self.row_add, self.total_rows):
                # self.grid_slaves(row=i)[-(self.selected_column+1)].configure(relief=self.table_relief_baze)
                self.grid_slaves(row=i)[-(self.selected_column + 1)].configure(
                    bg=self.table_cell_color(i, self.selected_column)
                )
            for j in range(self.total_columns):
                # self.grid_slaves(row=self.selected_row)[-(j+1)].configure(relief=self.table_relief_baze)
                self.grid_slaves(row=self.selected_row)[-(j + 1)].configure(
                    bg=self.table_cell_color(self.selected_row, j)
                )

            # Сбрасываем выбранную строку и столбец
            self.selected_row = None
            self.selected_column = None

    def table_cell_color(self, row, column):
        # (len(employee_list["task"])+1)
        row = row - self.row_add
        if row < 1:
            return self.table_cell_color_header
        elif row > 0 and 0 < column < len(self.employee_list["task"]) + 1:
            if (
                list(self.employee_list.items())[row][1][
                    self.employee_list["task"][column - 1]
                ]["done"]
                == None
            ):
                return self.table_cell_color_white
            elif (
                list(self.employee_list.items())[row][1][
                    self.employee_list["task"][column - 1]
                ]["done"]
                == False
            ):
                return self.table_cell_color_white
            elif (
                list(self.employee_list.items())[row][1][
                    self.employee_list["task"][column - 1]
                ]["grade"]
                != None
            ):
                if (
                    list(self.employee_list.items())[row][1][
                        self.employee_list["task"][column - 1]
                    ]["grade"]
                    == 1.0
                ):
                    return self.table_cell_color_green
                elif (
                    0
                    < list(self.employee_list.items())[row][1][
                        self.employee_list["task"][column - 1]
                    ]["grade"]
                    < 1
                ):
                    return self.table_cell_color_yellow
                else:
                    return self.table_cell_color_red
            elif (
                list(self.employee_list.items())[row][1][
                    self.employee_list["task"][column - 1]
                ]["auto_check"]
                == True
            ):
                return self.table_cell_color_green
            elif (
                list(self.employee_list.items())[row][1][
                    self.employee_list["task"][column - 1]
                ]["auto_check"]
                == False
            ):
                return self.table_cell_color_red
            elif (
                list(self.employee_list.items())[row][1][
                    self.employee_list["task"][column - 1]
                ]["done"]
                == True
                and list(self.employee_list.items())[row][1][
                    self.employee_list["task"][column - 1]
                ]["auto_check"]
                == None
            ):
                if (
                    list(self.employee_list.items())[row][1][
                        self.employee_list["task"][column - 1]
                    ]["execution_time"]
                    == False
                ):
                    return self.table_cell_color_cian
                else:
                    return self.table_cell_color_yellow
        elif column == len(self.employee_list["task"]) + 2:
            if self.table_teacher_check(row):
                return self.table_cell_color_green
            else:
                return self.table_cell_color_white
        else:
            return self.table_cell_color_white

    def blend_colors(self, color1, color2):
        # Получаем значения RGB для каждого цвета
        if color1 == self.table_cell_color_green:
            return self.table_cell_color_green
        r1, g1, b1 = (
            int(color1[1:3], 16),
            int(color1[3:5], 16),
            int(color1[5:], 16),
        )
        r2, g2, b2 = (
            int(color2[1:3], 16),
            int(color2[3:5], 16),
            int(color2[5:], 16),
        )

        # Вычисляем средние значения для каждого канала
        r_avg = (r1 + r2) // 2
        g_avg = (g1 + g2) // 2
        b_avg = (b1 + b2) // 2

        # Форматируем значения обратно в строку hex
        blended_color = f"#{r_avg:02X}{g_avg:02X}{b_avg:02X}"
        return blended_color

    def table_cell_text(self, row, column):
        row = row - self.row_add
        if row == 0:
            if column == 0:
                return "Ученик\№"
            elif column < len(self.employee_list["task"]) + 1:
                return self.employee_list["task"][column - 1].split("-")[1]
            else:
                return self.add_columns_name[
                    column - len(self.employee_list["task"]) - 1
                ]
        elif row > 0:
            if column == 0:
                return list(self.employee_list.keys())[row]
            elif column < len(self.employee_list["task"]) + 1:
                if (
                    list(self.employee_list.items())[row][1][
                        self.employee_list["task"][column - 1]
                    ]["done"]
                    == False
                    or list(self.employee_list.items())[row][1][
                        self.employee_list["task"][column - 1]
                    ]["done"]
                    == None
                ):
                    return ""
                elif (
                    list(self.employee_list.items())[row][1][
                        self.employee_list["task"][column - 1]
                    ]["done"]
                    == True
                ):
                    if (
                        list(self.employee_list.items())[row][1][
                            self.employee_list["task"][column - 1]
                        ]["auto_check"]
                        == False
                    ):
                        return 0
                    elif (
                        list(self.employee_list.items())[row][1][
                            self.employee_list["task"][column - 1]
                        ]["auto_check"]
                        == None
                    ):
                        return "+"
                    elif (
                        list(self.employee_list.items())[row][1][
                            self.employee_list["task"][column - 1]
                        ]["auto_check"]
                        == True
                    ):
                        if (
                            list(self.employee_list.items())[row][1][
                                self.employee_list["task"][column - 1]
                            ]["grade"]
                            == None
                        ):
                            return ""
                        elif (
                            list(self.employee_list.items())[row][1][
                                self.employee_list["task"][column - 1]
                            ]["grade"]
                            != None
                        ):
                            if (
                                list(self.employee_list.items())[row][1][
                                    self.employee_list["task"][column - 1]
                                ]["grade"]
                                == 1.0
                            ):
                                return 1
                            elif (
                                list(self.employee_list.items())[row][1][
                                    self.employee_list["task"][column - 1]
                                ]["grade"]
                                == 0.0
                            ):
                                return 0
                            else:
                                return list(self.employee_list.items())[row][1][
                                    self.employee_list["task"][column - 1]
                                ]["grade"]
            elif (
                self.add_columns_name[
                    column - len(self.employee_list["task"]) - 1
                ]
                == self.add_columns_name[0]
            ):
                grade = 0
                for j in range(len(self.employee_list["task"])):
                    if (
                        list(self.employee_list.items())[row][1][
                            self.employee_list["task"][j]
                        ]["grade"]
                        != None
                    ):
                        grade += list(self.employee_list.items())[row][1][
                            self.employee_list["task"][j]
                        ]["grade"]
                if grade == 0:
                    return ""
                else:
                    return round(grade, 1)
                """elif self.add_columns_name[column-len(self.employee_list['task'])-1] == self.add_columns_name[1]:
                if self.table_teacher_check(row):
                    return '+'
                else:
                    return '' """
            elif (
                self.add_columns_name[
                    column - len(self.employee_list["task"]) - 1
                ]
                == self.add_columns_name[1]
            ):
                return self.table_pv(row)
            elif (
                self.add_columns_name[
                    column - len(self.employee_list["task"]) - 1
                ]
                == self.add_columns_name[2]
            ):
                return self.table_pvr(row)
            elif (
                self.add_columns_name[
                    column - len(self.employee_list["task"]) - 1
                ]
                == self.add_columns_name[3]
            ):
                return self.table_student_grade(row)

    def table_teacher_check(self, row):
        # функция проверяет что каждая задача ученика была проверена учителем
        for j in range(len(self.employee_list["task"])):
            if (
                list(self.employee_list.items())[row][1][
                    self.employee_list["task"][j]
                ]["teacher_check"]
                != True
            ):
                return False
        else:
            return True

    def table_pv(self, row):
        ct = 0
        c = 0
        grade = 0
        for j in range(len(self.employee_list["task"])):
            ct += 1
            if (
                list(self.employee_list.items())[row][1][
                    self.employee_list["task"][j]
                ]["grade"]
                != None
            ):
                grade += list(self.employee_list.items())[row][1][
                    self.employee_list["task"][j]
                ]["grade"]
            if (
                list(self.employee_list.items())[row][1][
                    self.employee_list["task"][j]
                ]["auto_check"]
                == True
            ):
                c += 1
        return int(grade / ct * 100)

    def table_pvr(self, row):
        ct = 0
        c = 0
        grade = 0
        for j in range(len(self.employee_list["task"])):
            if (
                list(self.employee_list.items())[row][1][
                    self.employee_list["task"][j]
                ]["done"]
                == True
            ):
                ct += 1
            if (
                list(self.employee_list.items())[row][1][
                    self.employee_list["task"][j]
                ]["grade"]
                != None
            ):
                grade += list(self.employee_list.items())[row][1][
                    self.employee_list["task"][j]
                ]["grade"]
        if ct == 0:
            return 0
        else:
            return int(grade / ct * 100)

    def table_student_grade(self, row):
        a = self.table_pv(row)
        if a < 60:
            return 2
        elif a >= 60 and a < 70:
            return 3
        elif a >= 70 and a < 85:
            return 4
        elif a >= 85:
            return 5

    def update_table(self, employee_list, date_list=None):
        if date_list == None:
            date_list = self.date_list
        self.date_list = date_list
        self.employee_list = employee_list
        self.total_rows = len(self.employee_list)
        self.total_columns = len(self.employee_list["task"]) + self.add_columns
        for widget in self.grid_slaves():
            widget.grid_forget()
        self.create_table()

    def update_table_list(self, employee_list):
        self.code_frame.update(employee_list)

    def maxlen(self, s):
        max_len = len(s[0])
        for i in s:
            if len(i) > max_len:
                max_len = len(i)
        return max_len

    def create_widget(self):
        frame_top = self
        self.program_text = Text(frame_top, width=80, height=20)
        self.program_text.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        self.program_scroll = Scrollbar(frame_top, orient="vertical")

        self.program_scroll.grid(row=0, column=2, sticky="ns")
        self.program_text.config(yscrollcommand=self.program_scroll.set)
        self.program_scroll = Scrollbar(frame_top, orient="horizontal")
        self.program_scroll.grid(row=1, column=0, columnspan=3, sticky="we")
        self.program_text.config(xscrollcommand=self.program_scroll.set)
        frame_top.pack(side=LEFT)

    # def update_code_student(self,code):
    #   self.program_text.insert(END,code)
