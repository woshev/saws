import tkinter as tk
from tkhtmlview import HTMLText

# HTML код для отображения в HTMLText и вывода в консоль
html_code = """
<div class="highlight" style="background: #1d2331"><pre style="line-height: 125%;">
<span style="color: #FFAD66">from</span> <span style="color: #d4d2c8">typing</span> <span style="color: #FFAD66">import</span> <span style="color: #d4d2c8">Iterator</span>

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
root.title("Отображение HTML в HTMLText и вывод в консоль")

# Создание и настройка виджета HTMLText
html_text = HTMLText(root, height=30, width=80)
html_text.pack(expand=True, fill=tk.BOTH)

# Вставка HTML кода в HTMLText
html_text.set_html(html_code)

# Вывод HTML текста в консоль
print(html_text.get_text())

# Запуск главного цикла
root.mainloop()
