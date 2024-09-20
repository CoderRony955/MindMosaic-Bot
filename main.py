import discord
from discord import app_commands
from discord.ext import commands
import random
import json

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

bot = commands.Bot(command_prefix='!', intents=intents)


# Event triggered when the bot is ready and has connected to the server
@bot.event
async def on_ready():
    Activity = discord.Game(name='!bothelp')
    await bot.change_presence(status=discord.Status.online, activity=Activity)
    print(f'Bot {bot.user.name} has connected to Discord!')


# Basic command that the bot responds to
@bot.command(name='hello')
async def hello(ctx):
    # await ctx.send(f'Hello {ctx.author.name}!')
    embed = discord.Embed(
        description=f'Hello {ctx.author.name}! :)',
        color=discord.Color.yellow()
    )
    await ctx.send(embed=embed)


def load_quotes(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['facts']


def show_random_quote(facts):
    return random.choice(facts)


# Command to get a random AI fact
@bot.command(name='aifact')
async def aifact(ctx):
    user = ctx.author
    facts = load_quotes('facts.json')
    embed = discord.Embed(
        title='Here is the latest fact about AI 🧮',
        description=f'{show_random_quote(facts)}',
        color=discord.Color.orange()

    )
    embed.set_footer(text=f"Requested by {user.name}",
                     icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
    await ctx.send(embed=embed)


@bot.command(name='bothelp')
async def cmd_help(ctx):
    help_description = """
    **Available Commands /**
    
      This bot provides the latest and random facts about Artificial Intelligence. 
    Use the following commands to interact with the bot:
    
    `!aifact` or `/aifact` - get latest random facts about AI
    
    `/bothelp` or `!bothelp` - about bot and available commands
    
    `/ping` - check bot latency
    
    
     Have fun learning more about AI and enjoy exploring new facts!
    
    """
    bot_avatar_url = bot.user.avatar.url if bot.user.avatar else bot.user.default_avatar.url
    embed = discord.Embed(
        title='MindMosaic',
        description=f'{help_description}',
        color=discord.Color.light_gray()
    )
    embed.set_thumbnail(url=bot_avatar_url)
    embed.set_footer(text=f"{bot.user.name}", icon_url=bot_avatar_url)

    await ctx.send(embed=embed)


@bot.tree.command(name="bothelp", description="all commands")
async def h_cmd(interaction: discord.Interaction):
    # await interaction.response.send_message("Hello there!")
    help_description = """
       **Available Commands /**
       
         This bot provides the latest and random facts about Artificial Intelligence. 
       Use the following commands to interact with the bot:

       `!aifact` or `/aifact` - get latest random facts about AI

       `/bothelp` or `!bothelp` - about bot and available commands
    
       `/ping` - check bot latency

        Have fun learning more about AI and enjoy exploring new facts!

       """
    bot_avatar_url = bot.user.avatar.url if bot.user.avatar else bot.user.default_avatar.url
    embed = discord.Embed(
        title='MindMosaic',
        description=f'{help_description}',
        color=discord.Color.light_gray()
    )
    embed.set_thumbnail(url=bot_avatar_url)
    embed.set_footer(text=f"{bot.user.name}", icon_url=bot_avatar_url)
    await interaction.response.send(embed=embed)


@bot.tree.command(name="ping", description="Check bot latency.")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send(f"Pong! Latency is: {latency}ms.")


@bot.tree.command(name='aifact', description='get random AI facts')
async def fact(interaction: discord.Interaction):
    user = interaction.user
    facts = load_quotes('facts.json')
    embed = discord.Embed(
        title='Here is the latest fact about AI 🧮',
        description=f'{show_random_quote(facts)}',
        color=discord.Color.orange()

    )
    embed.set_footer(text=f"Requested by {user.name}",
                     icon_url=user.avatar.url if user.avatar else user.default_avatar.url)
    await interaction.response.send(embed=embed)


# Command to say goodbye
@bot.command(name='bye')
async def bye(ctx):
    # await ctx.send(f'Goodbye {ctx.author.name}, see you next time!')
    embed = discord.Embed(
        title=f'Goodbye👋🏻 {ctx.author.name}, see you later',
        color=discord.Color.yellow()
    )
    await ctx.send(embed=embed)


# Run the bot with your token
TOKEN = 'BOT-TOKEN'
bot.run(TOKEN)
