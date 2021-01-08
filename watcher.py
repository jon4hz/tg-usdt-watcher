#!/usr/bin/python3.8
#
# Author: jon4hz
# Date: 08.01.2021
# Desc: Script to overwatch the total supply of USDT with the etherscan api
#
###################################################################################

import configparser, threading, time
from telegram import Bot
from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

config = configparser.ConfigParser()
config.read('data/config.ini')


def getSupply(cmc) -> int:
    
    data = cmc.cryptocurrency_quotes_latest(symbol='USDT')
    print(data)
    exit()
    try:
        if int(data.get('status')) == 0:
            print(data.get('result'))
        
        else:
            return int(data.get('result'))
    
    except Exception as e:
        print(f'Error: {e}\nData: {data}')


def watcher() -> None:

    cmc = CoinMarketCapAPI(config['coinmarketcap'].get('TOKEN'))
    print(type(cmc))
    previous_supply = 0
    
    while True:
        supply = getSupply(cmc)
        
        if supply != previous_supply:
            
            if supply > previous_supply:
                message = f'{supply-previous_supply} USD₮ printed! \nTotal supply: {supply} USD₮'
                print(message)
                
                bot.send_message(
                    chat_id=config["telegram"].get("ADMIN_ID"),
                    text=message
                )

            elif supply < previous_supply:
                message = f'{previous_supply-supply} USD₮ burned! \nTotal supply: {supply} USD₮'
                print(message)
            
                bot.send_message(
                    chat_id=config["telegram"].get("ADMIN_ID"),
                    text=message
                )

            previous_supply = supply

        else:
            pass

        time.sleep(60)


def botHandler():
    pass


if __name__ == "__main__":

    bot = Bot(config["telegram"].get("TOKEN"))
    threading.Thread(target=watcher).start()
    threading.Thread(target=botHandler).start()