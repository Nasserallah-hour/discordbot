import discord
import os

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTA2NjA1MDI2MDM4MTc0OTM2Mg.Giheve.OqIJN-KMcIOvv7l0g7inZ83E0QOVHLSK_K6sjg')