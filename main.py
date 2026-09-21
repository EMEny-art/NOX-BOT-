import os
import discord
from discord.ext import commands
intents=discord.Intents.default()
intents.message_content=True
intents.members=True
bot=commands.Bot(command_prefix="!",intents=intents)
@bot.event
async def on_ready():
 print(f"NOX CONNESSO: {bot.user}")
 await bot.tree.sync()
@bot.tree.command(name="profilo",description="profilo")
async def profilo(interaction:discord.Interaction):
 await interaction.response.send_message(f"Ciao {interaction.user.mention} sono ON!")
bot.run(os.getenv("TOKEN"))
