import discord, os

token = os.getenv("TOKEN")
intent = discord.Intents.default()
intent.members = True
intent.message_content = True
client = discord.Client(intents=intent)

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.content.startswith('!vivo'):
    await message.channel.send('Pansito esta vivo!')
print(token)
client.run(token)