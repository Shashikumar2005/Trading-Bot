from bot.client import BinanceClient

client = BinanceClient()

print("========== TEST ==========")

try:
    account = client.client.futures_account()

    print(account)

except Exception as e:
    print(type(e))
    print(e)