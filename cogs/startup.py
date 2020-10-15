import discord
from discord.ext import commands
from main import logWebhook

class Startup(commands.Cog):

    def __init__(self,client,logWebhook):
        self.client=client
        self.logWebhook=logWebhook

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as: {self.client.user}\nWith ID: {self.client.user.id}')
        self.logWebhook.send(conetnt=f'I have come online!')


def setup(client):
    client.add_cog(Startup(client))