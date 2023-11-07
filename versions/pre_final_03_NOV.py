import MetaTrader5 as mt
import MT2 as mt2
from datetime import datetime
import time

mt2.initialize("C:\\Program Files\\MetaTrader 5\\terminal64.exe")
login=6060502348
password="+cP4FbZf"
server="ArkGlobal-Server"
mt2.login(login, password, server)

mt.initialize("C:/Program Files/MetaTrader2/terminal64.exe")
login=6060502347
password="V@DlJd3d"
server="ArkGlobal-Server"
mt.login(login, password, server)




def task():
    
    symbol="XAUUSD.r"
    lot=0.5
    point = mt.symbol_info(symbol).point
    price = mt.symbol_info_tick(symbol).bid
    deviation=0.25
    p=45

    print(price,point)

    request_buy={
        "action": mt.TRADE_ACTION_PENDING,
        "symbol": symbol,
        "volume": lot,
        "type": mt.ORDER_TYPE_BUY_LIMIT,
        "sl": price - p * point,
        "tp": price + p * point,
        "price": price-deviation,
        "comment": "python script open",
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC,
    }

    # request_buy={
    #     "action": mt.TRADE_ACTION_DEAL,
    #     "symbol": symbol,
    #     "volume": lot,
    #     "type": mt.ORDER_TYPE_BUY,
    #     "sl": price - 100 * point,
    #     "tp": price + 100 * point,
    #     "price": price,
    #     "comment": "python script open",
    #     "type_time": mt.ORDER_TIME_GTC,
    #     "type_filling": mt.ORDER_FILLING_IOC,
    # }
    # send a trading request
    result_buy=mt.order_send(request_buy)




    # price=mt.symbol_info_tick(symbol).ask
    price=mt2.symbol_info_tick(symbol).bid

    request_sell={
        "action": mt2.TRADE_ACTION_PENDING,
        "symbol": symbol,
        "volume": lot,
        "type": mt2.ORDER_TYPE_SELL_STOP,
        "sl": price + p * point,
        "tp": price - p* point,
        "price": price-deviation,
        "comment": "python script open",
        "type_time": mt2.ORDER_TIME_GTC,
        "type_filling": mt2.ORDER_FILLING_IOC,
    }
    # send a trading request
    result_sell=mt2.order_send(request_sell)




    a= mt.positions_get(symbol=symbol)
    print(result_buy)
    print(result_sell)
    print(mt.positions_total()) 
    print(mt.positions_get(symbol=symbol))

    time.sleep(20)
    print(mt.orders_get())


    a=mt.orders_get(symbol=symbol)
    list1=[]
    for i in a:
        ticket=i.ticket
        list1.append(ticket)
    

    for ticket_id in list1:

            request={  
            'action':mt.TRADE_ACTION_REMOVE,                
            'order':ticket_id
            }
            mt.order_send(request)

    
    b=mt2.orders_get(symbol=symbol)
    list1=[]
    for i in b:
        ticket=i.ticket
        list1.append(ticket)
    

    for ticket_id in list1:

            request={  
            'action':mt2.TRADE_ACTION_REMOVE,                
            'order':ticket_id
            }
            mt2.order_send(request)







# request.action=TRADE_ACTION_CLOSE_BY;                         
# request.position=position_ticket;                             
# request.position_by=PositionGetInteger(POSITION_TICKET); 

    def get_ticket(symbol):
        a=mt.positions_get(symbol=symbol)
        list1=[]
        for i in a:
            ticket=i.ticket
            list1.append(ticket)
        return ticket
            

    def remove_order_pending(symbol):  

        for ticket_id in get_ticket(symbol):

            request={  
            'action':mt.TRADE_ACTION_REMOVE,                
            'order':ticket_id
            }
            result=mt.order_send(request)
            return result
        
    # position = mt.positions_get(symbol=symbol, ticket=ticket)
    # print(position)
    #         

if __name__ == "__main__":
     i=0
     while True:
        task()
        i+=1
        if i>30:
            break
