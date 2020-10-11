import discord
from discord.ext import commands


class ReactionRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def new_reaction_role(self, channel_id, message_text, reaction_roles_dict):
        channel = self.bot.get_channel(channel_id)

        async for message in channel.history(limit=1):
            if message.content != message_text:
                reaction_role_message = await channel.send(message_text)

                for emoji, role in reaction_roles_dict.items():
                    await reaction_role_message.add_reaction(emoji)
                break

            reaction_role_message = message

            for reaction in reaction_role_message.reactions:
                async for user in reaction.users():
                    if user == self.bot.user:
                        continue

                    for emoji, role in reaction_roles_dict.items():
                        if reaction.emoji != emoji:
                            continue

                        if user not in channel.guild.members:
                            await reaction_role_message.remove_reaction(emoji, user)
                            continue

                        await user.add_roles(role)

        @commands.Cog.listener()
        async def on_raw_reaction_add(payload):
            if payload.member == self.bot.user:
                return

            if payload.message_id != reaction_role_message.id:
                return

            for emoji, role in reaction_roles_dict.items():
                if payload.emoji.name != emoji:
                    continue

                await payload.member.add_roles(role)

        @commands.Cog.listener()
        async def on_raw_reaction_remove(payload):
            if payload.user_id == self.bot.user.id:
                return

            if payload.message_id != reaction_role_message.id:
                return

            guild = self.bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)

            for emoji, role in reaction_roles_dict.items():
                if payload.emoji.name != emoji:
                    continue

                await member.remove_roles(role)
