import tkinter as tk
from tkhtmlview import HTMLScrolledText
import pygments.lexers as pl
import pygments.formatters as pf

def highlight_python_code(python_code):
    lexer = pl.PythonLexer()
    highlighted_code = pf.HtmlFormatter(style="lightbulb", noclasses=True).get_style_defs('.highlight') + highlight(python_code, lexer, pf.HtmlFormatter(noclasses=True))
    return highlighted_code

def change(html_label):
    cursor = html_label.index(tk.INSERT)
    code = html_label.get("1.0", "end-1c")
    h_code = highlight_python_code(code)
    html_label.set_html(h_code, strip=False)
    html_label.mark_set(tk.INSERT, cursor)
    style_tags = html_label.tag_names(cursor)
    for tag in style_tags:
        html_label.tag_add(tag, "1.0", "end")

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

root = tk.Tk()
root.title("Отображение HTML в Tkinter с помощью tkhtmlview")

html_label = HTMLScrolledText(root)
html_label.set_html('<pre><code>{}</code></pre>'.format(python_code), strip=False)
html_label.pack(expand=True, fill=tk.BOTH)
html_label.bind("<KeyRelease>", lambda event: change(html_label))

root.mainloop()
