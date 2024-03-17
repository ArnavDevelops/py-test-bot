import discord
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
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print('Logged in!')
    
@tree.command(
        name="ping", 
        description="Play ping pong with me, Liberal",
        guild=discord.Object(id=guildId)
)
async def ping(interaction: discord.Interaction):    
    await interaction.response.send_message("pong 🏓")

@tree.command(
        name="embed", 
        description="Try out embed, Liberal",
        guild=discord.Object(id=guildId)
)
async def embed(interaction: discord.Interaction): 
    embed = discord.Embed(
        title="Test",
        description="Test",
        color="RANDOM",
        timestamp = datetime
    )
    await interaction.response.send_message(embeds=[embed])

client.run(Token)