import os
import random
import sys

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix="!")


LOBBY_CHANNEL_NAME = "Lobby"
VOICE_CHANNLE_CATEGORY_NAME = "Voice Channels"
channel_names = [
    "илья",
    "сергей",
    "иркутск",
    "кирил",
    "грустный",
    "весёлый",
    "акваланг",
    "чилл",
    "угол-наклона-less-than-or-greater-than-90",
    "1XBET",
    "куда это логать?",
    "🗿",
]


@client.event
async def on_ready():
    await client.tree.sync()
    print(f"Logged in as {client.user}!")


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is not None:
        if before.channel.name != LOBBY_CHANNEL_NAME:
            channel = before.channel
            if len(channel.members) == 0:
                await channel.delete()
    if after.channel is not None:
        if after.channel.name != LOBBY_CHANNEL_NAME:
            return
        guild = after.channel.guild
        voice_channel_category = discord.utils.find(
            lambda cat: cat.name == VOICE_CHANNLE_CATEGORY_NAME, guild.categories
        )
        new_channel = await guild.create_voice_channel(
            random.choice(channel_names), category=voice_channel_category
        )
        await member.move_to(new_channel)


@client.hybrid_command(description="Rolls a random number between 0 and 100")
async def roll(ctx):
    number = random.randint(0, 100)
    await ctx.send(number)


if __name__ == "__main__":
    token = os.environ["BOT_TOKEN"]
    if token is None:
        print("token not configured")
        sys.exit(1)
    client.run(token)
