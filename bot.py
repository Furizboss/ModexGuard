import discord
from discord.ext import commands
from config import settings
from asyncio import sleep

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Готов к труду и обороне")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="гей порно"))
    await sleep(5)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="хуйню"))
    await sleep(5)


@bot.command()
async def help(ctx):
    emb = discord.Embed(color=ctx.author.color, title="Информация о командах")

    emb.add_field(name=f"{settings['prefix']}help: ", value="Информация", inline=False)
    emb.add_field(name=f"{settings['prefix']}serverinfo: ", value="Информация о сервере", inline=False)
    emb.add_field(name=f"{settings['prefix']}myroles: ", value="Узнать свои роли", inline=False)

    await ctx.send(embed=emb)


@bot.command(aliases=['serverinfo', 'server'])
async def _serverinfo(ctx):
    embed = discord.Embed(
        description=f'**Информация о сервере** **{ctx.guild.name}**\n'
                    f'\n**Участники:**\n'
                    f'Всего: **{ctx.guild.member_count}**\n'
                    f'\n**Каналы:**\n'
                    f':speech_balloon: Текствые: **{len(ctx.guild.text_channels)}**\n'
                    f':mega: Голосовые: **{len(ctx.guild.voice_channels)}**\n'
                    f':books: Категории: **{len(ctx.guild.categories)}**\n'
                    f'\n**Владелец:**\n'
                    f'{ctx.guild.owner}\n'
                    f'\n**Уровень проверки:**\n'
                    f'{ctx.guild.verification_level}\n'
                    f'**Дата создания:**\n{ctx.guild.created_at.strftime("%d.%m.%Y")}\n',
        color=ctx.author.color, )
    embed.set_footer(text=f'ID: {ctx.guild.id}')
    embed.set_thumbnail(url=str(ctx.guild.icon_url))
    await ctx.send(embed=embed)


@bot.command(aliases=['myroles', 'roles'])
async def _roles(ctx):
    member = ctx.message.author
    member_roles = member.roles
    x = ''
    for i in member_roles:
        element = str(i)
        element = element.replace('@', '')
        result = f'@{element}'
        x += f' - `{result}` -'

    embed = discord.Embed(
        description=f"{member.mention} список твоих ролей:\n\n{x}",
        color=ctx.author.color, )
    embed.set_thumbnail(url=str(ctx.message.author.avatar_url))
    await ctx.send(embed=embed)


bot.run(settings['token'])
