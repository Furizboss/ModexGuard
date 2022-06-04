import discord
from discord.ext import commands
from asyncio import sleep
import random

from config import settings
from systemFiles.helpCommands import Help
from systemFiles.moderation import Moder
from systemFiles.info import Info
from systemFiles.fun import Fun

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Готов к труду и обороне")

    watch = ['гей порно', 'за клоунами', 'українські новини', 'хентай', 'секс оргию', ', но не здоровается']
    listen = ['хуйню', 'пердёж', 'молитвы', 'гімн України', 'пропаганду', 'власть', ', но не слышит']
    games = ['ролевые игры', 'войнушки', 'теракт 911', 'взрыв жопы', 'симмулятор козла', 'игры с дружком']
    stream = ['пропаганду', 'порнуху 24/7', 'Onlyfans', 'ебанину', ', но не Бустер']
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(watch)))
        await sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=random.choice(listen)))
        await sleep(5)
        await bot.change_presence(activity=discord.Game(name=random.choice(games)))
        await sleep(5)
        await bot.change_presence(activity=discord.Streaming(name=random.choice(stream), url='https://www.twitch.tv/rf'))
        await sleep(5)


bot.add_cog(Moder(bot))
bot.add_cog(Help(bot))
bot.add_cog(Info(bot))
bot.add_cog(Fun(bot))
bot.run(settings['token'])