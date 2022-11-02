from importlib.util import module_for_loader
import discord
from discord.ext import commands
from typing import Dict
import os
import sys

import yaml
USER_PATH = "C:/Users/14704/Desktop/fsa connect/fsaconnect"
sys.path.append("{}\src\main".format(USER_PATH))
from grabber import *
print(sys.path)
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def config(ctx):
    await ctx.author.send('enter your fsaconnect username')
    username = await client.wait_for('message', check=lambda message: message.author == ctx.author and message.channel.id == ctx.author.dm_channel.id)
    await ctx.author.send('enter your fsaconnect password')
    password = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    data = {ctx.author.id: {'username': username.content,
                            'password': password.content}}
    print(data)
    with open('C:/Users/14704\Desktop/fsa connect/fsaconnect/discord/configs.yaml', 'r') as f:
        current_yaml = yaml.safe_load(f)
        current_yaml.update(data)
    if current_yaml:
        with open('C:/Users/14704\Desktop/fsa connect/fsaconnect/discord/configs.yaml', 'w') as f:
            yaml.safe_dump(current_yaml, f)
    await ctx.author.send('config saved')


@client.command()
async def getGrades(message):
    try:
        with open('C:/Users/14704/Desktop/fsa connect/fsaconnect/discord\configs.yaml', 'r') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            userdata = data[message.author.id]
            username = userdata['username']
            password = userdata['password']
            barGraph(username, password)
            await message.channel.send('fsaconnect v.0.1.0 by heykyros')
            await message.channel.send(file=discord.File('graph.png'))
            os.remove("C:/Users/14704/Desktop/fsa connect/graph.png")
            return
    except KeyError:
        await message.channel.send('you have not configured your account yet. use $config to do so')
        return


@client.command()
async def getAssignments(message):
    try:
        with open('C:/Users/14704/Desktop/fsa connect/fsaconnect/discord\configs.yaml', 'r') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            userdata = data[message.author.id]
            username = userdata['username']
            password = userdata['password']
            pullAssignments(username, password)
            await message.channel.send(file=discord.File('table.png'))
            os.remove("C:/Users/14704/Desktop/fsa connect/table.png")
            return
    except KeyError:
        await message.channel.send('you have not configured your account yet. use $config to do so')
        return

client.run(
    "MTAzNjc4NjY5MDc3MTE0NDczNA.GqTwyj.hPnSD1N-huEspxptLdhvvfpeIsaUnlq5jZ0RcY")
