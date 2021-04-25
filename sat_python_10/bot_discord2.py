import discord

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
    
    # отправляет сообщений
    await message.channel.send(message.content)
    
# запуск бота
client.run('ODMyODk5MzM5OTEwNTEyNjYw.YHqf9Q.CTZ03vSOjZoI9vSGFpDKkYqliPY')
