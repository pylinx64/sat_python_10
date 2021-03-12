import random

while True:

	print("$$$		Хотите сыграть?!		$$$")

	number_random = random.randint(1, 10)

	number_player = input("Введите 'выигрышное' число -> ")

	if str(number_random) == number_player:
		print("$$$ Вы выиграли! $$$")
	elif number_player == 'q':
		print("Игра остановлена.")
		break
	else:
		print("@@@ Вы проиграли! @@@")
