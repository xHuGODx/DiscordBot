import discord
import os
import random

TOKEN = os.getenv('TOKEN')  
GUILD_ID = int(os.getenv('GUILD_ID'))
USER_ID  = int(os.getenv('USER_ID'))

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
list_of_nicknames = ["Pedro", "Juan", "Carlos", "Luis", "Miguel", "Javier", "Andres", "Fernando", "Diego", "Pablo"]

async def update_nickname():
    await client.wait_until_ready()
    guild = client.get_guild(GUILD_ID)
    member = guild.get_member(USER_ID)
    print(f"Member: {member}")

    while not client.is_closed():
        new_nickname = random.choice(list_of_nicknames)
        if member:
            try:
                await member.edit(nick=new_nickname)
                print(f"Updated nickname to: {new_nickname}")
            except discord.Forbidden:
                print("Bot lacks permission to change nickname.")
        else:
            print("User not found in guild.")


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(update_nickname())

client.run(TOKEN)
