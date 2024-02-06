import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
bot = commands.Bot(
    intents=intents
)

@bot.event
async def on_ready():
    print(f"{bot.user} On ready!!")

bot.load_extensions(
    "cogs.minesweeper",
    store=False
)

bot.run(TOKEN)