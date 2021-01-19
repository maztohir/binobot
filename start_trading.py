from selenium import webdriver

from trader import Trader
from strategy import Strategy
from sleeper import Sleeper
from trade_area import TradeArea

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
trade_area = TradeArea(browser)
strategy = Strategy(browser)

# Trade will always start at minute + 5s
if datetime.datetime.now().second >= 25:
    Sleeper.sleep_until_ready()

# if loss, wait until next 2 minutes :)
additional_wait = 0

i = 1
while True: 
    trade_area.clear_area()
    Sleeper.sleep(2)
    balance = trader.trade(strategy.suggested_price, method=strategy.suggested_method, iteration=i, additional_wait=additional_wait)

    if balance.is_loss():
        strategy.add_losses()
        additional_wait = 0

    elif balance.profit == 0:
        additional_wait = 0

    else:
        strategy.current_loss = 0
        additional_wait = 0

    i += 1

    if i > 100:
        break