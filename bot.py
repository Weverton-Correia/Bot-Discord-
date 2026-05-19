import discord
from discord.ext import commands
import re

TOKEN = "DIscord"
ID_GUEIGAS = "ID do bot" 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

contador_cara = 0

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_message(message):
    global contador_cara

    if message.author.bot:
        return

    if message.author.id == ID_GUEIGAS:
        ocorrencias = len(re.findall(r'\bcara\b', message.content.lower()))
        contador_cara += ocorrencias

    await bot.process_commands(message)


@bot.command()
async def cara(ctx):
    await ctx.send(f"🗣️ O Gueigas já falou **cara** {contador_cara} vezes ")


bot.run(TOKEN)

