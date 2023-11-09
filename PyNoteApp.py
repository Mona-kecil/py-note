import discord
from dotenv import load_dotenv
import os

load_dotenv()
bot = discord.Bot(intents = discord.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")

@bot.slash_command(name = "ping", description = "Returns the bot's latency")
async def ping(ctx):
    await ctx.respond(f"Hello!!\nPong! {bot.latency * 1000}ms")

bot.run(os.getenv('TOKEN'))