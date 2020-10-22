import discord
from discord.ext import commands
import os

PREFIX = '!'
INTENTS = discord.Intents.all()

bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)

for file in os.listdir("extensions"):
    if not file.endswith(".py"):
        continue
    noExt_file = os.path.splitext(file)[0]
    bot.load_extension(f'extensions.{noExt_file}')


@bot.event
async def on_ready():
    print(f'Ready')


@bot.event
async def on_disconnect():
    print('Disconnected from Discord!')

    @bot.event
    async def on_connect():
        print('Connected to Discord!')


bot.run('NzQ2MDcxNzQ5NzU3NzYzNjk2.Xz6_dg.CIMfWbn2iMpyG-0-6kGez1eW1e8')
