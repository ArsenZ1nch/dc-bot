import discord
from discord.ext import commands


class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, user_mention:discord.Member, *, reason:str=None):
        if user_mention == ctx.author:
            await ctx.send("You can't kick yourself")
            return

        if user_mention == self.bot.user:
            bait_embed = discord.Embed(
                title='I can\'t ban myself!',
                description='You can remove me from this server ***[HERE](https://youtu.be/dQw4w9WgXcQ)***'
            )
            await ctx.send(embed=bait_embed)
            return

        if not ctx.author.guild_permissions.ban_members:
            await ctx.send(f"You are not allowed to kick")
            return

        if user_mention.top_role >= ctx.author.top_role and ctx.author != ctx.guild.owner or user_mention == ctx.guild.owner:
            await ctx.send("You are not allowed to kick this user")
            return


        kick_embed = discord.Embed(
            title='Kick Report',
            color=discord.Color.from_rgb(143, 0, 0)
        )
        kick_embed.set_thumbnail(
            url=user_mention.avatar_url
        )
        kick_embed.set_image(
            url='https://preview.redd.it/5eh64qnzelg51.jpg?width=640&crop=smart&auto=webp&s=9567ed3015be1358d4bf251961cb44dfef62f8d2'
        )
        kick_embed.add_field(name='Received the Kick', value=user_mention)
        kick_embed.add_field(name='Reason', value=reason or 'Unknown')
        kick_embed.set_footer(text=f'Kick issued by {ctx.author}')

        dm_kick_embed = kick_embed.copy()
        dm_kick_embed.description = f'You have been **kicked** from **{ctx.guild}!**'

        await user_mention.send(embed=dm_kick_embed)
        await ctx.guild.kick(user=user_mention, reason=reason)
        await ctx.send(embed=kick_embed)


    @commands.command()
    async def ban(self, ctx, user_mention:discord.Member, *, reason:str=None):
        if user_mention == ctx.author:
            await ctx.send("You can't ban yourself")
            return

        if user_mention == self.bot.user:
            bait_embed = discord.Embed(
                title='I can\'t ban myself!',
                description='You can remove me from this server ***[HERE](https://youtu.be/dQw4w9WgXcQ)***'
            )
            await ctx.send(embed=bait_embed)
            return

        if not ctx.author.guild_permissions.ban_members:
            await ctx.send(f"You are not allowed to ban!")
            return

        if user_mention.top_role >= ctx.author.top_role and ctx.author != ctx.guild.owner or user_mention == ctx.guild.owner:
            await ctx.send("You are not allowed to ban this user!")
            return


        ban_embed = discord.Embed(
            title='Ban Report',
            color=discord.Color.from_rgb(143, 0, 0)
        )
        ban_embed.set_thumbnail(
            url=user_mention.avatar_url
        )
        ban_embed.set_image(
            url='https://preview.redd.it/5eh64qnzelg51.jpg?width=640&crop=smart&auto=webp&s=9567ed3015be1358d4bf251961cb44dfef62f8d2'
        )
        ban_embed.add_field(name='Received the Ban', value=user_mention.mention)
        ban_embed.add_field(name='Reason', value=reason or 'Unknown')
        ban_embed.set_footer(text=f'Ban issued by {ctx.author}')

        dm_ban_embed = ban_embed.copy()
        dm_ban_embed.description = f'You have been **banned** from **{ctx.guild}!**'

        await user_mention.send(embed=ban_embed)
        await ctx.guild.ban(user=user_mention, reason=reason, delete_message_days=0)
        await ctx.send(embed=ban_embed)


    @commands.command()
    async def unban(self, ctx, user_mention:str, *, reason:str=None):
        if not ctx.author.guild_permissions.ban_members:
            await ctx.send(f"You are not allowed to unban")
            return

        if not user_mention.startswith('<@') and not user_mention.endswith('>'):
            return

        for ban in await ctx.guild.bans():
            if str(ban.user.id) in user_mention:
                await ctx.guild.unban(ban.user, reason=reason)

                unban_embed = discord.Embed(
                    title='Unban Report',
                    color=discord.Color.from_rgb(108, 79, 255)
                )
                unban_embed.set_thumbnail(url=ban.user.avatar_url)
                unban_embed.set_image(url='https://media3.giphy.com/media/ZE5DmCqNMr3yDXq1Zu/source.gif')
                unban_embed.add_field(name='Got Unbanned', value=user_mention)
                unban_embed.add_field(name='Unban Reason', value=reason) if reason else None
                unban_embed.set_footer(text=f'Unbanned by {ctx.author}')

                await ctx.send(embed=unban_embed)

                try:
                    invitation = await ctx.channel.create_invite(max_age=0, max_uses=1)
                    await ban.user.send(invitation)
                except discord.Forbidden:
                    await invitation.delete()
                return

        await ctx.send('No such banned user')


def setup(bot):
    bot.add_cog(Moderator(bot))
