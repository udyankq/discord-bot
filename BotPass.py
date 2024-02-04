import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def generate(password_size):
    all_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"

    for _ in range(1):
        password = ''
        for _ in range(password_size):
            password = password + random.choice(all_characters + special_characters)
        return password

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def gen_pass(ctx, password_size = 8):
    await ctx.send(generate(password_size))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTIwMTAzMzI1MzM2OTQyNTk3Mg.G59vnC.IW0wiayzSAb06U02ceMEbEDBCVfmDaAK_RBH_o")