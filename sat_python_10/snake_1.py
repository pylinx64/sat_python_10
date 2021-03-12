import time
import turtle
from random import randrange

# Экран для игры
screen = turtle.Screen()
# название 
screen.title('Snake with turtle module')
# задний фон
screen.bgcolor('orange')
# размер экрана
screen.setup(650, 650)
screen.tracer(0)

# рисуем границу
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-311, 311)
border.pendown()
border.goto(311, 311)
border.goto(311, -311)
border.goto(-311, -311)
border.goto(-311, 311)

# змейка
snake = []
for i in range(3):
	snake_segment = turtle.Turtle()
	# "форма" змейки
	snake_segment.shape('square')
	snake_segment.penup()
	if i > 0:
		snake_segment.color('gray')
	if i == 0:
		snake_segment.color('blue')
	# добавляем змейку в список
	snake.append(snake_segment)

# делаем еду
food = turtle.Turtle()
food.shape('circle')
food.penup()
# рандомная еда
food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))

# контроль змейки
screen.onkeypress(lambda: snake[0].setheading(90), 'Up')
screen.onkeypress(lambda: snake[0].setheading(270), 'Down')
screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
screen.onkeypress(lambda: snake[0].setheading(0), 'Right')
# слушает экран
screen.listen()


#------------------основной цикл программы---------------------
while True:
	
	# если змейка сьест яблоко
	if snake[0].distance(food) < 10:
		food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
		snake_segment = turtle.Turtle()
		snake_segment.shape('square')
		snake_segment.color('gray')
		snake_segment.penup()
		snake.append(snake_segment)


	# размещаем змейку
	for i in range(len(snake)-1, 0, -1):
		x = snake[i-1].xcor()
		y = snake[i-1].ycor()
		# размещает в точке х, у
		snake[i].goto(x, y)

	# движение головы
	snake[0].forward(20)
	# fps
	screen.update()
	
	# граница экрана
	x_cor = snake[0].xcor()
	y_cor = snake[0].ycor()
	# граница по х
	if x_cor > 300 or x_cor < -300:
		screen.bgcolor('red')
		break
	# граница по у
	if y_cor > 300 or y_cor < -300:
		screen.bgcolor('red')
		break
		

	
	
	# обновление экрана
	time.sleep(0.15)
	


# Шоб не вылетало
screen.mainloop()
screen.done()
