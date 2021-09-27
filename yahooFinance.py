import yfinance as yf


def msft_stock():
    msft = yf.Ticker("MSFT")
    msftInfo = msft.info
    keys = ['recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
    values = list(map(msftInfo.get, keys))
    print(values)


if __name__ == '__main__':
    msft_stock()
