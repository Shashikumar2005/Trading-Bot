from bot.client import BinanceClient

client = BinanceClient()

server_time = client.get_server_time()

print(server_time)