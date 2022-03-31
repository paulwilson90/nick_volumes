import json
import requests
from lxml import html
from termcolor import colored
# BTC MARKETS #
print(colored('BTC MARKETS', color='red'))
BTC_ID_1 = 'BTC-AUD'
BTC_ID_2 = 'ETH-AUD'
BTC_ID_3 = 'XRP-AUD'
BTC_ID_4 = 'USDT-AUD'
BTC_SOCKET = f'https://api.btcmarkets.net/v3/markets/tickers?marketId={BTC_ID_1}&marketId={BTC_ID_2}&marketId={BTC_ID_3}&marketId={BTC_ID_4}'
btc_message = (requests.get(BTC_SOCKET)).content
json_btc = json.loads(btc_message)
for ticker in json_btc:
    if ticker['marketId'] == BTC_ID_1:
        print('BTC', ticker['volumeQte24h'][:-9], colored('--- BTC Last Price: $' + ticker['lastPrice'], color='blue'))
    if ticker['marketId'] == BTC_ID_2:
        print('ETH', ticker['volumeQte24h'][:-9], colored('--- ETH Last Price: $' + ticker['lastPrice'], color='blue'))
    if ticker['marketId'] == BTC_ID_3:
        print('XRP', ticker['volumeQte24h'][:-9])
    if ticker['marketId'] == BTC_ID_4:
        print('USDT', ticker['volumeQte24h'][:-9])

print('')
# INDEPENDENT RESERVE #
print(colored('INDEPENDENT RESERVE', color='red'))
indres_page = requests.get('https://www.independentreserve.com/au/buy-sell')
indres_tree = html.fromstring(indres_page.content)
indres_prices_btc = indres_tree.xpath('//*[@id="__layout"]/div/div[2]/main/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[6]/span/span[2]/text()')
indres_prices_eth = indres_tree.xpath('//*[@id="__layout"]/div/div[2]/main/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[6]/span/span[2]/text()')
indres_prices_xrp = indres_tree.xpath('//*[@id="__layout"]/div/div[2]/main/div/div/div/div[2]/div/div/table/tbody/tr[3]/td[6]/span/span[2]/text()')
indres_prices_usdt = indres_tree.xpath('//*[@id="__layout"]/div/div[2]/main/div/div/div/div[2]/div/div/table/tbody/tr[4]/td[6]/span/span[2]/text()')

print('BTC', indres_prices_btc[0].replace(',', ''))
print('ETH', indres_prices_eth[0].replace(',', ''))
print('XRP', indres_prices_xrp[0].replace(',', ''))
print('USDT', indres_prices_usdt[0].replace(',', ''))

print('')
# SWYFTX #
print(colored('SWYFTX', color='red'))
url = "https://apic.swyftx.io/markets/aud/"
data = requests.get(url).json()
# uncomment to print all data:
# print(json.dumps(data, indent=4))
for d in data:
    if d["name"] == "Bitcoin":
        print('BTC', d["volume24H"])
    if d["name"] == "Ethereum":
        print('ETH', d["volume24H"])
    if d["name"] == "XRP":
        print('XRP', d["volume24H"])
        break
# this for loop won't run in one above
for d in data:
    if d['name'] == 'USD Tether':
        print('USDT', d['volume24H'])

