from tkinter import *
import tkinter
from tkinter.filedialog import *
from tkinter import ttk

def show_message(): #функция считывает введённую формулу и запускает функцию создания объекта
    print(entry.get())     # получаем введенный текст

#создаём окно
root = tkinter.Tk()
root.title("METANIT.COM")
root.geometry("1200x600")

#создание холста
space = tkinter.Canvas(root, width=1200, height=560, bg="black")
space.pack(side=tkinter.BOTTOM)

# верхняя панель с кнопками
frame = tkinter.Frame(root)
frame.pack(side=tkinter.RIGHT)

#окно для ввода
entry = ttk.Entry()
entry = tkinter.Entry(root, width=180)
entry.pack(anchor=NW, padx=6, pady=8)

#кнопка Добавить объект
button = tkinter.Button(frame, text="Добавить объект", command=show_message, width=20)
button.pack(side=tkinter.LEFT)

root.mainloop()
