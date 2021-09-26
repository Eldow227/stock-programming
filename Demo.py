
# %% 
### LOGOWANIE DO APLIKACJI ###
import MetaTrader5 as mt5
### LOGOWANIE ###
number = 239980
passw = 'dhysb2cu'
authorized =  mt5.initialize("C://Program Files//MetaTrader 5//terminal64.exe",
                      login = number, password = passw,
                      server = 'Pepperstone-Demo', timeout = 10000 )

if not authorized:
    
    print(f'Failed to connect to trade account {number} with password {passw}')

else:
    print('|','-'*29)
    print('|','    ***ACCOUNT INFO***')
    print('|','-'*29)
    
    
    account_info = mt5.account_info()._asdict()
    for key, value in account_info.items():
        
        print(f'| {key} --> {value}')
    print('|','-'*29)
        
# %%

### TWORZENIE BUY_LIST I SELL_LIST ###

BUY_LIST = []
SELL_LIST = []
print('Working...')

def get_symbol(sym_name):
    symbols = mt5.symbols_get()
    for symbol in symbols:
        if symbol.name == sym_name:
            return symbol.name


def show_symbols():
    symbols = mt5.symbols_get()
    symbol_list = []
    btc = []
    for symbol in symbols:
        symbol_list.append(symbol.name)
        if symbol.name == 'Bitcoin':
            btc.append(symbol)
            
    return symbol_list

#print(show_symbols())
       
    
def check_change(sym_name):
    
    symbols = mt5.symbols_get()
    for symbol in symbols:
        if symbol.name == sym_name:
          if symbol.session_close > symbol.session_open:                          
              result = 1
          else:
              result = 0
              
    return result

symbol_list = show_symbols()
for sym in symbol_list:
    if check_change(sym) == 1:
        BUY_LIST.append(sym)
    else:
        SELL_LIST.append(sym)

print('Done!')
# %%
print(SELL_LIST)

# %% ### WYKONYWANIE OPERACJI TRADINGOWEJ  ###
import random
import MetaTrader5 as mt5

###(BUY) Jezeli instrument w BUY_LIST kup i zamknij kiedy osiagnie
###cene wieksza o polowe  close - open

symbol = get_symbol('Bitcoin')
symbol_info = mt5.symbol_info(symbol)
# %%
print(symbol_info)
# %%
if symbol_info == None:
    print(f'{symbol} not found, we could not call order.')
    print('Terminating...')
    time.sleep(10)
    mt5.shutdown()
    quit()
    
lot = 0.1
price = mt5.symbol_info_tick(symbol).ask,
deviation = 50
symbols = mt5.symbols_get()
for i in symbols:
        if i.name == symbol:
            close_p = i.session_close
            open_p = i.session_open

diff = close_p - open_p
price = mt5.symbol_info_tick(symbol).ask
TP = price + 100
SL = price - 50


### #DEFINIOWANIE OPERACJI ###
import time
import MetaTrader5 as mt5

request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "sl" : SL,
    "tp": TP,
    "deviation": deviation,
    "magic": 3,
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling":mt5.ORDER_FILLING_IOC,
}

### WYSYLAM ZĄDANIE OPERACJI ###

result = mt5.order_send(request)

### SPRAWDZAM WYNIK WYKONANIA ###
print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol,lot,price,deviation));
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("2. order_send failed, retcode={}".format(result.retcode))
    # request the result as a dictionary and display it element by element
    result_dict=result._asdict()
    for field in result_dict.keys():
        print("   {}={}".format(field,result_dict[field]))
        # if this is a trading request structure, display it element by element as well
        if field=="request":
            traderequest_dict=result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
    print("shutdown() and quit")
    
else:
    print("2. order_send done, ", result)
    print("   opened position with POSITION_TICKET={}".format(result.order))
    


# %%

###(SELL) Jezeli instrument w SELL_LIST sprzedaj i zamknij kiedy osiagnie
###cene mniejsza o polowe różnicy open - close

#while account_info['balance'] > 75000:
    

