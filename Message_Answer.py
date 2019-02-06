import discord

from discord.ext import commands 
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix = '>')

@Bot.command(pass_context = True)
async def User_Message(ctx):
    await Bot.say("Bot_Answer")

Bot.run("token")