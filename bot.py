import discord
from discord.ext import commands
from config import token #make a token file to store the token
import random

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)

class Car():
    def __init__(self, warna, merek="Toyota"):
        self.warna = warna
        self.merek = merek

    def info(self):
        return f"Warna mobil adalah: {self.warna.title()}. Dan Merek mobil adalah: {self.merek.title()}"
        
        

@client.event
async def on_ready():
    print(f'Kita telah login sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('Ini adalah echo-bot yang dibuat dengan pustaka discord.py!')

@client.command()
async def info(ctx):
    await ctx.send(f'Nama saya {client.user}, saya dibuat oleh greyslight')

@client.command()
async def gamble(ctx):
    rNumber = random.randint(1,6)
    await ctx.send(f"Kamu dapet nomor {rNumber}")

@client.command()
async def add(ctx):
    await ctx.send("Berikan angka pertama")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    num1 = await client.wait_for('message', check=check)
    num1 = int(num1.content)
    await ctx.send("Berikan angka kedua")
    num2 = await client.wait_for('message', check=check)
    num2 = int(num2.content)
    try:
        result = num1 + num2
        await ctx.send(f"Hasil dari {num1} + {num2} adalah {result}")
    except:
        await ctx.send("Kamu tidak memasukkan angka!")

@client.command()
async def makecar(ctx, w, m):
    thecar = Car(warna=w, merek=m)
    await ctx.send(thecar.info())


    

@client.command()
async def allcmds(ctx):
    cmds = (
        "$about: menjelaskan fungsi bot ini",
        "$info: informasi tentang bot",
        "$gamble: lempar dadu",
        "$add: menambahkan 2 angka"
    )

client.run(token)
