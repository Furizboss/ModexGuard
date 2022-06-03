import discord
from discord.ext import commands
from config import settings

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['help', 'помощь'])
    async def _help(self, ctx, helpCommand=None):
        prefix = settings['prefix']

        if helpCommand == None or helpCommand == 'help':
            embed = discord.Embed(
                description=f'**Информация о командах:**\n'
                            f'\nВы можете получить детальную справку по каждой команде\n'
                            f'Например: `{prefix}help serverinfo`\n'
                            f'\n:bar_chart: Информация\n'
                            f'`{prefix}help` `{prefix}serverinfo` `{prefix}userinfo` `{prefix}roles`'
                            f'\n:joystick: Развлечение\n'
                            f'`{prefix}coin` `{prefix}howdy`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url="https://i.ibb.co/60CZrcf/1.png")
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/jbMm1Ff/19a97a99b40d6ec9efc75a3a3a17b632.png")
            await ctx.send(embed=embed)
        
        elif helpCommand == 'serverinfo' or helpCommand == 'server':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}serverinfo`:**\n'
                            f'\nКоманда позволяет получить информацию о сервере\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}server`\n'
                            f'`{prefix}serverinfo`'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url="https://i.ibb.co/60CZrcf/1.png")
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/jbMm1Ff/19a97a99b40d6ec9efc75a3a3a17b632.png")
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
            embed.set_thumbnail(url="https://i.ibb.co/60CZrcf/1.png")
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/jbMm1Ff/19a97a99b40d6ec9efc75a3a3a17b632.png")
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
            embed.set_thumbnail(url="https://i.ibb.co/60CZrcf/1.png")
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/jbMm1Ff/19a97a99b40d6ec9efc75a3a3a17b632.png")
            await ctx.send(embed=embed)

        elif helpCommand == 'coin':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}coin`:**\n'
                            f'\nКоманда позволяет подкинуть монетку\n'
                            f'\nКоманда приминяется без аргумента:\n'
                            f'`{prefix}coin`\n'
                            f'⠀',
                color=ctx.author.color)
            embed.set_thumbnail(url="https://i.ibb.co/60CZrcf/1.png")
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/jbMm1Ff/19a97a99b40d6ec9efc75a3a3a17b632.png")
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
            embed.set_thumbnail(url="https://i.ibb.co/60CZrcf/1.png")
            embed.set_footer(text=' by illia841 ©', icon_url = "https://i.ibb.co/jbMm1Ff/19a97a99b40d6ec9efc75a3a3a17b632.png")
            await ctx.send(embed=embed)

        else:
            await ctx.send('Упс.. Я не могу найти информацию о такой команде')
            print(helpCommand)