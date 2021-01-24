import selenium


class Balance:

    def __init__(self, browser):
        self._browser = browser
        self._previous_balance = 0

    @property
    def current_balance_str(self):
        balance = self._browser.find_element_by_id('qa_trading_balance')
        return balance.text
    
    @property
    def current_balance(self):
        balance_value = self.current_balance_str.lower().replace('rp','').replace('.00','').replace(',','')
        return float(balance_value)

    def set_previous_balance(self, value):
        self._previous_balance = value

    @property
    def profit(self):
        return self.current_balance - self._previous_balance

    @property
    def loss(self):
        return self._previous_balance - self.current_balance
    
    def is_profit(self):
        return self.profit > 0

    def is_not_losses(self):
        return self.profit >= 0

    def is_loss(self):
        return self.loss > 0