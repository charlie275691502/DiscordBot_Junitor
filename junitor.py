import discord
from discord.ext import commands
import re
from os import listdir
from os.path import isfile, join
import random

TOKEN = "YOUR_TOKEN"

bannedUserIds = []
bannedEmojis = ['💩']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f"{client.user} Ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any([bannedEmoji in message.content for bannedEmoji in bannedEmojis]) and message.author.id in bannedUserIds:
        await message.delete()
        print(f'Delete message: "{message.content}" from {message.author.name}')

@client.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name in bannedEmojis and payload.user_id in bannedUserIds:
        msg = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
        await msg.remove_reaction(payload.emoji, payload.member)
        print(f'Delete emoji: "{payload.emoji.name}" from {payload.member.name}')

client.run(TOKEN)