import tkinter as tk
from tkhtmlview import HTMLText

# HTML-текст в переменной tmp
tmp = """
<!DOCTYPE html>
<html>
<head>
  <title>Пример HTML</title>
</head>
<body>
  <h1>Добро пожаловать в Tkinter!</h1>
  <p>Это пример использования HTML в Tkinter.</p>
</body>
</html>
"""

# Исправление стилей HTML-текста
def apply_styles(html_text):
    html_text.tag_configure('h1', foreground='#f88f7f')
    html_text.tag_configure('p', foreground='#f88f7f')

# Создание окна Tkinter
root = tk.Tk()
root.title("Вставка HTML в Tkinter")

# Создание виджета HTMLText и вставка HTML-текста
html_text = HTMLText(root, wrap='word')
html_text.pack(expand=True, fill='both')

apply_styles(html_text)
html_text.set_html(tmp)
root.mainloop()
