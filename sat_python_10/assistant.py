import pyttsx3
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from datetime import datetime, date, time


# настройки бота
tts = pyttsx3.init()
tts.setProperty('rate', 500)		# скорость разговора


# Команды для бота
def say_bot(msg):
	'''Разговор для бота'''
	tts.say(msg)
	print(msg)
	tts.runAndWait()
	
def google_search(msg):
	reg_ex = re.search('загугли (.*)', msg)
	search_for = msg.split("загугли",1)[1] 
	url = 'https://www.google.com/'
	if reg_ex:
		subgoogle = reg_ex.group(1)
		url = url + 'r/' + subgoogle
	driver = webdriver.Firefox('C:\\Users\\Admin\\Documents\\')
	driver.get('http://www.google.com')
	search = driver.find_element_by_name('q')
	search.send_keys(str(search_for))
	search.send_keys(Keys.RETURN)


# Основной код ассистента
NAME = input('Введите имя: ') 	# запоминает имя админа
say_bot('Привет, ' + NAME)
say_bot('Меня зовут Как-нибудь-бот')# для разговора используйте эту команду
while True:
	say_bot('Введите команду/слово: ')
	command = input('-> ')
	if command == 'как дела?':
		say_bot('Норм, а у тебя?')
	elif command == 'погода?':
		say_bot('Солнечно')
	elif command == 'кто такой робот?':
		say_bot('1000111001')
	elif command == 'открой интернет':
		webbrowser.open('www.youtube.com')
	elif 'загугли' in command:
		say_bot('загуглил')
		google_search(command)
	elif command == 'время':
		time_check = datetime.now()
		h = time_check.hour
		m = time_check.minute
		say_bot(str(h) + ':'+ str(m))
	else:
		say_bot('Я ВАС НЕ РОЗУМИЮ')
