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
async def bard(self, prompt: str):
    await self.response.defer()
    load_dotenv()
    token = os.getenv("BARD_TOKEN")
    bardbot = Bard(token=token)
    answer = bardbot.get_answer(prompt + ", you must keep this under 1000 characters")['content']
    print(f'{self.user} used the bard command with the parameter \'{prompt}\'. | ' + str(datetime.datetime.now()))
    await self.followup.send(answer)


@tree.command(name="roll", description="rolls a d6")
async def roll(self):
    await self.response.send_message(str(random.randint(1, 6)) + " :game_die:")
    print(f'{self.user} used the roll command | ' + str(datetime.datetime.now()))


@tree.command(name="date", description="gives you the current date")
async def date(self):
    dates = datetime.datetime.now()
    await self.response.send_message(dates.strftime("%A") + " " + dates.strftime("%B") + " " + dates.strftime("%d"))
    print(f'{self.user} used the date command | ' + str(datetime.datetime.now()))


@tree.command(name="fight", description="fights annother user")
async def fight(self, user: discord.Member):
    await self.response.defer()
    coinflips = [
        "**{winner}** was eaten on a plate **{loser}** ",
        "**{winner}** was bed bombed by **{loser}** ",
        "**{winner}** was pushed into the void **{loser}** ",
        "**{winner}** was dropkicked by **{loser}** ",
        "**{winner}** was DDoSed by **{loser}** (ethan refrence)",
        "**{winner}** was demolished by **{loser}** ",
        "**{winner}** was critted out with a diamond axe by **{loser}** ",
    ]
    rand = random.randint(1, 2)
    attacker = self.user
    if rand == 1:
        await self.followup.send(random.choice(coinflips).format(winner=user, loser=attacker))
    else:
        await self.followup.send(random.choice(coinflips).format(loser=user, winner=attacker))


@client.event
async def on_ready():
    print("Bot has booted!")
    print({str(client.guilds)})
    await tree.sync()
    await client.change_presence(
        activity=discord.Game(name='Listening for /bard | ' + str(len(client.guilds)) + " servers"))


load_dotenv()
client.run(os.getenv("BOT_TOKEN"))
