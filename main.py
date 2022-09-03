from dis import dis
from msilib.schema import Component
import os
from re import S

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

MA_GUILD_ID = '1013056940726833243'

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



class InviteButtons(discord.ui.View):
    def __init__(self, *, invite_author, timeout=180, ):
        super().__init__(timeout=timeout)
        self.invite_author = invite_author
        self.joiner_ids = set()

    @discord.ui.button(label="มา",style=discord.ButtonStyle.green)
    async def ma_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        joiner_id = interaction.user.id
        self.joiner_ids.add(joiner_id)
        await interaction.response.edit_message(content=f"<@{self.invite_author}> ชวนยิง\n response: {' '.join([f'<@{id}>' for id in self.joiner_ids])}")

@bot.command(name="ma")
async def invite_command(ctx: commands.context):
    authorid = ctx.message.author.id
    inviteButtons = InviteButtons(invite_author=authorid)
    await ctx.send(f"<@{authorid}> ชวนยิง", view=inviteButtons)

bot.run(DISCORD_TOKEN)

