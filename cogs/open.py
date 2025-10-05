import discord
from discord.ext import commands
from python_aternos import Client
from python_aternos.aterrors import ServerStartError

class OpenServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="open")
    async def open_server(self, ctx):
        """Opens Aternos and starts the server"""
        embed = discord.Embed(
            title="🔗 Starting The Server....",
            description="Please wait while the bot sets up the server",
            color=0x0099ff
        )
        embed.set_footer(text="Bot Made by Triz")
        await ctx.send(embed=embed)

        try:
            # Connect to Aternos
            atclient = Client()
            atclient.login("AternosAutoRunBot", "ZzRJGVmvtCisrL2")  # replace with ENV later!
            aternos = atclient.account

            # Fix duplicate cookies
            cookies = aternos.atconn.session.cookies
            matches = [c for c in cookies if c.name == "ATERNOS_SESSION"]
            if len(matches) > 1:
                for c in matches[:-1]:
                    cookies.clear(c.domain, c.path, c.name)

            # Get first server
            servs = aternos.list_servers()
            myserv = servs[0]
            myserv.fetch()
            
            # Try starting
            try:
                myserv.start()
                myserv.fetch()
                status_embed = discord.Embed(
                    title="✅ Server Start Initiated",
                    description=f"Server **{myserv.address}** is starting...",
                    color=0x00ff00
                )
                status_embed.set_author(name="Aternos Server", icon_url="https://img.icons8.com/?size=64&id=KiENMF6j1Utp&format=png")
                status_embed.set_thumbnail(url="https://img.icons8.com/?size=64&id=Ua9vviRaZ8xY&format=png")
                status_embed.set_footer(text=f"Opened by {ctx.author}")
                await ctx.send(embed=status_embed)

            except ServerStartError:
                error_embed = discord.Embed(
                    title="⚠️ Server Start Status",
                    description=f"Failed to start {myserv.address}. Server might already be running.",
                    color=0xff0000
                )
                error_embed.set_author(name="Aternos Server", icon_url="https://img.icons8.com/?size=64&id=KiENMF6j1Utp&format=png")
                error_embed.set_thumbnail(url="https://img.icons8.com/?size=64&id=Ua9vviRaZ8xY&format=png")
                error_embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.send(embed=error_embed)

        except Exception as e:
            error_embed = discord.Embed(
                title="⚠️ General Error",
                description=f"Could not start server: `{str(e)}`",
                color=0xff0000
            )
            error_embed.set_author(name="Aternos Server", icon_url="https://img.icons8.com/?size=64&id=KiENMF6j1Utp&format=png")
            error_embed.set_thumbnail(url="https://img.icons8.com/?size=64&id=Ua9vviRaZ8xY&format=png")
            error_embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=error_embed)

async def setup(bot):
    await bot.add_cog(OpenServer(bot))
