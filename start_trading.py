from src.args import Args

from src.trader import Trader
from src.strategy import Strategy
from src.sleeper import Sleeper
from src.trade_area import TradeArea
from src.log import LOG

from dotenv import load_dotenv
from selenium import webdriver

import os

load_dotenv()
HOST = os.getenv("HOST")
SESSION = os.getenv("SESSION")

args = Args().parse()

browser = webdriver.Remote(command_executor=HOST, desired_capabilities={})
browser.close()
browser.session_id = SESSION

trader = Trader(browser, dry_run=args.dry_run)
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
    if i > 1000:
        break