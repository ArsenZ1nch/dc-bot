import json
import discord
from discord.ext import commands

PREFIX = '!'
PREFIX_LENGTH = len(PREFIX)

bot = commands.Bot(command_prefix=PREFIX)
bot.load_extension('extensions.moderator')
bot.load_extension('extensions.info')


@bot.event
async def on_ready():
    print(f'Ready')



    guild = bot.get_guild(746080721600512081)
    bot_spectator = guild.get_role(751380803967254589)
    message = f"Hello! React to this message with 🎥 to be able to spectate my development in {bot.get_channel(746080722942427206).mention}"

    reaction_roles_dict = {
        '🎥': bot_spectator
    }

    bot.loop.create_task(
        new_reaction_role(channel_id=751735282260246529, message_text=message,
                          reaction_roles_dict=reaction_roles_dict)
    )





@bot.event
async def on_member_ban(guild, user):
    for ban in await guild.bans():
        if ban.user != user:
            continue

        ban_embed = discord.Embed(
            title='Ban Report',
            color=discord.Color.from_rgb(143, 0, 0)
        )
        ban_embed.set_thumbnail(
            url=user.avatar_url
        )
        ban_embed.set_image(
            url='https://preview.redd.it/5eh64qnzelg51.jpg?width=640&crop=smart&auto=webp&s=9567ed3015be1358d4bf251961cb44dfef62f8d2'
        )
        ban_embed.add_field(name='Received the Ban', value=user.mention)
        ban_embed.add_field(name='Reason', value=ban.reason or 'Unknown')

        await guild.system_channel.send(embed=ban_embed)


@bot.event
async def on_member_unban(guild, user):
    unban_embed = discord.Embed(
        title='Unban Report',
        color=discord.Color.from_rgb(108, 79, 255)
    )
    unban_embed.set_thumbnail(url=user.avatar_url)
    unban_embed.set_image(url='https://media3.giphy.com/media/ZE5DmCqNMr3yDXq1Zu/source.gif')
    unban_embed.add_field(name='Got Unbanned', value=user.mention)

    await guild.system_channel.send(embed=unban_embed)


@bot.event
async def on_disconnect():
    print('Disconnected from Discord!')

    @bot.event
    async def on_connect():
        print('Connected to Discord!')


bot.run('NzQ2MDcxNzQ5NzU3NzYzNjk2.Xz6_dg.yqKgAdT_zWe6TZsJDn9GyNj8BHg')
