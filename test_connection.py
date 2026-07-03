from bot.client import client

try:
    balance = client.futures_account_balance()
    print("Connected Successfully!")
    print(balance)

except Exception as e:
    print("Error:", e)