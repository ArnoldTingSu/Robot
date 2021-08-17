import os
import discord
import requests
import json
import random
from replit import db


my_secret = os.environ['COIN']


client = discord.Client()

queryWords= [
  "question",
  "explore",
  "lookup",
  "find",
  "what",
  "need",
  "suggestion",
  "suggestions",
  "help",
  "wonder",
  "curious",
  "where",
  "when"
]

queryDict = {
  "question": "questions",
  "help": "help me"
}

queryStarterConvo = [
  "I know a solution...",
  "I may have a suggestion...",
  "I can help you with that!",
  "I'm a helper, I can look that up for you!",
  "Do you need help?",
  "Can I look that up fory you?",
  "I can show you pictures of that place.",
  "Let me enlighten you."
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("$hello"):
        await message.channel.send("hello!")
    
    if msg.startswith("$bye"):
      await message.channel.send("goodbye")

    if msg.startswith("$quote"):
      quote= get_quote()
      await message.channel.send(quote)

    if any(word in msg for word in queryWords):
      await message.channel.send(random.choice(queryStarterConvo))


client.run(os.getenv('COIN'))