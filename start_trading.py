from selenium import webdriver

from trader import Trader
from strategy import Strategy
from sleeper import Sleeper

from dotenv import load_dotenv

import os
import datetime

load_dotenv()
HOST = os.getenv("HOST")
SESSION = os.getenv("SESSION")

browser = webdriver.Remote(command_executor=HOST, desired_capabilities={})
browser.close()
browser.session_id = SESSION

trader = Trader(browser)
strategy = Strategy()

# Trade will always start at minute + 5s
if datetime.datetime.now().second >= 25:
    Sleeper.sleep_until_ready()

i = 1
while True: 
    balance = trader.trade(strategy.suggested_price, method=strategy.suggested_method, iteration=i)

    if balance.is_loss():
        strategy.add_losses()
    else:
        strategy.current_loss = 0

    i += 1

    if i > 100:
        break