import turtle
import time

list_colors = ['white', 'lime', 'yellow', 'pink']
t=turtle.Pen()


def side():
	'''Функция рисует сторону с разным цветом'''
	t.pencolor(list_colors[1])
	t.forward(15)
	t.left(5)


i = 0
while i < 72:
	side()
	t.right(10)
	t.write("Alex", font=("Arial", 40))
	i += 1

time.sleep(1000)
