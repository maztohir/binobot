class TradeArea:

    def __init__(self, browser):
        self._browser = browser

    
    def clear_area(self):
        try:
            btns = self._browser.find_elements_by_css_selector('.new-toast_close__1DODS')
            for btn in btns:
                btn.click()

            btns = self._browser.find_elements_by_css_selector('.modal_close__1Jjbf')
            for btn in btns:
                btn.click()
        except:
            pass
