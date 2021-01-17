class Strategy:

    TRADE_INITIAL_AMOUNT = 14000
    PREDICT_HIGHER = 'predict_higher'
    PREDICT_LOWER = 'predict_lower'

    def __init__(self):
        self.current_loss = 0
        self.current_price = self.TRADE_INITIAL_AMOUNT

    @property
    def suggested_price(self):
        return self.TRADE_INITIAL_AMOUNT * (2 ** self.current_loss)

    @property
    def suggested_method(self):
        return self.PREDICT_HIGHER

    def add_losses(self):
        
        if self.current_loss > 2:
            self.current_loss = 0
        else:
            self.current_loss += 1
