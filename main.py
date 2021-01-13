import discord  # Might need this later?
import os

import pandas as pd

from discord.ext import commands

from InFile import InFile
import config

initial_cogs = [
    'cogs.AI'
]

# Version 1.0
# JeepWranglerServiceBot
# Originally Authored By: FinCampbell

class Bot(commands.Bot):

    def __init__(self, command_prefix, self_bot):
        commands.Bot.__init__(self, command_prefix=command_prefix, self_bot=self_bot)
        self.message = "Launched"
        self.statusUpdate = "Still online"
        self.add_commands()
        self.masterframe = pd.DataFrame(columns=["Content"])

    async def on_ready(self):
        self.masterframe = self.clean(self.masterframe)

        for x in initial_cogs:
            self.load_extension(x)

        print(self.message)
        print(self.masterframe.head())

    def add_commands(self):
        @self.command(name="status", pass_context=True)
        async def status(ctx):
            print(ctx)
            await ctx.channel.send(self.statusUpdate)

    def clean(self, masterframe):
        for x in config.AUTHORS:
            for file in os.listdir(x):
                ff = InFile(x + "/" + file)
                tbl = []
                while True:
                    tt = ff.read()
                    if not tt: break
                    tbl.append(tt.strip())

                df = pd.DataFrame({'Content': tbl, 'Author': x})
                masterframe = masterframe.append(df)

        self.masterframe['Content'] = self.masterframe['Content'].str.replace('<|startoftext|>', '', regex=False)
        self.masterframe['Content'] = self.masterframe['Content'].str.replace('</|endoftext|>', '', regex=False)
        return masterframe


bot = Bot(command_prefix="!", self_bot=False)
bot.run(config.TOKEN)
