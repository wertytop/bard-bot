import datetime
import os
import random

import discord
from bardapi import Bard
from discord import app_commands
from dotenv import load_dotenv

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name="bard", description="allows a user to talk with google bard")
async def diffusion(self, prompt: str):
    await self.response.defer()
    load_dotenv()
    token = os.getenv("BARD_TOKEN")
    bard = Bard(token=token)
    answer = bard.get_answer(prompt+", you must keep this under 1000 characters")['content']
    print(answer, prompt)
    await self.followup.send(answer)


@tree.command(name="roll", description="rolls a d6")
async def diffusion(self):
    await self.response.send_message(str(random.randint(1, 6)) + " :game_die:")


@tree.command(name="date", description="gives you the current date")
async def diffusion(self):
    date = datetime.datetime.now()
    await self.response.send_message(date.strftime("%A") + " " + date.strftime("%B") + " " + date.strftime("%d"))


@client.event
async def on_ready():
    print("Bot has booted!")
    await tree.sync()


load_dotenv()
client.run(os.getenv("BOT_TOKEN"))
