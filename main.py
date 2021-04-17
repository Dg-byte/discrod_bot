import conf
import discord
from discord.ext import commands
import img_handler as imhl
import os
#
#
#
##Настраиваем расширенный доступ Intesnese
intense = discord.Intents.default()
#intense.members = True
#
##Создаем подключение бота
#client = discord.Client(intents = intense)
#
#@client.event
#async def on_message(message):
#    # <Message 
#    # id=825338292228718603 
#    # channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539> 
#    # type=<MessageType.default: 0>
#    # author=<Member id=307383433036824579 name='dimaditriy' discriminator='1518' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>> 
#    # flags=<MessageFlags value=0>>
#
#    # Отправлятор является самим ботом 
#    if message.author == client.user:
#        return
#    # Отправлятор является другим ботом
#    if message.author.bot:
#        return
#
#
## Задаем канал для бота [Мой канал dmitri-bot]
#    if message.channel.id == 825309140045529108:
#        #Ответить пользователю в формате "Hello, {user.name} - your message {user.content}"
#        msg = None
#        # Отправляем сообщение в канал Channel используя метод send
#     
#        command = message.content.split(" ", maxsplit=1)
#        #1. /hello - просто сообщение
#        if message.content == "/hello":
#            msg = f'Hello, {message.author.name}. I am {client.user.name}'
#        
#        #2. /about_me - сообщение  пользователю по его параметрам id/name (если есть ник то добавить "твой ник nick")        
#        elif message.content == "/about_me":
#            msg = f'Your id is {message.author.id}'
#            if message.author.nick:
#                msg=f'and your nick is {message.author.nick}'
#
#                
#        #3. /repeat [] - повторить за пользователем 
#        elif command[0] == "/repeat":
#            msg = command[1]
#
#        #4. /get_member {id/name} - берём инфу по пользователю по типу about_me {если пусто != обрабатываем ошибку}
#        elif command[0] == "/get_member":
#            name = command[1]
#            for _, member in list(enumerate(message.author.guild.members)):
#                if name == member.name or name == member.id:
#                    msg = f'His username is {member.name} {f"and his nick is {member.nick}" if member.nick else ""} - {member.id}' 
#            if name == "":
#                msg = f'There is no one who has that id or name'
#
#        #5. /get_members  - список всех пользователй по "1. name {nick} id"       *(через webhook)
#        elif message.content == "/get_members":
#            msg = ""
#            if message.author.guild.name == "Bots":
#                for idx, member in list(enumerate(message.author.guild.members)):
#                    msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else "" } - {member.id}\n'
#
#        #6. /get_сhannels  - список всех каналов категории Ботсы по "1. name id" *(через webhook)
#        elif message.content == "/get_channels":
#            msg = ""
#            if message.author.guild.name == "Bots":
#                for idx, channel in list(enumerate(message.author.guild.channels)):
#                    msg += f'{idx+1}. {channel.name} - {channel.id}\n'
#                    
       #7. /goto {id/name} - подключение бота в определенный канал (по умолчанию бот подключен в свой канал)          
#      elif command[0] == "/goto":
#          name_channel = command[1]
#          for _, channel in list(enumerate(message.author.guild.channels)):
#              if name_channel == channel.name or int(name_channel) == channel.id:
#                  message.channel.id = name_channel
#                  print("Ok")
#                  msg = f"Channel is changed"
#                  break
#              else: 
#                  msg = f"channel doesn't exist"
#                     
#
#        # Отправляем сообщение если оно есть
#        if msg != None:
#            await message.channel.send(msg)
#client.run(conf.bot_token)

#Объявляем бота с префиксом и расширенными правами
bot = commands.Bot(command_prefix = "!", intents = intense)

channel = 825309140045529108

@bot.command(name= "get_member")
async def command_get_member(ctx, member: discord.Member=None):
    msg = None
    global channel
    if ctx.channel.id == channel:

        if member:
            msg = f'Member {member.name} {"({member.nick})" if member.nick else ""} - {member.id}'

        if msg == None:
            msg = "error"

        await ctx.channel.send(msg)


@bot.command(name= "mk")
async def command_mk(ctx, fighter1: discord.Member=None, fighter2: discord.Member=None):
    msg = None
    global channel
    if ctx.channel.id == channel:

        if fighter1 and fighter2:
            #print(fighter1.avatar_url, fighter2.avatar_url)
            #Передаем ответ разработчику
            await imhl.vs_create(fighter1.avatar_url, fighter2.avatar_url)

            #msg = f'The first fighter is {fighter1.name}, the second fighter is {fighter2.name}\n Fight!'
            await ctx.channel.send(file=discord.File(os.path.join("./img/result.png")))

        if msg == None:
            msg = "error"

    #await ctx.channel.send(msg)






#@bot.command(name = "hello")
#async def command_hello(ctx, *args): 
#
#    print(ctx)
#    if ctx.channel.id == 825309140045529108:
#        msg= f'Hello to you! You said: "{" ".join(args)} "'
#        await ctx.channel.send(msg)
#
#@bot.command(name= "about_me")
#async def command_about_me(ctx, *args):
#
#    
#    if ctx.channel.id == 825309140045529108:
#
#        msg = f'Your id is {ctx.author.id}'
#        if ctx.author.nick:
#            msg = f'and your nick is {ctx.author.nick}'
#    await ctx.channel.send(msg)
#
#@bot.command(name= "repeat")
#async def command_repeat(ctx, *args):
#
#    
#    if ctx.channel.id == 825309140045529108:
#        if args != "":
#            msg = f'{" ".join(args)}'
#        else:
#            msg = f"You didn't write anything. Nothing to repeat"
#    await ctx.channel.send(msg)
#
#@bot.command(name = "get_members")
#async def command_get_members(ctx, *args):
#
#    if ctx.channel.id == 825309140045529108:
#        msg = ""        
#        if ctx.author.guild.name == "Bots":
#            
#            for idx, member in list(enumerate(ctx.author.guild.members)):
#                print(idx)
#                msg += f'{idx+1}. {member.name} {f"[{member.nick}]" if member.nick else ""} - {member.id}\n'
#    await ctx.channel.send(msg)
        #            msg = ""
#            if message.author.guild.name == "Bots":
#                for idx, member in list(enumerate(message.author.guild.members)):
#                    msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else "" } - {member.id}\n'


bot.run(conf.bot_token)