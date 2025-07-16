
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.environ("DISCORD_TOKEN")
print("TOKEN USE:" TOKEN[:10]+"MTM5NTAwNzM0MjU0MTUzNzQyMw.GzP48T.OT6t9HSEQjmzxQg24EkenQUjEIlhJZdKLhBgZQ")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Import cogs
initial_extensions = ['cogs.moderation', 'cogs.general', 'cogs.slash']

for ext in initial_extensions:
    bot.load_extension(ext)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(TOKEN)
