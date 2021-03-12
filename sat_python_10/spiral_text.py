import turtle

colors = ['#DD87DC', '#DDD687', '#87D5DD', '#87DD9C', '#DD8E87']
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(10)

text = turtle.textinput('Подсказка 1', 'Подсказка 2')

for i in range(1000):
	t.pencolor(colors[i%5])
	t.penup()
	t.forward(i * 40)
	t.pendown()
	t.write(text, font=('Arial Bold', int((i + 4) / 4), 'bold'))
	t.left(72)
