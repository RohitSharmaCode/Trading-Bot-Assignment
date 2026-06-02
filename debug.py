from bot.client import BinanceClient

client = BinanceClient().get_client()

try:
    account = client.futures_account()
    print(account)

except Exception as e:
    print(e)