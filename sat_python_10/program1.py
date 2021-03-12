import random

import time 

list1 = ["Minecraft", "NFS", "The Lust of Us", "GTA", "The Wither 3"]

print("-> gameKeys.net - выиграй игру на свой вкус")

money = input("-> Введите кол-во $: ")

money = int(money)

game = input("-> Хотите сыграть?(y / n): ")

if game == "y":
	random_game = random.choice(list1)
	print("-> Рулетка запущена...")
	print("-> 3..2..1..")
	print("-> Вы выиграли ", random_game)
elif game == "n":
	print("-> Стоп гейм")
	#break
else:
	print("-> Введите еще раз <-")
	
print(money)hg
