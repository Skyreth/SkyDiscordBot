import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Made by Skyreth")

@bot.event
async def on_ready():
    print("Bot Succesfully Started !")

@bot.command()
async def talk(ctx):
	await ctx.send("Coucou !")

@bot.event
async def on_message(message):
	if message.content == "Hello" or message.content == "Bonjour":
		await message.channel.send("Bonjour a toi "+message.author.+" !")
