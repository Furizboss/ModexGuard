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
            await ctx.send('Отметьте участник для бана как аргумент')
        else:
            await member.ban(reason=reason)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, member:discord.Member = None, reason = None):
        if member == None:
            await ctx.send('Отметьте участник для бана как аргумент')
        else:
            await member.kick(reason=reason)
            await ctx.send(f'{member} был выгнан с сервера!')