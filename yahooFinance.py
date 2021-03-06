import yfinance as yf
import pandas as pd


def msft_stock():
    msft = yf.Ticker("MSFT")
    msftInfo = msft.info
    keys = ['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
    msft_li = list(map(msftInfo.get, keys))
    return msft_li


def aapl_stock():
    aapl = yf.Ticker("AAPL")
    aaplInfo = aapl.info
    keys = ['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
    aapl_li = list(map(aaplInfo.get, keys))
    return aapl_li

def meta_stock():
    meta = yf.Ticker("FB")
    metaInfo = meta.info
    keys = ['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
    meta_li = list(map(metaInfo.get, keys))
    return meta_li


def tsla_stock():
    tsla = yf.Ticker("TSLA")
    tslaInfo = tsla.info
    keys = ['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
    tsla_li = list(map(tslaInfo.get, keys))
    return tsla_li


# def voo_stock():
#     voo = yf.Ticker("VOO")
#     vooInfo = voo.info
#     keys = ['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
#     values = list(map(vooInfo.get, keys))
#     print(values)


def nio_stock():
    nio = yf.Ticker("NIO")
    nioInfo = nio.info
    keys = ['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
    nio_li = list(map(nioInfo.get, keys))
    return nio_li


def creating_pandas_dataframe():
    list_msft = msft_stock()
    list_aapl = aapl_stock()
    list_meta = meta_stock()
    list_tsla = tsla_stock()
    list_nio = nio_stock()
    df = pd.DataFrame([list_msft, list_aapl, list_meta, list_tsla, list_nio], columns=['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice'])
    return df


def adding_timeStamp():
    add_timeStamp = creating_pandas_dataframe()
    add_timeStamp['dateTime'] = pd.to_datetime('now').strftime("%Y-%m-%d")
    print(add_timeStamp)


if __name__ == '__main__':
    adding_timeStamp()
# Running this application with AWS Lambda (https://towardsdatascience.com/python-packages-in-aws-lambda-made-easy-8fbc78520e30)