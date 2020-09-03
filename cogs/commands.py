import discord, random
from discord.ext import commands
from time import sleep

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Commands cog loaded')

    #Zdam sysopa?
    @commands.command(aliases=['czy_zdam_sysopa?', 'panie_profesorze_czy_zdam_sysopa?', 'czy_on_zda?', 'czy_zdam?'])
    async def czy_zdam(self, ctx, student = ''):
        responses = ['Jasne!!!', 'Zobaczymy', 'Raczej bym się nie spodziewał', 'Chwila chwila, spokojnie, to się okaże', 'Ty? Haha']
        responses_student = [f'{student} oj z nim to może być ciężko', f'{student} no on to jest ciekawy przypadek', f'{student} napewno ma większe szanse niż pan, panie {str(ctx.author)[:-5]}']
        if student=='':
            await ctx.send(random.choice(responses))
        else:
            await ctx.send(random.choice(responses_student))

    #Smoli uczy się liczyć
    @commands.command()
    async def licz(self, ctx, amount = 5):
        buf = amount
        while amount > 0:
            await ctx.send(f'Elo mordo #{buf-amount}')
            sleep(1)
            amount-=1

    #Smoli mnoży, i nie da się oszukać
    @commands.command(aliases=['mnóż'])
    async def mnoz(self, ctx, xvalue = 1.0, yvalue = 1.0):
        await ctx.send(f'Wynik mnożenia to: {xvalue*yvalue} nie oszukasz mnie')

    #Smoli czyści czat
    @commands.command(aliases = ['czyść'])
    async def clear(self, ctx, amount = 5):
        if amount == 0:
            await ctx.send('0 Nie jest poprawną wartością (Co ty chcesz usnąć zero wiadomości? To ma wgl jakiś sens?)')
        else:
            await ctx.channel.purge(limit = amount+1)

    #Smoli wykopuje z zajęć
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason = reason)
        await ctx.send(f'Żeganmy Pana {member} z dzisiejszych zajęć Systemów Operacyjnych z powodu {reason}, sam Pan sobie na to zasłużył')
        print(f'{member} został wyrzucony z powodu: {reason}')
            #await ctx.send(f'Nie ma takiego użytkownika proszę Pana, może już zakończył tą edycję kursu?')
            #print(f'Nie ma takiego użytkownika proszę Pana, może już zakończył tą edycję kursu?')
        await ctx.send(str(discord.ext.commands.errors.BadArgument))

    @commands.command(help = 'Zmienia status Imperatora\nSkładnia: "[Prefix] status atrybut nazwa_statusu"\natrybut 1 - gra, 2 - film (Must be an integer)')
    async def status(self, ctx, atrybut : int, *, status):
        if int(atrybut)==1:
            await self.client.change_presence(activity = discord.Game(status))
        if int(atrybut)==2:
            await self.client.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name = status))

    @status.error
    async def status_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Podaj wszytskie wymagane argumenty, po więcej informacji użyj --> [Prefix] help status')
        if isinstance(error, commands.BadArgument):
            await ctx.send(f'Podaj odpowiedni typ argumentu, po więcej informacji użyj --> [Prefix] help status')
        

def setup(client):
    client.add_cog(Commands(client))