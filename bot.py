import discord, random, os
from discord.ext import commands
from time import sleep


client = commands.Bot(command_prefix = ['Smolin ', 'Panie Profesorze '])

#On ready event
@client.event
async def on_ready():
    print("Bot is ready!!!")
    await client.change_presence(activity = discord.Game('Fedora workstation x86_64'))

#Ładowanie rozszerzeń/loadnig extensions
@client.command(aliases = ['włącz'])
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Włączyłem rozszerzenie "{extension}" [ON]')

#Wyłączanie rozszerzeń/unloading extensions
@client.command(aliases = ['wyłącz'])
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Wyłączyłem rozszerzenie "{extension}" [OFF]')

#Przeładowanywanie rozsrzeń - to prawdziwe/reloading extensions - the real one
@client.command(aliases = ['przeładuj_rly'])
async def reload_rly(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Przeładowałem rozszerzenie "{extension}" [OFF --> ON]')

#Przeładowanywanie rozsrzeń - ten żart - haha, bardzo śmieszne
#reloading extensions - this joke - haha, Lmao, no seriously verry funny AWESOME joke, do you ever consider a comedian job?
@client.command(aliases = ['przeładuj'])
async def reload(ctx, extension):
    if extension + '.py' in os.listdir('./cogs'):
        await ctx.send(f'Sam se przeładuj rozszerzenie "{extension}", co ty sobie myślisz')
        sleep(3)
        await ctx.send(f'( ° ͜ʖ͡°)╭∩╮')
        sleep(3)
        i = 0
        while i<5:
            await ctx.send(f'.')
            sleep(1)
            i+=1
        await ctx.send(f'Już? Poszedłeś sobie? Ochłąnąłeś?')
        sleep(4)
        await ctx.send(f'No zostaw mnie w spokoju już, nic ci nie zrobię rozumiesz, innym studentom też nie pomagałem to tobie nie mogę')
        sleep(5)
        await ctx.send(f'No dobra okej, wygrałeś, przeładuję ci to "{extension}", huh')
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        sleep(2)
        await ctx.send(f'No już zrobione, zadowolony?!')
    else:
        await ctx.send(f'Postradałeś zmysły? Nie ma takiego rozszerzenia jak "{extension}"')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Wiadomość powitalna na konsoli
@client.event
async def on_member_join(member):
    print(f'Witam {member} na dzisiejszych zajęciach z Systemów Operacyjnych')

#Wiadomość pożegnalna na konsoli
@client.event
async def on_member_remove(member):
    print(f'Do zobaczenia {member} w kolejnej edycji kursu :)')



client.run('NzQ4OTg5MTM1Mzk3ODQ3MTAw.X0lcfQ.Y0CHTIHYhr50dzlshMy3iudSDUQ')