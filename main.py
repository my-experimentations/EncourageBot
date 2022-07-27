import discord
#allows us to use the .env file for token
import os
#allows our code to make HTTP requests to get data from the API. API returns json
import requests
#makes working data returned easier to use
import json
import random
#use the replit database
from replit import db


#create an instance of a clinet that is the connection to Discord
client = discord.Client()

#trigger words to activate the bot
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
#users will be able to add to this list later.
starter_encouragements = [
  "Cheer up!", "Hang in there.", "You are a great person / bot!"]

#returns a quote from the API
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#use the client to register an event
@client.event
#this event is going to be called when the bot is ready to start being used
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#when the bot receives a message...
@client.event
async def on_message(message):
  #ignores messages sent by the bot
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in message.content for word in sad_words):
      await message.channel.send(random.choice(starter_encouragements))

#running the bot
#use TOKEN b/c bot will be public and token will mask bot token.
client.run(os.getenv('TOKEN'))

#reference: https://www.youtube.com/watch?v=SPTfmiYiuok