from selenium import webdriver

from trader import Trader
from strategy import Strategy
from sleeper import Sleeper
from trade_area import TradeArea
from log import LOG

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

i = 1
while True: 
    LOG.init_strategy()
    trade_area.clear_area()
    Sleeper.sleep(2)

    balance = trader.trade(strategy.suggested_price, method=strategy.suggested_method, iteration=i, additional_wait=strategy.additional_wait)

    strategy.response_result(balance)

    i += 1
    if i > 100:
        break