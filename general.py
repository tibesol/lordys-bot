
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def helpme(self, ctx):
        await ctx.send("Here's what I can do: !kick, !ban, !clear, !ping, /hello")

async def setup(bot):
    await bot.add_cog(General(bot))
