# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 23:50:59 2021
init file for redbot
@author: Sandeep
"""

from redbot.core.bot import Red

from .cog_quotie_red import cog_quotie_red


def setup(bot: Red):
    daily = AnnounceDaily(cog_quotie_red)
    bot.add_cog(daily)
    bot.loop.create_task(daily.check_day())