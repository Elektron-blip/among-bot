import discord
import os
from discord.ext import commands
import requests

client = commands.Bot(command_prefix=',')

for filename in os.listdir('./cogs'):
    if filename.endswith == '.py':
        client.load_extension(f'cogs.{filename[:-3]}')

logWebhook = discord.Webhook.from_url(url=os.environ.get('LOG_WEBHOOK_URL'), adapter=discord.RequestsWebhookAdapter())

client.run(os.environ.get('TOKEN'))
