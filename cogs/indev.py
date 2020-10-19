import discord
import os
from discord.ext import commands

vcManager = {}


class Indev(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief='Lets a qualified person claim the voice channel', description='Lets a qualified person claim a channel and get perms for that specific channel. The bot also supresses everyone\'s mic when the owner of the channel mutes theirs.')
    async def claim(self, ctx):
        if ctx.message.author.guild_permissions >= discord.Permissions(manage_guild=True) or discord.utils.get(ctx.message.author.roles, id=os.environ.get('MANAGER_ROLE_ID')) != None:
            if ctx.message.author.voice != None:
                vcManager[ctx.message.author.voice] = ctx.message.author
                await ctx.send(f'You are the manager of {ctx.message.author.voice.channel.mention}.')
            else:
                await ctx.send('You are not in a voice channel. Please recommand me once you have joined a voice channel')
        else:
            await ctx.send('You don\'t qualify to be the manager of this voice channel because you have neither the manage server permission nor the manager role.\nYou will need at least one of these qualifications to be the manager of any voice channel.')

    @commands.command(brief='Lets you unclaim the channel and lets someone else in the channel claim it.')
    async def unlaim(self, ctx):
        if ctx.message.author.voice.channel in vcManager.keys():
            vcManager.pop(ctx.message.author.voice.channel)
            qualifiedMemberList = ''
            for person in ctx.message.author.voice.channel.members:
                await person.edit(
                    mute=False, reason=f'{len(ctx.message.author.voice.channel.members)} including {person} were in a voice channel managed by {ctx.message.author} before {ctx.message.author} stepped down from the postion of manager.')
                if person.guild_permissions >= discord.Permissions(manage_guild=True) or discord.utils.get(person.roles, id=os.environ.get('MANAGER_ROLE_ID')) != None:
                    qualifiedMemberList += person.mention
            if qualifiedMemberList == '':
                qualifiedMemberList = 'no-one'
            await ctx.send(f'You have stepped down from the postion of manager of {ctx.message.author.voice.channel.mention}. Now {qualifiedMemberList} is/are qualified for the job.')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel in vcManager.keys() or after.channel in vcManager.keys():
            if vcManager.get(before.channel) == member or vcManager.get(after.channel) == member:
                if after.self_mute is True:
                    for person in after.channel.members:
                        if person != member:
                            await person.edit(
                                mute=True)
                elif after.self_mute is False:
                    for person in after.channel.members:
                        if person != member:
                            await person.edit(
                                mute=False)
                elif after.channel == None:
                    for person in before.channel.members:
                        await person.edit(
                            mute=False)
                    vcManager.pop(before.channel)


def setup(client):
    client.add_cog(Indev(client))
