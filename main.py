import discord
from discord.ext import commands
import json
import os

with open("database//database.json") as database:
    bot_guilds = json.load(database)["Guilds"]


async def prefix_definer(bot, message):
    prefix = bot_guilds[str(message.guild.id)]['Prefix'] if str(message.guild.id) in bot_guilds.keys() else '!'
    return prefix


INTENTS = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix_definer, intents=INTENTS)

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
