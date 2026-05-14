import yfinance as yf

def get_live_price():
    # 1. Ask the user for input
    ticker_input = input("Enter the stock ticker symbol (e.g., AAPL, BTC-USD): ").upper().strip()

    try:
        # 2. Initialize the ticker
        stock = yf.Ticker(ticker_input)
        
        # 3. Fetch data (fast_info is the quickest way to get the current price)
        price = stock.fast_info['last_price']
        currency = stock.fast_info['currency']
        
        # 4. Display the result
        print("-" * 30)
        print(f"Ticker:   {ticker_input}")
        print(f"Price:    {price:.2f} {currency}")
        print("-" * 30)

    except Exception:
        print(f"Error: Could not find data for '{ticker_input}'. Please check the symbol.")

if __name__ == "__main__":
    get_live_price()