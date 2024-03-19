import discord
import datetime
from discord.ext import commands
from discord import Option
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

guildId = os.environ.get("guildId")
Token = os.environ.get("Token")

intents = discord.Intents.default().all()
client = commands.Bot(intents=intents)

#Activity
@client.event
async def on_ready():
    activity = discord.Activity(
        name="You",
        type=discord.ActivityType.watching
    )
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Logged in!')

@client.slash_command(
        name="ping", 
        description="Play ping pong with me, Liberal",
)
async def ping(ctx):    
    await ctx.respond(content=f"pong 🏓 | Bot's Latency: {client.latency}", ephemeral=True)

@client.slash_command(
        name="embed", 
        description="Try out embed, Liberal",
)
async def embed(ctx): 
    embed = discord.Embed(
        author=discord.EmbedAuthor(name='Test', icon_url="https://cdn.discordapp.com/emojis/1180664825274183740.webp?size=128&quality=lossless"),
        title="Test",
        description="Test",
        colour=255000,
        timestamp=datetime.datetime.now(datetime.timezone.utc),
        image="https://cdn.discordapp.com/emojis/1207023441858011186.webp?size=128&quality=lossless",
        thumbnail="https://cdn.discordapp.com/emojis/1180665320562761829.webp?size=128&quality=lossless",
        footer=discord.EmbedFooter(text='Test', icon_url="https://cdn.discordapp.com/emojis/1180664825274183740.webp?size=128&quality=lossless")
    )
    embed.add_field(name='inclined field', value='inclined field', inline=True)
    embed.add_field(name='field', value='field')

    await ctx.respond(embeds=[embed])

@client.command(
    name="say",
    description="What do u want me to say?",
)
async def say(
    ctx: discord.ApplicationContext,
    text: Option(input_type=str, name="Text", description="Enter the text") # type: ignore
    ):
    await ctx.respond(content="Sent!", ephemeral=True)
    await ctx.send(f"{text}")

client.run(Token)