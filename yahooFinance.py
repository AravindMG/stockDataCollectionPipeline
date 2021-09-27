import yfinance as yf


def msft_stock():
    msft = yf.Ticker("MSFT")
    msftInfo = msft.info
    keys = ['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
    values = list(map(msftInfo.get, keys))
    print(values)


def aapl_stock():
    aapl = yf.Ticker("AAPL")
    aaplInfo = aapl.info
    keys = ['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
    values = list(map(aaplInfo.get, keys))
    print(values)


if __name__ == '__main__':
    print("---- Microsoft Stock Data ----")
    msft_stock()
    print("\n")
    print("---- Apple Stock Data ----")
    aapl_stock()
    print("\n")
