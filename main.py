import discord
from discord.ext import commands
Token = 'Your_Token'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents) 

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

@bot.command()
async def join(ctx)
    
bot.run(Token) # Launcher
