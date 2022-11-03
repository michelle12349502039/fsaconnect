
from importlib.util import module_for_loader
import discord
from discord.ext import commands
from typing import Dict
import os
import sys
from matplotlib.pyplot import text, title

import yaml
USER_PATH = "C:/Users/14704/Desktop/fsa connect/fsaconnect"
sys.path.append("{}\src\main".format(USER_PATH))
print(sys.path)
from grabber import *
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents,
                      activity=discord.Game(name="fsaconnect v.0.1.0 by heykyros"))
client.remove_command('help')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# respond if someone @s the bot
@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        embed = discord.Embed(title="fsaconnect", description="Hello! I'm bot that provides commands to access fsaconnect right from discord! To see my commands, type $help",
                              color=discord.Color.from_rgb(193, 154, 183))
        await message.channel.send(embed=embed)
    await client.process_commands(message)


@client.command()
async def config(ctx):
    embed = discord.Embed(description="Please enter your FSA Connect **username**",
                          color=discord.Color.from_rgb(193, 154, 183))
    await ctx.author.send(embed=embed)
    try:
      username = await client.wait_for('message', check=lambda message: message.author == ctx.author and message.channel.id == ctx.author.dm_channel.id,timeout=60)
      embed.description = "Please enter your FSA Connect **password**"
      try:
        password = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
        data = {ctx.author.id: {'username': username.content,
                            'password': password.content}}
        with open('C:/Users/14704\Desktop/fsa connect/fsaconnect/discord/configs.yaml', 'r') as f:
            current_yaml = yaml.safe_load(f)
            current_yaml.update(data)
        if current_yaml:
            with open('C:/Users/14704\Desktop/fsa connect/fsaconnect/discord/configs.yaml', 'w') as f:
                yaml.safe_dump(current_yaml, f)
        embed.description = "Config saved succesfully, enjoy!"
        await ctx.author.send(embed=embed)
      except:
        ctx.author.send("You have ran out of time to send your password. Please run this commmand again")
    except:
      ctx.author.send("You have ran out of time to send your username. Please run this commmand again")
    embed.description = "Please enter your FSA Connect **password**"
    await ctx.author.send(embed=embed)
    

@client.command()
async def mygrades(message):
    try:
        with open('C:/Users/14704/Desktop/fsa connect/fsaconnect/discord\configs.yaml', 'r') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            userdata = data[message.author.id]
            username = userdata['username']
            password = userdata['password']
            barGraph(username, password)
            file=discord.File('C:/Users/14704/Desktop/fsa connect/graph.png')
            embed = discord.Embed(title="your grades", color=discord.Color.from_rgb(0, 0, 0))
            embed.set_image(url="attachment://graph.png")
            await message.channel.send(file=file, embed=embed)
            os.remove("C:/Users/14704/Desktop/fsa connect/graph.png")
            return
    except KeyError:
        await message.channel.send('You have not configured your account yet. Please use $config and check your DMs')
        return


@client.command()
async def myassignments(message):
    try:
        with open('C:/Users/14704/Desktop/fsa connect/fsaconnect/discord\configs.yaml', 'r') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            userdata = data[message.author.id]
            username = userdata['username']
            password = userdata['password']
            pullAssignments(username, password)
            file=discord.File('C:/Users/14704/Desktop/fsa connect/table.png')
            embed = discord.Embed(title="your assignments", color=discord.Color.from_rgb(0, 0, 0))
            embed.set_image(url="attachment://table.png")
            await message.channel.send(file=file, embed=embed)
            os.remove("C:/Users/14704/Desktop/fsa connect/table.png")
            return
    except KeyError:
        await message.channel.send('You have not configured your account yet. Please use $config and check your DMs')
        return


@client.command()
async def help(message):
    embed = discord.Embed(title="Command Help",
                          color=discord.Color.from_rgb(193, 154, 183))
    embed.add_field(
        name="$config", value="Configure your account", inline=False)
    embed.add_field(name="$mygrades",
                    value="Get a graph of your grades", inline=False)
    embed.add_field(name="$myassignments",
                    value="Get your upcoming assignments", inline=False)
    embed.set_footer(text="fsaconnect v.0.1.0 by heykyros ❤️")
    await message.channel.send(embed=embed)

client.run(
    "fuck u")
