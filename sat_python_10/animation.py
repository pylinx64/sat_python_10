import pygame

# инициализируем движок
pygame.init()

# цвета
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red   = ( 255,   0,   0)

# задает ширину и высоту экрана
size = [1280, 961]
screen = pygame.display.set_mode(size)

# установка заголовка окна
pygame.display.set_caption("Cool ITFriends Game")


# Останавливается в цикле, пока игрок не нажмет на кнопку закрыть
done = False

# Используется для FPS
clock = pygame.time.Clock()

#Начальная позиция прямоугольника
rect_x = 50
rect_y = 50

# Изменение скорости
rect_change_x = 5
rect_change_y = 5

#-------------------Основной цикл программы-------------------
while done == False:
	# ОБРАБОТКА ВСЕХ СОБЫТИЙ 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	# ОБРАБОТКА ВСЕХ СОБЫТИЙ 
	
	
	# ЛОГИКА ИГРЫ
	
	# ЛОГИКА ИГРЫ
	
	
	# ВЕСЬ КОД РИСОВАНИЯ
	# Очистить экран и установить белый фон
	screen.fill(black) 
	
	# Прямоугольник
	pygame.draw.rect(screen, white, [rect_x, rect_y, 50, 50])
	
	# Изменение скорости прямоугольника
	rect_x += rect_change_x
	rect_y += rect_change_y
	
	# Изменение направления
	if rect_y > 911 or rect_y < 0:
		rect_change_y = rect_change_y * -1
	
	if rect_x > 1230  or rect_x < 0:
		rect_change_x = rect_change_x * -1
	
	# ВЕСЬ КОД РИСОВАНИЯ
	
	# Обновить экран, чтобы увидеть рисунок
	pygame.display.flip()
	
	# Ограничить до 60 кадров
	clock.tick(60)

# Правильное выключение игры 
pygame.quit()

