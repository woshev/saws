import tkinter as tk
from tkinter import ttk

def on_click(event):
    row = tree.identify_row(event.y)
    column = tree.identify_column(event.x)
    row_num = tree.index(row)
    col_num = tree.column(tree.identify_column(column), "id")
    print(f"Clicked on Row: {row_num}, Column: {col_num}")

def create_table(data):
    num_rows = len(data)
    num_cols = len(data[0])
    
    tree["columns"] = tuple(range(num_cols))
    tree.heading("#0", text="Index")
    tree.column("#0", width=50)
    for col_num in range(num_cols):
        tree.heading(col_num, text=f"Column {col_num}")
        tree.column(col_num, width=100)

    for i, row_data in enumerate(data):
        tree.insert("", "end", text=f"Row {i}", values=row_data)

root = tk.Tk()
root.title("Table with Row and Column Click")
frame=ttk.Frame(root,borderwidth=2, relief="sunken")
frame.pack()
tree = ttk.Treeview(frame)
style = ttk.Style()
style.configure("Treeview", font=("Helvetica", 10), rowheight=25)
style.configure("Treeview.Cell", borderwidth=1, relief="sunken")
style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), relief="flat", borderwidth=1)
 
# Установка цвета фона для выделенной строки
style.map("Treeview.Cell", background=[("selected", "lightblue")], foreground=[("selected", "black")])
style.configure("Treeview.Heading", foreground='green') #
create_table([[f"Value {i}_{j}" for j in range(5)] for i in range(10)])

tree.bind("<Button-1>", on_click)
tree.pack(expand=True, fill="both")

root.mainloop()
