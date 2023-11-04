import os

import discord
import random

intents = discord.Intents.default()
intents.voice_states = True
client = discord.Client(intents=intents)


lobby_channel_name = "Lobby"
voice_channel_category_name = "Voice Channels"
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
    print(f"Logged in as {client.user}!")


@client.event
async def on_voice_state_update(member, before, after):
    if before is not None:
        if before.channel.name != lobby_channel_name:
            channel = before.channel
            if len(channel.members) == 0:
                await channel.delete()
    if after is not None:
        if after.channel.name != lobby_channel_name:
            return
    guild = after.channel.guild
    voice_channel_category = discord.utils.find(
        lambda cat: cat.name == voice_channel_category_name, guild.categories
    )
    new_channel = await guild.create_voice_channel(
        random.choice(channel_names), category=voice_channel_category
    )
    await member.move_to(new_channel)


if __name__ == "__main__":
    token = os.environ["BOT_TOKEN"]
    if token is None:
        print("token not configured")
        exit(1)
    client.run(token)
