import discord, random
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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





def setup(client):
    client.add_cog(Web(client))