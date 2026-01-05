import requests

def get_stock_price(symbol):
    url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey=demo"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"{symbol}: ${data['price']}"
    return f"Error getting price for {symbol}"

if __name__ == "__main__":
    print("Stock Price Checker")
    while True:
        symbol = input("\nEnter stock symbol (or 'quit'): ").upper()
        if symbol == 'QUIT':
            break
        print('Test')
        print(get_stock_price(symbol))