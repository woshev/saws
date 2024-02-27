import tkinter as tk
from tkhtmlview import HTMLScrolledText
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

def change(html_label):
    cursor = html_label.index(tk.INSERT)
    # Получаем стиль текста вокруг курсора
    code = html_label.get("1.0","end-1c")
    h_code = highlight_python_code(code)
    html_label.set_html(h_code,strip = False)
    html_label.mark_set(tk.INSERT,cursor)
    style_tags = html_label.tag_names(cursor)






# HTML код для отображения в Tkinter HtmlFrame и вывода в консоль
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
html_code = """<div class="highlight" style="background: #1d2331"><pre style="line-height: 125%;"><span></span><span style="color: #FFAD66">from</span> <span style="color: #d4d2c8">typing</span> <span style="color: #FFAD66">import</span> <span style="color: #d4d2c8">Iterator</span>

<span style="color: #7e8aa1"># This is an example</span>
<span style="color: #FFAD66">class</span> <span style="color: #73D0FF">Math</span><span style="color: #d4d2c8">:</span>
    <span style="color: #7e8aa1; font-weight: bold; font-style: italic">@staticmethod</span>
    <span style="color: #FFAD66">def</span> <span style="color: #FFD173">fib</span><span style="color: #d4d2c8">(n:</span> <span style="color: #FFD173">int</span><span style="color: #d4d2c8">)</span> <span style="color: #FFAD66">-&gt;</span> <span style="color: #d4d2c8">Iterator[</span><span style="color: #FFD173">int</span><span style="color: #d4d2c8">]:</span>
<span style="color: #d4d2c8">        </span><span style="color: #7e8aa1">&quot;&quot;&quot;Fibonacci series up to n.&quot;&quot;&quot;</span>
        <span style="color: #d4d2c8">a,</span> <span style="color: #d4d2c8">b</span> <span style="color: #FFAD66">=</span> <span style="color: #DFBFFF">0</span><span style="color: #d4d2c8">,</span> <span style="color: #DFBFFF">1</span>
        <span style="color: #FFAD66">while</span> <span style="color: #d4d2c8">a</span> <span style="color: #FFAD66">&lt;</span> <span style="color: #d4d2c8">n:</span>
            <span style="color: #FFAD66">yield</span> <span style="color: #d4d2c8">a</span>
            <span style="color: #d4d2c8">a,</span> <span style="color: #d4d2c8">b</span> <span style="color: #FFAD66">=</span> <span style="color: #d4d2c8">b,</span> <span style="color: #d4d2c8">a</span> <span style="color: #FFAD66">+</span> <span style="color: #d4d2c8">b</span>

<span style="color: #d4d2c8">result</span> <span style="color: #FFAD66">=</span> <span style="color: #FFD173">sum</span><span style="color: #d4d2c8">(Math</span><span style="color: #FFAD66">.</span><span style="color: #d4d2c8">fib(</span><span style="color: #DFBFFF">42</span><span style="color: #d4d2c8">))</span>
<span style="color: #FFD173">print</span><span style="color: #d4d2c8">(</span><span style="color: #D5FF80">&quot;The answer is </span><span style="color: #95E6CB">{}</span><span style="color: #D5FF80">&quot;</span><span style="color: #FFAD66">.</span><span style="color: #d4d2c8">format(result))</span>
</pre></div>


"""

# Создание главного окна
root = tk.Tk()
root.title("Отображение HTML в Tkinter с помощью tkhtmlview")

# Создание и настройка виджета HTMLLabel
html_label = HTMLScrolledText(root)
html_label.configure(bg="#1d2331")
html_label.configure(insertbackground="white")
html_label.set_html(highlighted_code,strip=False)
html_label.pack(expand=True, fill=tk.BOTH)
html_label.bind("<KeyRelease>",lambda event:change(html_label))
print(1)
print(repr(html_label.get(1.0,tk.END)))
print(2)
highlighted_code = highlight_python_code(python_code)
html_label.set_html(highlighted_code,strip=False)
print(repr(html_label.get(1.0,tk.END)))
# Запуск главного цикла
root.mainloop()
