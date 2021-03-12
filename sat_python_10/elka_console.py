import sys
import random
# позволяет рисовать в консольке
w = sys.stdout.write
def t(n,s):
	# рисует вверх елки
	for i in range(n):
		for a in range(n-i):
			# заполняет пустое пространство
			w(" ")
		# конец елки слева
		w("[")
		for l in range(i<<1):
			if i == n-1:
				# рисует последний рядок
				w("_")
			elif random.randint(0, n) == i:
				w("O")
			else:
				# рисует елку
				w("~")
		# конец елки справа
		w("]")
		print("")
	
	# рисует низ елки
	for o in range(s):
		for i in range(n):
			w(" ")
		# бревно
		print("[]")

# 10 - кол-во иголок, 2 - кол-во бревен 
t(10, 2)
