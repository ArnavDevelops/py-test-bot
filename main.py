import discord
from discord import app_commands
import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

guildId = os.environ.get("guildId")
Token = os.environ.get("Token")

intents = discord.Intents.default().all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

#Activity
@client.event
async def on_ready():
    activity = discord.Activity(
        name="Amongus",
        type=discord.ActivityType.watching
    )
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('Logged in!')

@app_commands.command(
        name="ping", 
        description="Play ping pong with me, Liberal",
)
async def ping(interaction: discord.Interaction):    
    await interaction.response.send_message(content="pong 🏓", ephemeral=True)

@app_commands.command(
        name="embed", 
        description="Try out embed, Liberal",
)
async def embed(interaction: discord.Interaction): 
    embed = discord.Embed(
        title="Test",
        description="Test",
        color="RANDOM",
        timestamp=datetime.datetime
    )
    await interaction.response.send_message(embeds=[embed])


tree.add_command(ping, guild=discord.Object(id=guildId))

client.run(Token)