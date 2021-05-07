import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = "!", intents = intents)

#online message
@bot.event  
async def on_ready():
    print('==Bot is online==')

#join
@bot.event
async def on_member_join(member):
    print(F'{member} has joined!')
    channel = bot.get_channel(839829560560582669)
    await channel.send(F'<{member}>has joined')

#leave
@bot.event
async def on_member_remove(member):
    print(F'{member} has left QAQ')
    channel = bot.get_channel(839829560560582669)
    await channel.send(F'<{member}>has left QAQ')

#ping
@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)}(ms)is the server ping to this bot')

#send message
@bot.command()
async def sayd(ctx, *, msg="無"):
    await ctx.message.delete()
    await ctx.send(msg)
    

bot.run(jdata["TOKEN"])