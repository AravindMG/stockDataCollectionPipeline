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


def tsla_stock():
    tsla = yf.Ticker("TSLA")
    tslaInfo = tsla.info
    keys = ['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
    values = list(map(tslaInfo.get, keys))
    print(values)


def voo_stock():
    voo = yf.Ticker("VOO")
    vooInfo = voo.info
    keys = ['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
    values = list(map(vooInfo.get, keys))
    print(values)


def nio_stock():
    nio = yf.Ticker("NIO")
    nioInfo = nio.info
    keys = ['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
    values = list(map(nioInfo.get, keys))
    print(values)


if __name__ == '__main__':
    print("---- Microsoft Stock Data ----")
    msft_stock()
    print("\n")
    print("---- Apple Stock Data ----")
    aapl_stock()
    print("\n")
    print("---- Tesla Stock Data ----")
    tsla_stock()
    print("\n")
    print("---- VOO Stock Data ----")
    voo_stock()
    print("\n")
    print("---- NIO Stock Data ----")
    nio_stock()
    print("\n")
