import MT1 as mt
import MT2 as mt2
from datetime import datetime
import time

mt2.initialize("C:/Program Files/MetaTrader 5/terminal64.exe")
login=6060502347
password="V@DlJd3d"
# login=6060502348
# password="+cP4FbZf"
server="ArkGlobal-Server"
mt2.login(login, password, server)

mt.initialize("C:/Program Files/MetaTrader2/terminal64.exe")
# login=6060502347
# password="V@DlJd3d"
login=6060502348
password="+cP4FbZf"
server="ArkGlobal-Server"
mt.login(login, password, server)


print("Execution has started !!")

def task():
    symbol="XAUUSD.r"
    position1=mt2.positions_get(symbol="XAUUSD.r")
    position2=mt.positions_get(symbol="XAUUSD.r")
    print(position1,position2)

    if position1 and position2!=():
        pass

    else:
        print('executing else statement')
        list_close_position1=[]
        for i in position1:
            ticket=i.ticket
            list_close_position1.append(ticket)
        
        list_close_position2=[]
        for j in position2:
            ticket=j.ticket
            list_close_position2.append(ticket)

        print(list_close_position1,list_close_position2)

        try:
            for position_ticket_id_1 in list_close_position1:
                mt2.Close(symbol='XAUUSD.r',ticket=position_ticket_id_1)

            for position_ticket_id_2 in list_close_position2:
                mt.Close(symbol='XAUUSD.r',ticket=position_ticket_id_2) 
        
        except Exception as e:
             print(e)
             pass
    



    symbol="XAUUSD.r"
    lot=0.1
    point = mt.symbol_info(symbol).point
    price = mt.symbol_info_tick(symbol).bid
    deviation=0.25  # old value 0.25
    p=45
    sleep_time=30
    volatile=False

    price=price-deviation

     


    request_buy={
        "action": mt.TRADE_ACTION_PENDING,
        "symbol": symbol,
        "volume": lot,
        "type": mt.ORDER_TYPE_BUY_LIMIT,
        "sl": price - p * point,
        "tp": price + p * point,
        "price": price,
        "comment": "python script open",
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC,
    }

    result_buy=mt.order_send(request_buy)


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
    #result_buy=mt.order_send(request_buy)




    # price=mt.symbol_info_tick(symbol).ask
    price=mt2.symbol_info_tick(symbol).bid
    price=price-deviation

    request_sell={
        "action": mt2.TRADE_ACTION_PENDING,
        "symbol": symbol,
        "volume": lot,
        "type": mt2.ORDER_TYPE_SELL_STOP,
        "sl": price + p * point,
        "tp": price - p* point,
        "price": price,
        "comment": "python script open",
        "type_time": mt2.ORDER_TIME_GTC,
        "type_filling": mt2.ORDER_FILLING_IOC,
    }
    # send a trading request
    result_sell=mt2.order_send(request_sell)

    print(result_buy)
    print(result_sell)

#### sleep untill other order is been given #####
    time.sleep(sleep_time) 


    if volatile==False:

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

        
if __name__ == "__main__":
     i=0
     while True:
        task()
       