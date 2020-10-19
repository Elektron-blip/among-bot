import discord
from main import logWebhook
from discord.ext import commands

class Error(commands.Cog):

    def __init__(self,client):
        self.client=client
        self.logWebhook=logWebhook

    @commands.Cog.listener()
    async def on_error(self,error):
        print(error)
        self.logWebhook.send(content=f'```console\n{error}\n```')

def setup(client):
    client.add_cog(Error(client))