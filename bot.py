import discord
from discord.ext import commands
import os
import asyncio
from keep_alive import keep_alive  # <- import from keep_alive.py
from dotenv import load_dotenv
load_dotenv()

print("TOKEN FOUND:", bool(os.getenv("DISCORD_TOKEN")))
print("TOKEN VALUE:", os.getenv("DISCORD_TOKEN"))
print("USER:", os.getenv("DISCORD_USER"))
print("PASS FOUND:", bool(os.getenv("DISCORD_PASS")))


intents = discord.Intents.default()
intents.message_content = True  # needed for commands

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            
            
print("TOKEN from env:", os.getenv("DISCORD_TOKEN"))


async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("DISCORD_TOKEN")) # store token in secrets


# start keep-alive web server
keep_alive()

# run bot
asyncio.run(main())
