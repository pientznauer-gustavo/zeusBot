import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="*", intents=intents)

@bot.event
async def on_ready():
    print(f"Tô com a mamadeira cheia aqui")

@bot.command()
#serve mais pra eu testar e saber quando o bot tá online
async def teste(ctx, arg=None):
    await ctx.send("funcionando") 
    await bot.process_commands(mensagem)

@bot.event
#função básica de receber membros recem chegados...
async def on_member_join(membro):
    canal = membro.guild.system_channel
    await canal.send(f"{membro.mention}, BEM VINDO MANO...")



@bot.event
async def on_message(mensagem):
    if mensagem.author == bot.user:
        return
    #testando uma funcionalidade de censura
    if "jack" in mensagem.content.lower():
        await mensagem.delete()
        await mensagem.channel.send(f"EIIIIII {mensagem.author.mention}")
    #testando uma de adicionar reação
    if "leite" in mensagem.content.lower():
        await mensagem.add_reaction("🍼")

    await bot.process_commands(mensagem)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)



