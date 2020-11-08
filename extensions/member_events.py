import discord
from discord.ext import commands


class ModeratorEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        for ban in await guild.bans():
            if ban.user != user:
                continue

            ban_embed = discord.Embed(
                title='Ban Report',
                description=f'{user.mention} just got **banned!**',
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

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        unban_embed = discord.Embed(
            title='Unban Report',
            color=discord.Color.from_rgb(108, 79, 255)
        )
        unban_embed.set_thumbnail(url=user.avatar_url)
        unban_embed.set_image(url='https://media3.giphy.com/media/ZE5DmCqNMr3yDXq1Zu/source.gif')
        unban_embed.add_field(name='Got Unbanned', value=user.mention)

        await guild.system_channel.send(embed=unban_embed)


def setup(bot):
    bot.add_cog(ModeratorEvent(bot))
