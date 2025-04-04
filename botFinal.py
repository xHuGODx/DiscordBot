import discord
import asyncio
import os
from datetime import datetime

TOKEN = os.getenv('TOKEN') 
GUILD_ID = os.getenv('GUILD_ID') 
USER_ID = os.getenv('USER_ID')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def update_nickname():
    await client.wait_until_ready()
    guild = client.get_guild(GUILD_ID)
    member = guild.get_member(USER_ID)

    while not client.is_closed():
        today = datetime.today()
        summer_start = datetime(today.year, 7, 1)
        days_left = (summer_start - today).days

        new_nickname = f"{days_left} days until Summer"
        if member:
            try:
                await member.edit(nick=new_nickname)
                print(f"Updated nickname to: {new_nickname}")
            except discord.Forbidden:
                print("Bot lacks permission to change nickname.")
        else:
            print("User not found in guild.")

        await asyncio.sleep(86400)  # Update every 24 hours

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(update_nickname())

client.run(TOKEN)
