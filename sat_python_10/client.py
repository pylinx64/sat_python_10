# -*- coding: utf-8 -*-

import threading
import socket
import time
import random

import colorama
from colorama import Fore, Style
colorama.init()

def receving (name, sock, switch):
	while not switch:
		try:
			while True:
				# data - сообщение, addr - ip человека
				data, addr = sock.recvfrom(1024)
				# декодирует сообщение и печатает в ВАШУ консоль
				print('\n'+data.decode("utf-8"))
				time.sleep(0.2)
		except:
			# ничего не делает пока ошибка (напр, 404)
			pass

# Выкл, подкл
shutdown = False
join = False

# ваш ip, порт
host = socket.gethostbyname(socket.gethostname())
port = 0

# ip servera
server = ("192.168.31.20", 11719)

# сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

colors = [Fore.CYAN, Fore.MAGENTA, Fore.GREEN, Fore.RED]

name = input("$ name: ")
# разбивает на буквы
name = list(name)
# перебивает буквы и добовляет рандомный цвет
name = [random.choice(colors) + char + Fore.RESET for char in name]
	
# собирает буквы обратно
name = ''.join(name)

s.sendto((str("["+name+"] => join chat ")).encode("utf-8"), server)
time.sleep(0.2)

rT = threading.Thread(target = receving, args = ("RecvThread", s, shutdown))
rT.start()

while shutdown == False:
	try:
		print("["+name+"] > ", end='')
		
		print(Fore.GREEN, end='')
		message = input()
		message = Fore.GREEN+message+Fore.RESET
		print(Fore.RESET, end='')
		
		if message != "":
			 s.sendto(("["+name+"] > "+message).encode("utf-8"), server)
		time.sleep(0.2)
	except:
		s.sendto(("["+name+"] <= left chat ").encode("utf-8"), server)
		shutdown = True

rT.join()
s.close()
