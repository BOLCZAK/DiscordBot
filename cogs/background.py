import discord
from discord.ext import commands, tasks

class Background(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Background cog loaded')

    @tasks.loop(seconds = 10.0)
    async def mow(self, ctx):
        print(f'Mówię')
        await ctx.send(f'Mowie')

    @commands.command()
    async def start_loop(self, ctx):
        self.mow.start()

    @commands.command()
    async def stop_loop(self, ctx):
        self.mow.cancel()

    


def setup(client):
    client.add_cog(Background(client))