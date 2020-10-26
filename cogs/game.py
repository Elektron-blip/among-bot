import os
import discord
from discord.ext import commands
from main import logWebhook


class Game(commands.Cog):

    def __init__(self, client):

        self.client = client

    @commands.command(brief='Creates a channel with the name as the game code.', description='The bot creates a voice channel and renames it to the game code and gives the creator extra permissions in the channel.')
    async def create(self, ctx, code: str):
        if ctx.message.author.guild_permissions >= discord.Permissions(manage_channels=True) or ctx.guild.get_role(os.environ.get('MANAGER_ROLE_ID')) in ctx.message.author.roles:
            if ctx.message.author.voice is not None:
                if ctx.message.author.is_on_mobile() is False:
                    vc = await ctx.guild.create_voice_channel(name=code, overwrites=discord.PermissionOverwrite(mute_members=True, priority_speaker=True), category=ctx.guild.get_channel(os.environ.get('VOICE_CATEGORY')), reason=f'{ctx.message.author} created this channel.', bitrate=int(ctx.guild.bitrate_limit), user_limit=10)
                    await ctx.message.author.edit(nick=f'{ctx.message.author.display_name} (manager)', voice_channel=vc)
        else:
            await ctx.send('You don\'t satisfy one or more of these requirements:\n- User has either the manage_channel guild permission or has the manager role\n- User must be in a voice channel\n- User must be a logged in on anything but a phone or console')


def setup(client):
    client.add_cog(Game(client))