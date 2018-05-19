
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import feedparser


client = Bot(description="Newsbot by Kat", command_prefix="news-", pm_help = False)


@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	return await client.change_presence(game=discord.Game(name='PLAYING STATUS HERE')) 


@client.command()
async def world(*args):
	d = feedparser.parse('https://www.economist.com/rss/the_world_this_week_rss.xml')
	link = d['entries'][2]['id']
	await client.say(link)
	await asyncio.sleep(3)

@client.command()
async def china(*args):
	d = feedparser.parse('https://www.economist.com/sections/china/rss.xml')
	link1 = d['entries'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['entries'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['entries'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['entries'][3]['link']
	await client.say(link4)

@client.command()
async def us(*args):
	d = feedparser.parse('https://www.economist.com/sections/united-states/rss.xml')
	link1 = d['entries'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['entries'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['entries'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['entries'][3]['link']
	await client.say(link4)

@client.command()
async def americas(*args):
	d = feedparser.parse('https://www.economist.com/sections/americas/rss.xml')
	link1 = d['entries'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['entries'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['entries'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['entries'][3]['link']
	await client.say(link4)

@client.command()
async def tech(*args):
	d = feedparser.parse('https://www.economist.com/sections/science-technology/rss.xml')
	link1 = d['entries'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['entries'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['entries'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['entries'][3]['link']
	await client.say(link4)

@client.command()
async def more_tech(*args):
	d = feedparser.parse('https://www.economist.com/sections/science-technology/rss.xml')
	link5 = d['entries'][4]['link']
	await client.say(link5)
	await asyncio.sleep(3)
	link6 = d['entries'][5]['link']
	await client.say(link6)
	await asyncio.sleep(3)
	link7 = d['entries'][6]['link']
	await client.say(link7)
	await asyncio.sleep(3)
	link8 = d['entries'][7]['link']
	await client.say(link8)

@client.command()
async def econ(*args):
	d = feedparser.parse('https://www.economist.com/sections/economics/rss.xml')
	link1 = d['entries'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['entries'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['entries'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['entries'][3]['link']
	await client.say(link4)


@client.command()
async def britain(*args):
	d = feedparser.parse('https://www.economist.com/sections/britain/rss.xml')
	link1 = d['entries'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['entries'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['entries'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['entries'][3]['link']
	await client.say(link4)

@client.command()
async def culture(*args):
	d = feedparser.parse('https://www.economist.com/sections/culture/rss.xml')
	link1 = d['entries'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['entries'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['entries'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['entries'][3]['link']
	await client.say(link4)

@client.command()
async def more_culture(*args):
	d = feedparser.parse('https://www.economist.com/sections/culture/rss.xml')
	link5 = d['entries'][4]['link']
	await client.say(link5)
	await asyncio.sleep(3)
	link6 = d['entries'][5]['link']
	await client.say(link6)
	await asyncio.sleep(3)
	link7 = d['entries'][6]['link']
	await client.say(link7)
	await asyncio.sleep(3)
	link8 = d['entries'][7]['link']
	await client.say(link8)

@client.command()
async def africa(*args):
	d = feedparser.parse('https://www.economist.com/sections/middle-east-africa/rss.xml')
	link1 = d['entries'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['entries'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['entries'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['entries'][3]['link']
	await client.say(link4)

@client.command()
async def europe(*args):
	d = feedparser.parse('https://www.economist.com/sections/europe/rss.xml')
	link1 = d['entries'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['entries'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['entries'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['entries'][3]['link']
	await client.say(link4)

@client.command()
async def asia(*args):
	d = feedparser.parse('https://www.economist.com/sections/asia/rss.xml')
	link1 = d['entries'][0]['link']
	await client.say(link1)
	await asyncio.sleep(3)
	link2 = d['entries'][1]['link']
	await client.say(link2)
	await asyncio.sleep(3)
	link3 = d['entries'][2]['link']
	await client.say(link3)
	await asyncio.sleep(3)
	link4 = d['entries'][3]['link']
	await client.say(link4)

@client.command()
async def help(*args):
	await client.say("news-asia")
	await client.say("news-europe")
	await client.say("news-us")
	await client.say("news-world")
	await client.say("news-africa")
	await client.say("news-tech")
	await client.say("news-culture")
	await client.say("news-econ")

@client.command()
async def npr(*args):

client.run('NDQ3MjEwMTY2MzcxMjIxNTE0.DeER4w.kjDIBnRfyI67C9G26uQW21fT3Aw')

