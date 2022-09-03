from dis import dis
import os
from re import S

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord')

@bot.command(name='ping')
async def ping_command(ctx):
    await ctx.send(f"Pong: Latency is {bot.latency * 1000:.3f}ms")

@bot.command(name='echo')
async def echo_command(ctx, arg):
    await ctx.send(f"{arg}")

bot.run(DISCORD_TOKEN)

