list_veg = ["Баклажан", "Помидоры", "Огурец", "Сок", "Капуста"]

# Вывести весь список
print(list_veg)

print("Вывод списка не лучший способ ctrl + C и ctrl + V") # Выводит пустою строку

# Вывод списка "не лучший способ" ctrl + C и ctrl + V
print(list_veg[0])
print(list_veg[1])
print(list_veg[2])
print(list_veg[3])
print(list_veg[4])

print("Вывод списка с помощью цикла while")

# Вывод списка с помощью цикла while
i = 0
veg = len(list_veg)
while i < veg:
	print(list_veg[i])
	i = i + 1

print("Вывод списка с помощью цикла for in")

# Вывод списка с помощью цикла for in
for veg in list_veg:
	print(veg)
