from datetime import time
from src.strategy import Strategy
from src.trade_amount import TradeAmount
from src.balance import Balance
from src.log import LOG
from src.sleeper import Sleeper

class Trader:

    def __init__(self, browser, dry_run=False):
        self._browser = browser
        self._trade_amount = TradeAmount(browser)
        self._balance = Balance(browser)
        self._dry_run = dry_run

    def predict_higher(self):
        btn = self._browser.find_element_by_css_selector('#qa_trading_dealUpButton button')
        self.execute(btn)

    def predict_lower(self):
        btn = self._browser.find_element_by_css_selector('#qa_trading_dealDownButton button')
        self.execute(btn)

    def execute(self, btn):
        if not self._dry_run:
            btn.click()

    def trade(self, price, method=Strategy.PREDICT_HIGHER, iteration=1, additional_wait=0) -> Balance:
        self._trade_amount.set_value(price)

        before_trade_balance = self._balance.current_balance
        LOG.trade_start(self._balance.current_balance_str, price, iteration, method)

        if not Sleeper.is_time_to_trade():
            Sleeper.sleep_until_ready()

        if method == Strategy.PREDICT_HIGHER:
            self.predict_higher()
        else:
            self.predict_lower()
        
        Sleeper.sleep_until_ready()
        if additional_wait:
            Sleeper.sleep(additional_wait)

        self._balance.set_previous_balance(before_trade_balance)
        LOG.trade_end(self._balance.current_balance_str, self._balance.profit, self._balance.loss)
        return self._balance
    




