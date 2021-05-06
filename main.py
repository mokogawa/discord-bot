import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event  
async def on_ready():
    print('==Bot is online==')

bot.run("ODM5ODIxMTA0NTI3ODM1MTg2.YJPOWg.nf_nve29_Hl1ES4vT35y5Hq_4eY")