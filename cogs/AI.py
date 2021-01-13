from discord.ext import commands
import random


def setup(bot):
    bot.add_cog(AI(bot))


class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bitch(self, ctx):
        member = ctx.author
        await ctx.send('Hello {0.name}, you bitch.'.format(member))

    @commands.command()
    async def quote(self, ctx, arg):
        User = self.bot.masterframe.loc[self.bot.masterframe["Author"].str.lower().str.contains(arg.lower())]
        User = User.reset_index()
        del User['index']

        await ctx.send(User.iloc[random.randint(0, User.shape[0] - 1), 0])
