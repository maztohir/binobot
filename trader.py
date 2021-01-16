from datetime import time
from strategy import Strategy
from trade_amount import TradeAmount
from balance import Balance
from log import LOG
from sleeper import Sleeper

class Trader:

    def __init__(self, browser):
        self._browser = browser
        self._trade_amount = TradeAmount(browser)
        self._balance = Balance(browser)

    def predict_higher(self):
        btn = self._browser.find_element_by_css_selector('#qa_trading_dealUpButton button')
        btn.click()

    def predict_lower(self):
        btn = self._browser.find_element_by_css_selector('#qa_trading_dealDownButton button')
        btn.click()

    def trade(self, price, method=Strategy.PREDICT_HIGHER, iteration=1) -> Balance:
        self._trade_amount.set_value(price)

        before_trade_balance = self._balance.current_balance
        LOG.trade_start(self._balance.current_balance_str, price, iteration)

        if method == Strategy.PREDICT_HIGHER:
            self.predict_higher()
        else:
            self.predict_lower()
        
        # Next Trade will always start at minute + 5s
        Sleeper.sleep_until_ready()

        self._balance.set_previous_balance(before_trade_balance)
        LOG.trade_end(self._balance.current_balance_str, self._balance.profit, self._balance.loss)
        return self._balance
    




