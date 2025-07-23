import discord
from discord.ext import commands
import asyncio
import json
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key="--")
Token = '--'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} Entro')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!'):
        prompt = message.content[len('!'):]
        try:
            headers = {
                "content-type": "aplication/json",
                "authorization": f"bearer {SK_API}"
            }
            payload = {
                "model": "deepseek-r1:8b",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
            response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=payload)
            response.raise_for_status()
            deepseek_response = response.json()
            ai_text = deepseek_response['choices'][0]['message']['content']
            await message.channel.send(ai_text)
        except requests.exceptions.RequestException as e:
            await message.channel.send(f"Error communicating with DeepSeek API: {e}")
        except KeyError:
            await message.channel.send("Could not parse DeepSeek API response.") #line 34 error "authorization"

#    await message.channel.send(message.content)

#    if message.content.startswith('$hello'):
#            await message.channel.send('hello')

client.run(Token) #Launcher
