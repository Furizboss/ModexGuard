import discord
from discord.ext import commands

class Moder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['clear', 'cls'])
    @commands.has_permissions(manage_messages=True)
    async def _clear(self, ctx, amount=None):
        if amount == None:
            await ctx.send('Введите количество сообщений для очистки как аргумент')
        else:
            await ctx.channel.purge(limit=int(amount))

    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member = None, reason = None):
        if member == None:
            await ctx.send('Отметьте участника для бана как аргумент')
        else:
            await member.ban(reason=reason)


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member = None, reason = None):
        if member == None:
            await ctx.send('Отметьте участника для изгнания как аргумент')
        else:
            await member.kick(reason=reason)
            await ctx.send(f'{member} был выгнан с сервера!')


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds:int = None):
        if seconds == None:
            await ctx.send('Отметьте время медленого режима как аргумент')
        else:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send(f"Задержка в этом канале установленно на {seconds} секунд!")