import discord 
import random
import os 
from discord.ext import commands 
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix= "!", intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def basura_reciclaje(ctx):
    await ctx.send("la basura reciclaje♻️, ayuda al planeta a no tener tantos recidios y poder reutilizarlos. haciendo bolsas, manualidades o hasta objetos cotidianos")

@bot.command()
async def basura_organica(ctx):
    await ctx.send("la basura organica es la basura q proviene de la comida y se deconpone facil porque son plantas, frutas, etc.")

@bot.command()
async def basura_peligrosa(ctx):
    await ctx.send("La Basura Peligrosa❌(no es reciclaje), son los residuos hospitalarios o que tenga bacterias, parásitos, virus, hongos e infecciosos")

@bot.command()
async def imag_basura(ctx):
    basura_alet= random.choice(os.listdir("basura"))
    with open(f"basura/{basura_alet}", 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run("token")
