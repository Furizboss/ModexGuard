import random
import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coin(self, ctx):
        x = random.randint(0, 1)
        if x == 0:
            value = 'Монетка летит... Выпадает **Орёл**'
        if x == 1:
            value = 'Монетка летит... Выпадает **Решка**'

        embed = discord.Embed(
            description=value,
            color=ctx.author.color)
        await ctx.send(embed=embed)


    @commands.command(aliases=['howdy', 'howdyho'])
    async def _howdy(self, ctx):
        imgUrl = [ "https://i.ibb.co/Rykx1ZJ/1.png", "https://i.ibb.co/FWqhmy5/2.jpg", "https://i.ibb.co/phhGPhk/3.jpg",
        "https://i.ibb.co/WnDD1z7/4.jpg", "https://i.ibb.co/pX63w3Q/5.jpg", "https://i.ibb.co/tQh4Gx5/image.jpg",
        "https://i.ibb.co/Jqwyr5Y/9.png", "https://i.ibb.co/nf4VF9J/8.png", "https://i.ibb.co/J5qyBqY/7.png",
        "https://i.ibb.co/gMw4ss5/6.png"]

        emb = discord.Embed(title = "Howdy Ho", color=ctx.author.color)
        emb.set_image(url = random.choice(imgUrl))
        await ctx.send(embed = emb)
    

    @commands.command()
    async def ben(self, ctx, Question = None):
        answer = ['Yes', 'No', 'Ho-ho-ho']

        if Question == None:
            await ctx.send('Введите вопрос Бену как аргумент')
        else:
            embed = discord.Embed(
                description = f'**{random.choice(answer)}**',
                color=ctx.author.color)
            await ctx.send(embed=embed)

    
    @commands.command()
    @commands.is_nsfw()
    async def nsfw(self, ctx):
        imgUrl = [  "https://i.ibb.co/8mS69kM/image.jpg", "https://i.ibb.co/wMp7zk4/1.png", "https://i.ibb.co/zbWwnFL/2.jpg",
                    "https://i.ibb.co/XDmzYz2/3-1.jpg", "https://i.ibb.co/FxgxVfF/3.png", "https://i.ibb.co/nmjkQCR/4-2.jpg",
                    "https://i.ibb.co/1Xrh9qn/4.jpg", "https://i.ibb.co/QCCbwzy/5.jpg", "https://i.ibb.co/crYbNDb/5.png",
                    "https://i.ibb.co/ZzD4sqQ/6-1.jpg", "https://i.ibb.co/tqcn7B3/6.png", "https://i.ibb.co/d7c4jnF/7.jpg",
                    "https://i.ibb.co/PtpxhvR/8.png", "https://i.ibb.co/4jxyPpc/9.jpg", "https://i.ibb.co/j46wRw4/10.jpg",
                    "https://i.ibb.co/BGHVZjw/10.jpg", "https://i.ibb.co/CH82Cvc/11.jpg", "https://i.ibb.co/qddh7bX/12.jpg",
                    "https://i.ibb.co/Qdwxtvy/13-1.jpg", "https://i.ibb.co/ckP94qR/13.jpg", "https://i.ibb.co/8BMQqKB/14.jpg",
                    "https://i.ibb.co/SnCLsdY/16.jpg", "https://i.ibb.co/VgLBBFG/46-1.jpg", 'https://i.ibb.co/2n5kcn0/g-5.png',
                    'https://i.ibb.co/B3673Hr/g-6.png', 'https://i.ibb.co/MPDTQ88/g-7.png', 'https://i.ibb.co/QcdYsXX/g-8.png',
                    'https://i.ibb.co/Z1Sv2pB/g-2.jpg', 'https://i.ibb.co/Z6fW91D/g-1.gif', 'https://i.ibb.co/25XJ1Dx/g-9.png',
                    'https://i.ibb.co/XVMyVBs/g-11.png', 'https://i.ibb.co/G2qZmST/g-3.jpg', 'https://i.ibb.co/5THFPb9/g-12.png',
                    'https://i.ibb.co/RjZVXVC/g-1.png', 'https://i.ibb.co/B6cth7R/g-2.png', 'https://i.ibb.co/ZJnYLJM/g-3.png',
                    'https://i.ibb.co/pfqQCyc/g-1.jpg', 'https://i.ibb.co/L8q96J7/g-4.png'  ]
        
        
        emb = discord.Embed(title = ":underage: NSFW", color=ctx.author.color)
        emb.set_image(url = random.choice(imgUrl))
        await ctx.send(embed = emb)