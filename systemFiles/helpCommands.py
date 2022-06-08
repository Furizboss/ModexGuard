import discord
from discord.ext import commands
from config import settings

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['help', 'помощь'])
    async def _help(self, ctx, helpCommand=None):
        prefix = settings['prefix']
        botId = discord.utils.get(ctx.guild.members, id = settings['id'])

        # общий help
        if helpCommand == None or helpCommand == 'help':
            embed = discord.Embed(
                description=f'**Информация о командах:**\n'
                            f'\nВы можете получить детальную справку по каждой команде\n'
                            f'Например: `{prefix}help serverinfo`\n'
                            f'\n:bar_chart: Информация\n'
                            f'`{prefix}help` `{prefix}serverinfo` `{prefix}userinfo` `{prefix}roles` `{prefix}avatar`'
                            f'\n:toolbox: Модерация\n'
                            f'`{prefix}ban` `{prefix}kick` `{prefix}clear` `{prefix}slowmode`'
                            f'\n:joystick: Развлечение\n'
                            f'`{prefix}coin` `{prefix}howdy` `{prefix}ben` `{prefix}nsfw` `{prefix}ping`'
                            f'\n⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)
        

        # помощь раздела информации
        elif helpCommand == 'serverinfo' or helpCommand == 'server':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}serverinfo`:**\n'
                            f'\nКоманда позволяет получить информацию о сервере\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}server`\n'
                            f'`{prefix}serverinfo`'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)

        elif helpCommand == 'userinfo' or helpCommand == 'user':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}userinfo`:**\n'
                            f'\nКоманда позволяет получить информацию о пользователе\n'
                            f'\nКоманда приминяется как с аргументом так и без:\n'
                            f'`{prefix}user`\n'
                            f'`{prefix}user <@пользователь>`\n'
                            f'`{prefix}userinfo`\n'
                            f'`{prefix}userinfo <@пользователь>`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)

        elif helpCommand == 'roles' or helpCommand == 'myroles':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}roles`:**\n'
                            f'\nКоманда позволяет получить информацию о всех ролях пользователя\n'
                            f'\nКоманда приминяется как с аргументом так и без:\n'
                            f'`{prefix}myroles`\n'
                            f'`{prefix}roles`\n'
                            f'`{prefix}roles <@пользователь>`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)

        elif helpCommand == 'avatar':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}avatar`:**\n'
                            f'\nКоманда позволяет получить аватарку пользователя\n'
                            f'\nКоманда приминяется как с аргументом так и без:\n'
                            f'`{prefix}avatar`\n'
                            f'`{prefix}avatar <@пользователь>`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)


        # помощь раздела развлечение
        elif helpCommand == 'coin':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}coin`:**\n'
                            f'\nКоманда позволяет подкинуть монетку\n'
                            f'\nКоманда приминяется без аргумента:\n'
                            f'`{prefix}coin`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)

        elif helpCommand == 'howdy' or helpCommand == 'howdyho':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}howdy`:**\n'
                            f'\nКоманда позволяет получить рандомное фото Хауди Хо\n'
                            f'\nКоманда приминяется без аргумента:\n'
                            f'`{prefix}howdy`\n'
                            f'`{prefix}howdyho`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)

        elif helpCommand == 'ben':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}ben`:**\n'
                            f'\nКоманда позволяет получить ответ на вопрос от Бена\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}ben <вопрос>`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)

        elif helpCommand == 'nsfw':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}nsfw`:**\n'
                            f'\nКоманда позволяет получить nsfw аниме фото\n'
                            f':warning: Команду можно применить только в NSFW чатах\n'
                            f'\nКоманда приминяется без аргумента:\n'
                            f'`{prefix}nsfw`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)

        elif helpCommand == 'ping':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}pong`:**\n'
                            f'\nКоманда позволяет получить "Pong"\n'
                            f'\nКоманда приминяется без аргумента:\n'
                            f'`{prefix}ping`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)


        # помощь раздела Модерирование
        elif helpCommand == 'ban':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}ban`:**\n'
                            f'\nКоманда позволяет забанить пользователя на сервере\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}ban <участник>`\n'
                            f'`{prefix}ban <участник> <причина>`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)

        elif helpCommand == 'kick':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}kick`:**\n'
                            f'\nКоманда позволяет увыгнать пользователя с сервера\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}kick <участник>`\n'
                            f'`{prefix}kick <участник> <причина>`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)
            
        elif helpCommand == 'cls' or helpCommand == 'clear':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}clear`:**\n'
                            f'\nКоманда позволяет удалить сообщения в канале\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}cls <количество сообщений>`\n'
                            f'`{prefix}clear <количество сообщений>`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)

        elif helpCommand == 'slowmode':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}slowmode`:**\n'
                            f'\nКоманда позволяет установить медленный режим в канале\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}slowmode < время задержки >`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url=botId.avatar_url)
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/0hDpXRf/00.png")
            await ctx.send(embed=embed)

        else:
            await ctx.send('Упс.. Я не могу найти информацию о такой команде')
            print(helpCommand)