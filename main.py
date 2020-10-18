import discord
import os
from discord.ext import commands
import requests

client = commands.Bot(command_prefix=',', intents=discord.Intents.all())

logWebhook = discord.Webhook.from_url(
    url=os.environ.get('LOG_WEBHOOK_URL'), adapter=discord.RequestsWebhookAdapter())

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ.get('TOKEN'))
