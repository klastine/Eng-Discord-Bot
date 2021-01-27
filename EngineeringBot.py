import discord
import os
import asyncio
import time

class MyClient(discord.Client):
    async def on_message(self, message):
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

f = open("secret.txt","r")
for line in f:
    secret = line

client = MyClient()
client.run(secret)
