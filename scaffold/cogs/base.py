from discord.ext import commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="me", hidden=True)
    @commands.is_owner()
    async def only(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}")

    @commands.command(name="hello", hidden=True)
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}")

    @commands.group(
        aliases=["e"], pass_context=True, invoke_without_command=True, hidden=True
    )
    @commands.is_owner()
    async def ext(self, ctx):
        cogs = list(self.bot.extensions.keys())
        for index, cog in enumerate(cogs):
            cogs[index] = cog.replace("scaffold.cogs.", "")

        msg = "```fix\nLoaded Extensions:\n--------\n{}```".format(" ".join(cogs))
        user = await self.bot.fetch_user(ctx.message.author.id)
        await user.send(msg)

    @ext.group(aliases=["unload"], pass_context=True)
    @commands.is_owner()
    async def unload_ext(self, ctx, *args):
        self.bot.unload_extension("scaffold.cogs." + args[0])

    @ext.group(aliases=["load"], pass_context=True)
    @commands.is_owner()
    async def load_ext(self, ctx, *args):
        self.bot.load_extension("scaffold.cogs." + args[0])


def setup(bot):
    bot.add_cog(Base(bot))
