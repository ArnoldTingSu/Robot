import os
import discord
my_secret = os.environ['COIN']


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("hello!")
    
    if message.content.startswith("bye"):
      await message.channel.send("goodbye")

client.run(os.getenv('COIN'))