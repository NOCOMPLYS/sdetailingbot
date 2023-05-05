from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import logging

import os

'''
logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)
'''

bot = Bot('5911733872:AAE3UkEYGbtIbghpZxCGqGaEpO2xy0MWwho') # token=os.getenv('TOKEN')
dp = Dispatcher(bot)