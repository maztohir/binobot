import sys
import time

class LOG:

    def trade_start(balance_str, open_trade_amount, iteration, method):
        print('')
        print('.')
        print('.')
        print(f'---------- TRADE START: ITERATION {iteration} -------------')
        print(f'BALANCE BEFORE TRADE    : {balance_str}')
        print(f'OPEN TRADE AMOUNT       : {open_trade_amount}')
        print(f'METHOD                  : {method}')
        print('.')
        print('.')

    def countdown(second):
        for i in range(second,0,-1):
            sys.stdout.write('\rWaiting ' + str(i) + 's. ')
            sys.stdout.flush()
            time.sleep(1)

    def trade_end(balance_str, profit, loss):
        print('')
        print('.')
        print('.')
        print(f'BALANCE AFTER TRADE     : {balance_str}')
        if profit > 0:
            print(f'{LOGColor.OKGREEN}PROFIT                  : {profit}{LOGColor.ENDC}')
        else:
            print(f'{LOGColor.FAIL}LOSS                    : {loss}{LOGColor.ENDC}')
        print('---------- TRADE END -------------')
        print('')

    def init_strategy():
        print('')
        print('')
        print('-------')
        print('initiating strategy..')
    
    def error(string):
        print(f'{LOGColor.FAIL}{string}{LOGColor.ENDC}')

class LOGColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'