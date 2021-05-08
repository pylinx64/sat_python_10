import discord
import random
import asyncio	


# это для ответа "как дела"
message_1 = ['норм', 'ненорм', 'а у тебя?', 'класс']

# создаем бота
client = discord.Client()

# ловим событие "сообщение"
@client.event
async def on_message(message):
	# проверка чтобы ббот не отвечал себе же
	if message.author == client.user:
		return
	
	# проверка чтобы отвечал только людям
	if message.author.bot == True:
		return
		
	# печатаем в консоль сообщение и автора
	print(message.author, message.content) 
	
	if message.content == 'привет':
		# отправляет сообщений
		await message.channel.send('Ни хао')
	
	elif message.content == '$casino':
		await message.channel.send('> // Запуск казино //')
		for x in range(10):
			msg = await message.channel.send(x * 10)
			await asyncio.sleep(1)
			await msg.delete()
			
	
	elif message.content == 'как дела':
		await message.channel.send(random.choice(message_1))
	
	else:
		await message.channel.send('Я тебя не понял')
	
# запуск бота
client.run('ODM1MTgxMTU1NjU3MTg3NDA4.YILtEA.2PZXgKGYWpN_MQ1jNKlauzSrQnQ')
