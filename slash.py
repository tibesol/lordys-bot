
import discord
from discord import app_commands
from discord.ext import commands

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            synced = await self.bot.tree.sync()
            print(f"Synced {len(synced)} slash commands")
        except Exception as e:
            print(f"Failed to sync slash commands: {e}")

    @app_commands.command(name="hello", description="Say hello")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello there! I'm Carl Purple 💜")

async def setup(bot):
    await bot.add_cog(Slash(bot))
