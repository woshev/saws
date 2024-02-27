import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from pygments import highlight
import pygments.lexers as pl
import pygments.formatters as pf
from pygments.formatters import Terminal256Formatter
import tkhtmlview as th

def highlight_python_code(python_code):
    # Определяем лексер для Python
    lexer = pl.PythonLexer()
    # Получаем выделенный код
    highlighted_code = highlight(python_code, lexer, pf.HtmlFormatter(style="lightbulb",noclasses=True))
    return highlighted_code

# Создаем главное окно
root = tk.Tk()
root.title("Выделение синтаксиса Python")

# Пример исходного кода на Python
python_code = '''
from typing import Iterator

# This is an example
class Math:
    @staticmethod
    def fib(n: int) -> Iterator[int]:
        """Fibonacci series up to n."""
        a, b = 0, 1
        while a < n:
            yield a
            a, b = b, a + b

result = sum(Math.fib(42))
print("The answer is {}".format(result))
'''
#python_code = 'print(\n'

# Получаем выделенный код
highlighted_code = highlight_python_code(python_code)
print(highlighted_code)
html_text = th.HTMLText(root, font=("Consolas", 12))
html_text.insert("1.0",highlighted_code)
html_text.pack(fill="both", expand=True)
# Вставляем выделенный код в текстовое поле
#text.insert(tk.INSERT, highlighted_code)

# Запускаем главный цикл обработки событий
root.mainloop()
