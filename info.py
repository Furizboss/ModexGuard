import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['serverinfo', 'server'])
    async def _serverinfo(self, ctx):
        embed = discord.Embed(
            description=f'**{ctx.guild.name}**\n'
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

    @commands.command(aliases=['myroles', 'roles'])
    async def _roles(self, ctx):
        member = ctx.message.author
        member_roles = member.roles
        member_roles.pop(0)
        member_roles.reverse()
        x = ''
        for i in member_roles:
            element = str(i.id)
            result = f'<@&{element}>'
            if len(member_roles) <= 5:
                x += f'{result}\n'
            else:
                x += f'- {result} -'

        embed = discord.Embed(
            description=f"{member.mention} список твоих ролей:\n\n{x}",
            color=ctx.author.color, )
        embed.set_thumbnail(url=str(ctx.message.author.avatar_url))
        await ctx.send(embed=embed)
