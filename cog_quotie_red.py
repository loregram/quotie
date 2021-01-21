# -*- coding: utf-8 -*-
"""
Quote Bot
USAGE: !quote -- Prints a random quote from saved list
		!quote <quote text> -- Saves quote to text file
This bot injests quotes and saves them to a txt file along with the
date (YYYYmmdd).
It can then spit out a random quote
*NOTE* delimiter currently set to ,; <-- do not use in quotes

Text file saved in main bot folder

@author Sandeep Vora
Date: 11/20/2020

"""
from redbot.core import commands
import random

filename='test1.txt'   #where quotes will be saved. Will save in main bot directory
triggerword = '!quote' #trigger



class cog_quotie_red(commands.Cog):
#	@commands.command(pass_context=True)
	@commands.Cog.listener()
	async def on_message(self,ctx):
		if ctx.content.startswith(triggerword):
			if ctx.content == triggerword:
				channel = ctx.channel
				f=open(filename,'r')
				responses=f.readlines()
				f.close()
				response = random.choice(responses)
				response=response.split(',;')[-1]
				await channel.send(response)
			else:
				channel = ctx.channel
				quote = ctx.content.replace(triggerword,'')
				f = open(filename,"a+")
				from datetime import date
				now=date.today()
				date=now.strftime("%Y")+now.strftime("%m")+now.strftime("%d")
				f.write(date+',;')
				f.write(quote+'\n')
				f.close()
