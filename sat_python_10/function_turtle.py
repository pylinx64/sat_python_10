import turtle

colors = ['#30FF57', '#6630FF', '#FF9A30']
t = turtle.Pen()


def side(i, m, p):
	# входные данные: i-угол, m-размер линии
	t.pencolor(colors[p])
	t.forward(m)
	t.left(i)

side(120, 100, 0) 	#линия под углом 120 и разммером 100
side(120, 100, 1) 
side(120, 100, 2) 

turtle.done()	# останавливает программу

