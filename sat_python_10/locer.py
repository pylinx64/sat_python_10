import pyautogui 
from pyautogui import click, moveTo
from tkinter import Tk, Entry, Label
import time

# создаем окно
root = Tk()

# длина и высота экрана
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

# полный экран
root.attributes('-fullscreen', True)

# добавляет текст
text = Label(root, text='''Хакер /nxab/g👽''', font=1)
text.grid(row=0, column=0)

# добавляет поля для ввода
input_text = Entry(root, font=1)
# ширина, длина поля; x, y 
input_text.place(width=200, height=40, x=w/2-85, y=h/2)

# обновляем экран
root.update()

while True:
    root.update()
