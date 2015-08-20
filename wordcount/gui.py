import tkinter
from tkinter import constants
from tkinter.filedialog import askopenfile
from tkinter.scrolledtext import ScrolledText

from core import count_words, top_words, lines


class SmartScrolledText(ScrolledText):
    @property
    def text(self):
        return self.get(1.0, tkinter.END)

    @text.setter
    def text(self, value):
        self.delete(1.0, tkinter.END)
        self.insert(tkinter.INSERT, value)


class App:
    FILE_TYPES = (
        ('Arquivo Texto', '*.txt'),
        ('Todos', '*.*'),
    )

    COUNT = 1
    TOP = 2
    MODE = {
        COUNT: count_words,
        TOP: top_words,
    }

    def __init__(self, parent):
        self._file = None
        self.option = tkinter.IntVar()
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # define buttons
        rb1 = tkinter.Radiobutton(master=self.parent, text='Count', value=self.COUNT, variable=self.option, command=self.on_change)
        rb1.pack(anchor=tkinter.W)

        rb2 = tkinter.Radiobutton(master=self.parent, text='Top', value=self.TOP, variable=self.option, command=self.on_change)
        rb2.pack(anchor=tkinter.W)

        btn = tkinter.Button(self.parent, text='Escolher arquivo', command=self.on_click)
        btn.pack(fill=constants.BOTH, padx=5, pady=5)

        frame = tkinter.Frame(master=self.parent)
        frame.pack(fill='both', expand='yes')

        self.textarea = SmartScrolledText(master=frame, wrap=tkinter.WORD, width=25, height=20)
        self.textarea.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)

    def on_change(self):
        if not self._file:
            return
        self.show_words()

    def on_click(self):
        """Returns an opened file in read mode."""
        self._file = askopenfile(mode='r', filetypes=self.FILE_TYPES)
        self.show_words()

    def show_words(self):
        self._file.seek(0)

        op = self.MODE[self.option.get()]

        self.textarea.text = lines(op(self._file))


def gui():
    root = tkinter.Tk()
    root.title("Word count 1.0")

    app = App(root)
    root.mainloop()
