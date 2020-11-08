import discord
from discord.ext import commands


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        ping = ctx.message
        pong = await ctx.send('pong')

        time1 = ping.created_at
        time2 = pong.created_at
        response_delta = int((time2 - time1).total_seconds()*1000)
        await pong.edit(content=f'It took `{response_delta} ms` for me to respond')

        if response_delta > 1000:
            print(f'Response Time Warning! {response_delta} ms response time detected on {ctx.guild or ctx.channel}!')
            await ctx.send("**Warning!** Response time of over **1** second detected! Please stop spamming commands, if you are doing so!")

            appinfo = await self.bot.application_info()
            await appinfo.owner.send(f'**Response Time Warning!** `{response_delta}` ms response time detected on `{ctx.guild or ctx.channel}`!')



    @commands.command('general-info')
    @commands.guild_only()
    async def general(self, ctx):
        name = ctx.guild.name
        icon = ctx.guild.icon_url
        gif_url = 'https://media3.giphy.com/media/ZE5DmCqNMr3yDXq1Zu/source.gif'
        owner = ctx.guild.owner
        member_count = ctx.guild.member_count
        channel_count = len(ctx.guild.text_channels) + len(ctx.guild.voice_channels)
        region = ctx.guild.region.name

        server_embed = discord.Embed(
            title=f'"{name}" Server Info:',
            description=ctx.guild.description,
            color=discord.Color.from_rgb(19, 214, 113)
        )

        server_embed.set_thumbnail(url=icon)
        server_embed.set_image(url=gif_url)
        server_embed.add_field(name='Owner', value=owner, inline=False)
        server_embed.add_field(name='Member Count', value=member_count, inline=True)
        server_embed.add_field(name='Channel Count', value=channel_count, inline=True)
        server_embed.add_field(name='Region', value=region.capitalize(), inline=False)

        await ctx.send(embed=server_embed)

    @commands.command()
    @commands.guild_only()
    async def members(self, ctx, *, type:str = None):
        image = 'https://media3.giphy.com/media/ZE5DmCqNMr3yDXq1Zu/source.gif'

        real_members = discord.Embed(
            title='Real Members:',
            color=discord.Color.from_rgb(19, 214, 113)
        )

        bots = discord.Embed(
            title='Bots',
            color=discord.Color.from_rgb(19, 214, 113)
        )

        for member in ctx.guild.members:
            display_name = member.display_name
            status = member.status

            if not member.bot:
                real_members.add_field(name=display_name, value=status, inline=False)
                continue
            bots.add_field(name=display_name, value=status, inline=False)

        real_members.set_image(url=image)
        bots.set_image(url=image)

        if type:
            type.lower()
            if type == 'bots':
                await ctx.send(embed=bots)
            elif type == 'real members' or type == 'real_members' or type == 'real':
                await ctx.send(embed=real_members)
            else:
                await ctx.send('This type is not valid')
                await ctx.send(embed=real_members)
                await ctx.send(embed=bots)
            return

        await ctx.send(embed=real_members)
        await ctx.send(embed=bots)


def setup(bot):
    bot.add_cog(ServerInfo(bot))
