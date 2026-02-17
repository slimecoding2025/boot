import discord
from discord.ext import tasks
from datetime import datetime

TOKEN = "MTQ3MzM5OTE3Mjc2ODk5MzQyMw.GHEqTW.-StmjqScJ12E1f-HPKEcZ-h95zDUdvXppa8DCU"

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
client = discord.Client(intents=intents)

BAC_DATE = datetime(2026, 6, 13, 8, 0, 0)

@tasks.loop(hours=12)
async def countdown():
    now = datetime.now()
    remaining = BAC_DATE - now

    if remaining.total_seconds() > 0:
        days = remaining.days
        hours = remaining.seconds // 3600
        minutes = (remaining.seconds % 3600) // 60

        message = f"mazel {days} jours w {hours}h w {minutes} min 3al bac"

        for guild in client.guilds:
            for channel in guild.text_channels:
                if channel.name == "general-chat":
                    await channel.send(message)
                    break

@client.event
async def on_ready():
    print("Bot Ready!")
    countdown.start()


client.run(TOKEN)

