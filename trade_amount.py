from selenium.webdriver.common.keys import Keys
from log import LOG

class TradeAmount:

    def __init__(self, browser):
        self._browser = browser
    
    def set_value(self, value):
        amount_value = self._browser.find_element_by_css_selector('#amount-counter input')
        amount_value.send_keys(Keys.COMMAND + "a" + Keys.DELETE)
        amount_value.send_keys(value)
        LOG.countdown(2)
        print(' setting trade amount to '+str(value))
        assert value == int(self.get_value())

    def get_value(self):
        amount_value = self._browser.find_element_by_css_selector('#amount-counter input')
        return amount_value.get_attribute('value')
