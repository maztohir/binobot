from log import LOG

import datetime

class Sleeper:

    def sleep(second):
        LOG.countdown(second)

    def sleep_until_ready():
        current_second = datetime.datetime.now().second
        prepare_time = 60 - current_second
        LOG.countdown(prepare_time + 10)

    def is_time_to_trade():
        return datetime.datetime.now().second <= 25

