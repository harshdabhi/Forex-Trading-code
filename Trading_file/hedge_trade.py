import MT1 as mt1
import MT2 as mt2
from constant import *
import time

class trading_metatrader:
    


    def __init__(self,path1:str=path1,path2:str=path2,login1:int=login1,password1:str=password1,login2:int=login2,
                 password2:str=password2,server:str=server,symbol:str=symbol,lot:int=lot,deviation:int=deviation,perct:int=perct) -> None:
        
        '''
                Initializes the class with the given parameters.

                Args:
                    path1 (str): The path for the first MT5 connection.
                    path2 (str): The path for the second MT5 connection.
                    login1 (int): The login ID for the first MT5 connection.
                    password1 (str): The password for the first MT5 connection.
                    login2 (int): The login ID for the second MT5 connection.
                    password2 (str): The password for the second MT5 connection.
                    server (str): The server for the MT5 connections.
                    symbol (str): The symbol for the trading.
                    lot (int): The lot size for the trading.
                    deviation (int): The deviation for the trading.
                    perct (int): The percentage for the trading.

                Returns:
                    None
                
        '''
    
        self.server=server
        self.symbol=symbol

        mt1.initialize(path1)
        self.login1=login1
        self.password1=password1
        mt1.login(self.login1,self.password1,self.server)

        mt2.initialize(path2)
        self.login2=login2
        self.password2=password2
        mt2.login(self.login2, self.password2,self.server)

        self.lot=lot
        self.deviation=deviation
        self.perct=perct




    def buy_position(self):
        """
            Buys a position in the market.

            Parameters:
            None

            Returns:
            None
        """

        point = mt1.symbol_info(self.symbol).point
        price = mt1.symbol_info_tick(self.symbol).bid
   

        price=price-self.deviation
        request_buy={
        "action": mt1.TRADE_ACTION_PENDING,
        "symbol": self.symbol,
        "volume": self.lot,
        "type": mt1.ORDER_TYPE_BUY_LIMIT,
        "sl": price - self.perct * point,
        "tp": price + self.perct * point,
        "price": price,
        "comment": "python script open",
        "type_time": mt1.ORDER_TIME_GTC,
        "type_filling": mt1.ORDER_FILLING_IOC,
    }

        result_buy=mt1.order_send(request_buy)
        

    def sell_position(self,):

        """
            Sell a position in the market.

            Parameters:
            None

            Returns:
            None
        """
        point = mt2.symbol_info(self.symbol).point
        price = mt2.symbol_info_tick(self.symbol).bid
   

        price=price-self.deviation
        request_buy={
        "action": mt2.TRADE_ACTION_PENDING,
        "symbol": self.symbol,
        "volume": self.lot,
        "type": mt2.ORDER_TYPE_SELL_STOP,
        "sl": price + self.perct * point,
        "tp": price - self.perct * point,
        "price": price,
        "comment": "python script open",
        "type_time": mt2.ORDER_TIME_GTC,
        "type_filling": mt2.ORDER_FILLING_IOC,
    }

        result_sell=mt2.order_send(request_buy)
        
        

    def close_position(self,):

        """
        Closes the positions in the symbol.

        Parameters:
            None

        Returns:
            None
        """
        position1=mt2.positions_get(symbol=self.symbol)
        position2=mt1.positions_get(symbol=self.symbol)

        if position1 and position2!=():
            pass

        else:

            list_close_position1=[i.ticket for i in position1]
            list_close_position2=[i.ticket for i in position2]



            try:
                for position_ticket_id_1 in list_close_position1:
                    mt2.Close(symbol=self.symbol,ticket=position_ticket_id_1)

                for position_ticket_id_2 in list_close_position2:
                    mt1.Close(symbol=self.symbol,ticket=position_ticket_id_2) 
            
            except Exception as e:
                print(e)
                pass
        

    def cancel_pending(self,):
        
        pending_position_1=mt1.orders_get(symbol=self.symbol)
        list_position_1=[i.ticket for i in pending_position_1 ]
        

        for ticket_id in list_position_1:

                request={  
                'action':mt1.TRADE_ACTION_REMOVE,                
                'order':ticket_id
                }
                mt1.order_send(request)

        
        pending_position_2=mt2.orders_get(symbol=self.symbol)
        list_position_2=[i.ticket for i in pending_position_2]
        

        for ticket_id in list_position_2:

                request={  
                'action':mt2.TRADE_ACTION_REMOVE,                
                'order':ticket_id
                }
                mt2.order_send(request)

