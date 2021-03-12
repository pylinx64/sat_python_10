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
	screen.fill(white) 
	# ВЕСЬ КОД РИСОВАНИЯ
	
	# Обновить экран, чтобы увидеть рисунок
	pygame.display.flip()
	
	# Ограничить до 60 кадров
	clock.tick(60)

# Правильное выключение игры 
pygame.quit()
