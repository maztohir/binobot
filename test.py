from selenium import webdriver

from src.trader import Trader
from src.strategy import Strategy
from src.sleeper import Sleeper
from src.trade_amount import TradeAmount

from dotenv import load_dotenv

import os
import datetime

load_dotenv()
HOST = os.getenv("HOST")
SESSION = os.getenv("SESSION")

browser = webdriver.Remote(command_executor=HOST, desired_capabilities={})
browser.close()
browser.session_id = SESSION


strategy = Strategy(browser)
trade_amount = TradeAmount(browser)

for i in range(20):
    trade_amount.set_value(strategy.suggested_price)
    strategy.add_losses()