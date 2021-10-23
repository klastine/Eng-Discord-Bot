import discord
import os
import asyncio
import time
import re
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

f = open("secret.txt","r")
secret = f.readline()
f.close()
client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_message(message):
    if message.content.startswith('>>join'):
        content = message.content.split()
        if len(content) != 2:
            message.channel.send("Invalid number of arguments!")
        else:
            member = message.author
            role = discord.utils.get(message.guild.roles, name=str(content[1]))
            try:
                await member.add_roles(role)
                string = "Added to "+content[1]
                await message.channel.send(string)
            except:
                await message.channel.send("Role not found!")
    elif message.content.startswith('>>leaveall'):
        classMatcher = re.compile(r'[a-z]+[0-9]+')
        content = message.content.split()
        for role in message.author.roles:
            try:
                if classMatcher.match(role.name):
                    await message.author.remove_roles(role)
            except Exception as e:
                print(e)
                #await message.channel.send("Error!")
        string = "Left all classes!"
        await message.channel.send(string)
    elif message.content.startswith('>>leave'):
        content = message.content.split()
        if len(content) != 2:
            message.channel.send("Invalid number of arguments!")
        else:
            member = message.author
            role = discord.utils.get(message.guild.roles, name=str(content[1]))
            try:
                await member.remove_roles(role)
                string = "Left "+content[1]
                await message.channel.send(string)
            except:
                await message.channel.send("Role not found!")
    elif message.content.startswith('>>classes'):
        classMatcher = re.compile(r'[a-z]+[0-9]+')
        string = "The classes currently supported are: \n"
        roles = []
        for y in message.guild.roles:
            roles.append(y.name)
        classes = [x for x in roles if classMatcher.match(x)]
        for role in classes:
            string = string + role + "\n"
        await message.channel.send(string)

@client.event
async def on_member_join(member):
    tag = member.mention
    string = "Welcome to the U of Iowa Engineering Discord "+tag+"! To join the channels for your class, just go to <#803094504554102785> and type >>join followed by the class code in all lower-case to be entered in. Example: >>join ece2220. If you don't get entered into the class channel, we haven't made one for that class yet. Please put your class list in <#803002750115905538>. We want to have a channel for every class with more than 2 server members in it, so we need to know what our server members are taking!"
    await client.get_channel(803111033891192842).send(string)

client.run(secret)
