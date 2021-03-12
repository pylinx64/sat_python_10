'''
try:
	a = input('Введите число ')
	print(int(a) * 100)
except:
	print('Error')
'''

import colorama, tqdm, time, random
from colorama import Fore

for i in tqdm.tqdm(range(101), colour='cyan', desc='Loading game', ascii=True):
	time.sleep(0.01)

colorama.init()
print(Fore.CYAN + 'Hello wolrd')
