from balance import Balance
class Strategy:

    TRADE_INITIAL_AMOUNT = 20000
    PREDICT_HIGHER = 'predict_higher'
    PREDICT_LOWER = 'predict_lower'
    MAXIMUM_LOSSES = 3
    MAJORITY_OPINION_SCORE_TOLLERANCE = 70
    COMPENSATION_TIME = 2.2

    def __init__(self, browser):
        self.current_loss = 0
        self.current_price = self.TRADE_INITIAL_AMOUNT
        self._browser = browser
        self._have_buy = False
        self.additional_wait = 0

    @property
    def suggested_price(self):
        calculated_price = self.TRADE_INITIAL_AMOUNT * (self.COMPENSATION_TIME ** self.current_loss)
        return round(calculated_price)

    @property
    def suggested_method(self):
        if self.is_high_chance_to_be_positive():
            print('Follow majority open to higher')
            return self.PREDICT_HIGHER
        elif self.is_high_chance_to_be_negative():
            print('Follow majority open to lower')
            return self.PREDICT_LOWER
        else:
            print('Decide to use default method to open')
            return self.default_method

    @property
    def default_method(self):
        if not self._have_buy:
            self._have_buy = True
            print('Open higher')
            return self.PREDICT_HIGHER
        else:
            self._have_buy = False
            print('Open lower')
            return self.PREDICT_LOWER

    @property
    def positive_ratio(self):
        positive_ratio = self._browser.find_element_by_css_selector('majority-opinion .ratio_positive__1qpzL')
        ratio_str = positive_ratio.text
        return int(ratio_str.replace(' ','').replace('%',''))

    def is_high_chance_to_be_positive(self):
        return self.positive_ratio > self.MAJORITY_OPINION_SCORE_TOLLERANCE
    
    def is_high_chance_to_be_negative(self):
        negative_ratio = 100 - self.positive_ratio
        return negative_ratio > self.MAJORITY_OPINION_SCORE_TOLLERANCE

    def add_losses(self):
        if self.current_loss < self.MAXIMUM_LOSSES-1:
            self.current_loss += 1
        else:
            self.current_loss = 0

    def response_result(self, balance:Balance):
        if balance.is_loss():
            self.add_losses()
            self.additional_wait = 0

        elif balance.profit == 0:
            self.additional_wait = 0

        else:
            self.current_loss = 0
            self.additional_wait = 0