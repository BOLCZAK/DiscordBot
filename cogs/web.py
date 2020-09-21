import discord, random
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from googlesearch import search
from time import sleep

class Web(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Web cog loaded')

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(r"webdriver\chromedriver.exe", chrome_options=options)

    @commands.command(alises = ['jaka_jest_najnowsza_wersja_fedorki?', 'jaka_jest_najnowsza_wersja_fedorki'])
    async def fedora_version(self, ctx):
        browser = Web.driver
        browser.get("https://getfedora.org/pl/")
        tekst = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div/div/div[1]/div/div[2]/div').get_attribute('innerHTML')
        tekst = tekst.replace('&nbsp;', ' ')

        await ctx.send(tekst)

    @commands.command(aliases = ['wyszukaj', 'znajdź', 'znajdz'], help = 'Smolin szuka podanej frazy w google\nSkładnia: "[Prefix] google ilość zapytanie"\nilość - ilość wyników jakie chcemy zobaczyć')
    async def google(self, ctx, amount, *, question):
        # browser = Web.driver
        # browser.get("https://google.pl")
        # browser.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(question)
        # browser.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[3]/center/input[1]').click()
        # output = browser.find_element_by_xpath('/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/a/h3').get_attribute('innerHTML')

        results = search(question, tld="pl", lang="pl", start=0, stop=int(amount), pause=2)

        for index, query in enumerate(results):
            await ctx.send(f'{index+1} wynik wyszukiwania google:\n{query}')
            sleep(1)
        





def setup(client):
    client.add_cog(Web(client))