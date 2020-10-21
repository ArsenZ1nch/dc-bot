import discord
from discord.ext import commands

PREFIX = '!'
INTENTS = discord.Intents.all()

bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)

bot.load_extension('extensions.reaction_role')
bot.load_extension('extensions.moderator')
bot.load_extension('extensions.info')
bot.load_extension('extensions.moderator_event')


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
