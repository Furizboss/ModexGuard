import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Информация о сервере
    @commands.command(aliases=['serverinfo', 'server'])
    async def _serverinfo(self, ctx):
        bots = len(([member for member in ctx.guild.members if member.bot]))
        embed = discord.Embed(
            description=f'**{ctx.guild.name}**\n'
                        f'\n**Участники:**\n'
                        f':busts_in_silhouette: Всего: **{ctx.guild.member_count}**\n'
                        f':bust_in_silhouette: Людей: **{ctx.guild.member_count - bots}**\n'
                        f':robot: Ботов: **{bots}**\n'
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

    # Информация о ролях пользователя

    @commands.command(aliases=['myroles', 'roles'])
    async def _roles(self, ctx, member: discord.Member = None, guild: discord.Guild = None):
        if member == None:
            userPrefix = ctx.message.author
        else:
            userPrefix = member

        member_roles = userPrefix.roles
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
            description=f"{userPrefix.mention} список ролей:\n\n{x}",
            color=ctx.author.color, )
        embed.set_thumbnail(url=str(userPrefix.avatar_url))
        await ctx.send(embed=embed)

    # Информация о пользователя

    @commands.command(aliases=['user', 'userinfo'])
    async def _userinfo(self, ctx, member: discord.Member = None, guild: discord.Guild = None):
        if not member:
            member = ctx.message.author

        t = member.status
        if t == discord.Status.online:
            d = ":green_circle: В сети"
        if t == discord.Status.offline:
            d = ":black_circle: Не в сети"
        if t == discord.Status.idle:
            d = ":crescent_moon: Не активен"
        if t == discord.Status.dnd:
            d = ":no_entry: Не беспокоить"

        value1 = member.activity

        embed = discord.Embed(
            description=f'**Информация о пользователе**\n'
                        f'\n**Имя: **{member.display_name}\n'
                        f'**Статус: **{d}\n'
                        f'**Роль на сервере: **{member.top_role.mention}\n'
                        f'**Дата создания: **{member.created_at.strftime("%d.%m.%Y")}\n',
            color=ctx.author.color, )
        embed.set_footer(text=f'ID: {member.id}')
        embed.set_thumbnail(url=str(member.avatar_url))
        await ctx.send(embed=embed)

    # Аватарка пользователя

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member == None:
            userPrefix = ctx.message.author
        else:
            userPrefix = member

        emb = discord.Embed(
            title=f"Аватарка пользователя {userPrefix.display_name}", color=ctx.author.color)
        emb.set_image(url=str(userPrefix.avatar_url))
        await ctx.send(embed=emb)
