import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import feedparser


client = Bot(description="Newsbot by Kat", command_prefix="!", pm_help = False)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Made by Kate Kulinski')
	return await client.change_presence(game=discord.Game(name='Reading!'))

@client.command()
async def politics(*args):
	d = feedparser.parse('https://www.economist.com/the-world-this-week/rss.xml')
	link = d['items'][1]['link']
	await client.say(link)
	await asyncio.sleep(3)

@client.command()
async def business(*args):
	d = feedparser.parse('https://www.economist.com/the-world-this-week/rss.xml')
	link = d['items'][0]['link']
	await client.say(link)
	await asyncio.sleep(3)

@client.command()
async def china(*args):
	d = feedparser.parse('https://www.economist.com/china/rss.xml')
	link1 = d['items'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['items'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['items'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['items'][3]['link']
	await client.say(link4)

@client.command()
async def us(*args):
	d = feedparser.parse('https://www.economist.com/united-states/rss.xml')
	link1 = d['items'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['items'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['items'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['items'][3]['link']
	await client.say(link4)

@client.command()
async def americas(*args):
	d = feedparser.parse('https://www.economist.com/the-americas/rss.xml')
	link1 = d['items'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['items'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['items'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['items'][3]['link']
	await client.say(link4)

@client.command()
async def tech(*args):
	d = feedparser.parse('https://www.economist.com/science-and-technology/rss.xml')
	link1 = d['items'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['items'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['items'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['items'][3]['link']
	await client.say(link4)

@client.command()
async def more_tech(*args):
	d = feedparser.parse('https://www.economist.com/science-and-technology/rss.xml')
	link5 = d['items'][4]['link']
	await client.say(link5)
	await asyncio.sleep(3)
	link6 = d['items'][5]['link']
	await client.say(link6)
	await asyncio.sleep(3)
	link7 = d['items'][6]['link']
	await client.say(link7)
	await asyncio.sleep(3)
	link8 = d['items'][7]['link']
	await client.say(link8)

@client.command()
async def econ(*args):
	d = feedparser.parse('https://www.economist.com/finance-and-economics/rss.xml')
	link1 = d['items'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['items'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['items'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['items'][3]['link']
	await client.say(link4)


@client.command()
async def britain(*args):
	d = feedparser.parse('https://www.economist.com/britain/rss.xml')
	link1 = d['items'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['items'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['items'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['items'][3]['link']
	await client.say(link4)

@client.command()
async def africa(*args):
	d = feedparser.parse('https://www.economist.com/middle-east-and-africa/rss.xml')
	link1 = d['items'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['items'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['items'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['items'][3]['link']
	await client.say(link4)

@client.command()
async def middle(*args):
	d = feedparser.parse('https://www.economist.com/middle-east-and-africa/rss.xml')
	link1 = d['items'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['items'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['items'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['items'][3]['link']
	await client.say(link4)

@client.command()
async def europe(*args):
	d = feedparser.parse('https://www.economist.com/europe/rss.xml')
	link1 = d['items'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['items'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['items'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['items'][3]['link']
	await client.say(link4)

@client.command()
async def asia(*args):
	d = feedparser.parse('https://www.economist.com/asia/rss.xml')
	link1 = d['items'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['items'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['items'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['items'][3]['link']
	await client.say(link4)


@client.command()
async def guide(*args):
	guide = '''
	**NEWSIE COMMANDS**
	!asia = Asia
	!middle = Middle East 
	!americas = Americas
	!china = China 
	!us = United States
	!europe = Europe
	!africa = Africa
	!econ = Economics/Financial 
	!business = Business this week
	!politics = Politics this week
	!tech = Technology
	
	'''
	await client.say(guide)

client.run('')
