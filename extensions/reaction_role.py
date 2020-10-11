from discord.ext import commands


class ReactionRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        async def new_reaction_role(channel_id, message_text, reaction_roles_dict):
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

            @self.bot.event
            async def on_raw_reaction_add(payload):
                if payload.member == self.bot.user:
                    return

                if payload.message_id != reaction_role_message.id:
                    return

                for emoji, role in reaction_roles_dict.items():
                    if payload.emoji.name != emoji:
                        continue

                    await payload.member.add_roles(role)

            @self.bot.event
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

        guild = self.bot.get_guild(746080721600512081)
        bot_spectator = guild.get_role(751380803967254589)
        message = f"Hello! React to this message with 🎥 to be able to spectate my development in {self.bot.get_channel(746080722942427206).mention}"

        reaction_roles_dict = {
            '🎥': bot_spectator
        }

        self.bot.loop.create_task(
            new_reaction_role(channel_id=751735282260246529, message_text=message,
                                   reaction_roles_dict=reaction_roles_dict)
        )


def setup(bot):
    bot.add_cog(ReactionRole(bot))
