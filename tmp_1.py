import tkinter as tk

def button_click():
    print("Кнопка нажата!")

root = tk.Tk()
root.title("Пример с тремя фреймами")

# Функция для создания фреймов с текстовым полем и кнопкой
def create_frame(parent):
    frame = tk.Frame(parent, bd=2, relief="solid", padx=5, pady=5)
    frame.pack(side="left", padx=5, pady=5)

    text_entry = tk.Entry(frame)
    text_entry.pack(pady=5)

    button = tk.Button(frame, text="Нажми меня", command=button_click)
    button.pack(pady=5)

# Создание трех фреймов
for _ in range(3):
    create_frame(root)

root.mainloop()
