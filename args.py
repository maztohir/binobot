import argparse

class Args:
    def __init__(self):
        self._parser = argparse.ArgumentParser(description='Trading option')

    def parse(self):
        self._parser.add_argument('--dry-run', dest='dry_run', action='store_true', help="to dry run the trading")
        args = self._parser.parse_args()
        return args