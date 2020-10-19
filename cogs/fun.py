import discord
from discord.ext import commands
from main import logWebhook


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='The bot says what you want it to say.', description='The bot will just repeat whatever you throw at it. Simple really.')
    async def say(self, ctx, *, message: str):
        await ctx.message.delete()
        sentMessage = await ctx.send(content=message, allowed_mentions=discord.AllowedMentions.none())
        logWebhook.send(
            content=f'{ctx.message.author.mention} used me to say ```{message}``` in {ctx.channel.mention}. Click [here](<{sentMessage.jump_url}>) to go to that message.',allowed_mentions=discord.AllowedMentions.none())


def setup(client):
    client.add_cog(Fun(client))
