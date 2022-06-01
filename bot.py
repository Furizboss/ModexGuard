import discord
from discord.ext import commands
from config import settings

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="гей порно"))
    print("Готов к труду и обороне")


@bot.command()
async def help(ctx):
    PREFIX = 's!'
    emb1 = discord.Embed(color=discord.Colour.from_rgb(0, 204, 255), title="Информация о командах")

    emb1.add_field(name=f"{PREFIX}help: ", value="Информация", inline=False)
    emb1.add_field(name="С тебя хватит ", value="С тебя хватит", inline=False)

    await ctx.send(embed=emb1)


bot.run(settings['token'])