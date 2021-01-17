class Strategy:

    TRADE_INITIAL_AMOUNT = 14000
    PREDICT_HIGHER = 'predict_higher'
    PREDICT_LOWER = 'predict_lower'
    MAXIMUM_COMPENSATION_TIME = 3

    def __init__(self, browser):
        self.current_loss = 0
        self.current_price = self.TRADE_INITIAL_AMOUNT
        self._browser = browser

    @property
    def suggested_price(self):
        return self.TRADE_INITIAL_AMOUNT * (2 ** self.current_loss)

    @property
    def suggested_method(self):
        if self.is_high_chance_to_be_negative():
            return self.PREDICT_LOWER
        else:
            return self.PREDICT_HIGHER

    @property
    def positive_ratio(self):
        positive_ratio = self._browser.find_element_by_css_selector('majority-opinion .ratio_positive__1qpzL')
        ratio_str = positive_ratio.text
        return int(ratio_str.replace(' ','').replace('%',''))

    def is_high_chance_to_be_positive(self):
        return self.positive_ratio > 75
    
    def is_high_chance_to_be_negative(self):
        negative_ratio = 100 - self.positive_ratio
        return negative_ratio > 75

    def add_losses(self):
        if self.current_loss >= self.MAXIMUM_COMPENSATION_TIME:
            self.current_loss = 0
        else:
            self.current_loss += 1
