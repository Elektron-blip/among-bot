import discord
import os
from discord.ext import commands
from main import logWebhook


class Game(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Changes the name of the game channel to whatever you specify.')
    async def room(self, ctx, code: str):
        if ctx.message.author.guild_permissions >= discord.Permissions(manage_guild=True) or commands.has_role(os.environ.get('MANAGER_ROLE_ID')):
            if ctx.message.author.voice.channel is not None:
                await ctx.message.author.voice.channel.edit(name=code.upper(), reason=f'{ctx.message.author} changed the room code.')
                await ctx.send(f'I have changed the name of your voice channel to {code.upper()}')
            else:
                await ctx.send('You need to be in a voice channel to use this command.')
        else:
            await ctx.send(f'You dont have the neccessary permissions to run this command. (You will need either MANAGE_GUILD permissions or the manager role to be able to use this command)')

    @commands.command(brief='Rests the name of the voice channel.')
    async def reset(self, ctx):
        if ctx.message.author.guild_permissions >= discord.Permissions(manage_guild=True) or commands.has_role(os.environ.get('MANAGER_ROLE_ID')):
            if ctx.message.author.voice is not None:
                await ctx.message.author.voice.channel.edit(name='game-chat', reason=f'{ctx.message.author} reset the room name.')
                await ctx.send(f'I have changed the name of your voice channel to `game-chat`')
            else:
                await ctx.send('You need to be in a voice channel to use this command.')
        else:
            await ctx.send(f'You dont have the neccessary permissions to run this command. (You will need either MANAGE_GUILD permissions or the manager role to be able to use this command)')


def setup(client):
    client.add_cog(Game(client))
