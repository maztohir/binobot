from selenium.webdriver.common.keys import Keys
from log import LOG

from retrying import retry
class TradeAmount:

    def __init__(self, browser):
        self._browser = browser
    
    def set_value(self, value):
        self._set_value(value)
    
    @retry(wait_fixed=1000, stop_max_attempt_number=5)
    def _set_value(self, value):
        amount_value = self._browser.find_element_by_css_selector('#amount-counter input')
        amount_value.send_keys(Keys.COMMAND + "a" + Keys.DELETE)
        amount_value.send_keys(value)
        LOG.countdown(1)
        print(f'Setting trade amount to {value}')
        if value != int(self.get_value()):
            LOG.error(f'Failed to set amount to {value}, retrying...')
            raise Exception('Failed to change trade amount. Aborting mission.')

    def get_value(self):
        amount_value = self._browser.find_element_by_css_selector('#amount-counter input')
        return amount_value.get_attribute('value')
