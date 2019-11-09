import discord
import asyncio
from discord.ext import commands
import os
import discord
import random
import time
import math

client = commands.Bot(command_prefix=".")
client.remove_command("help")


x = 0
m=60
h=60*m

@client.command()
async def blow(ctx):
    global x, m, h
    if commands.is_owner():
        if x == 0:
            while x < 12*h:
                x = x + 1
                time.sleep(1)
                if x == 6*h:
                    await ctx.send("@everyone 6 HOURS REMAINING.")

                if x<60:
                    await ctx.send("{} seconds remaining.".format(60-x))
            await ctx.send("Boom.")
        if x > 0:
            await ctx.send("Bomb already ticking !")

@client.command()
async def uptime(ctx):
    sr =12*h-x
    srm = round((sr/60),0)
    srh = round((sr/60/60),0)
    print('```{} seconds remaining\n {} minutes remaining,\n {} hours remaining.```'.format(sr,srm,srh))

@client.event
async def on_ready():

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='TICK. TICK. TICK.||.time to see how long till explosion'))


client.run('NjQyNjcyOTA0Mjk5MDg1ODM1.XcaXPA.ryeYz7TnrRrlIDzYtVwhXth9bs8')