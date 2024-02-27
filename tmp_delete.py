import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.geometry("300x200")

# Создаем виджет Text
text_widget = tk.Text(root, wrap="word")
text_widget.pack(expand=True, fill="both")

# Многострочный текст с использованием \n для переносов строк
multiline_text = "Это\nмногострочный\nтекст"

# Вставляем многострочный текст в Text
text_widget.insert("1.0", multiline_text)

root.mainloop()