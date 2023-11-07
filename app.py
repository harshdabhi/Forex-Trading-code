from Trading_file.hedge_trade import trading_metatrader
import time

mt=trading_metatrader()
print("Execution started")

def task(sleep_time):
    """
        A function that performs a series of actions in a loop.

        This function does the following:
        1. Closes any open position using the `close_position` method.
        2. Buys a position using the `buy_position` method.
        3. Sells a position using the `sell_position` method.
        4. Waits for 30 seconds using the `time.sleep` function.
        5. Cancels any pending orders using the `cancel_pending` method.

        This function does not take any parameters and does not return any values.
    """
    mt.close_position()   ### close any position if any one is open 
    mt.buy_position()     ### buy position
    mt.sell_position()    ### sell position
    time.sleep(sleep_time)
    mt.cancel_pending()   ### cancel pending orders


if __name__ == "__main__":
    i=0
    sleep_time = 25
    while True:
        i+=1
        task(sleep_time)
        print(f"Execution completed {i}")
    

