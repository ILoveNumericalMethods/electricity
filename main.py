from tkinter import *
import tkinter
from tkinter.filedialog import *
from tkinter import ttk

def start_execution():
    print("start")
def show_message():
    label["text"] = entry.get()     # получаем введенный текст

def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    root = tkinter.Tk()
    # пространство отображается на холсте типа Canvas
    space = tkinter.Canvas(root, width=1200, height=600, bg="black")
    space.pack(side=tkinter.BOTTOM)
    # верхняя панель с кнопками
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.RIGHT)

    start_button = tkinter.Button(frame, text="Start", command=start_execution, width=10)
    start_button.pack(side=tkinter.LEFT)

    entryExample = tkinter.Entry(root,
                            width=180)

    entryExample.pack(side=tkinter.LEFT,
                      padx=10)

    root.mainloop()



if __name__ == '__main__':
    main()
