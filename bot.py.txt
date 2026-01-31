import discord
from discord.ext import commands
import re

TOKEN = "MTQ2Njk1MjIwMjIyNzY3OTU1Ng.Gsb7Jq.oZN2IGGdOigpBso6sTTB6wDJq6BDI91CEfwt5U"
ID_GUEIGAS = 1466952202227679556  

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
    await ctx.send(f"🗣️ O Gueigas já falou **cara** {contador_cara} vezes 😂")


bot.run(TOKEN)
