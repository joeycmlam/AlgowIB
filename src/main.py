# ib_api_demo.py

from ib.ext.Contract import Contract
from ib.ext.Order import Order
from ib.opt import Connection, message

# ib_api_demo.py

def error_handler(msg):
    """Handles the capturing of error messages"""
    print ("Server Error: %s" % msg)

def reply_handler(msg):
    """Handles of server replies"""
    print ("Server Response: %s, %s" % (msg.typeName, msg))

def historicalTicksLast(reqId: int, ticks ,done: bool):
    for tick in ticks:
        print("HistoricalTickLast. ReqId:", reqId, tick)


if __name__ == '__main__':
    tws_conn = Connection.create(port=7497
                                 , clientId=100)
    tws_conn.connect()

    # Assign the error handling function defined above
    # to the TWS connection
    tws_conn.register(error_handler, 'Error')

    tickers = ['PPF', 'SDIV']

    historicalTicksLast(1, ticks=tickers, done=True)

    # Assign all of the server reply messages to the
    # reply_handler function defined above
    tws_conn.registerAll(reply_handler)

    tws_conn.disconnect()