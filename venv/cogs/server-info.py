import discord
from discord.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="server-info")
    async def server_info(self, ctx):
        """Sends server information"""
        embed = discord.Embed(
            title="PDM SMP",
            description="IP: *thepleroma.aternos.me*\nPort: *36259*",
            color=0x99e868
        )
        embed.set_thumbnail(url="https://i.imgur.com/whUqmAx.png")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
        embed.timestamp = discord.utils.utcnow()

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ServerInfo(bot))
