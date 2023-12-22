###### IMPORTS ######
 
import random
import sqlite3
import discord
from discord import app_commands
from discord.ext import commands
import requests
from config import *

###### FONCTIONS #######

###### FIN FONCTIONS #######


    
###### BOT ######
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

if DEVMODE:
    TOKEN="DEV_TOKEN"
else:
    TOKEN=RE_TOKEN

bot = commands.Bot(command_prefix="$", intents=intents, help_command=None)

async def get_bot():
    return bot

###### COMMANDES ######
    
@bot.tree.command(name='ping', description='Affiche la latence du bot')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.response.send_message(f"Pong! Latence: {latency}ms")

@bot.tree.command(name='ping2', description='Affiche la latence du bot')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.response.send_message(f"Pong! Latence: {latency}ms")

@bot.tree.command(name='card', description='Choisi entre yugioh et magic')
async def card(ctx):
    await ctx.response.send_message(f"J'ai choisi {random.choice(['yugioh', 'magic'])}")

# Confirme la connexion
@bot.event
async def on_ready():
    print('Logged in as', bot.user)
    await bot.get_channel(1092509916238979182).send("Bot démarré avec succès!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {synced} commands.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")
    await bot.change_presence(activity=discord.Game(name='Coucou!'))

###### FIN BOT ######
    
###### COMMANDES TEXTE ######
@bot.event
async def on_message(message):

    #ignore lui meme
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
        ping()

    await bot.process_commands(message)
    if message.author.id in DEV_ID: #admin commands :)

        if message.content == '$adstop':
            await message.channel.send('Arret en cours...')
            await bot.close()

        if message.content[:6] == '$adsay':
            await message.channel.send(message.content[7:])
            await message.delete()

        if message.content[:9] == '$adstatus':
            await bot.change_presence(activity=discord.Game(name=message.content[10:]))
            await message.channel.send('Status changé!')
###### FIN COMMANDES ######

###### A LA FIN, LANCE LE BOT ######    
bot.run(TOKEN) #run bot