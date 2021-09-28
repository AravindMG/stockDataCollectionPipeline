import yfinance as yf
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, DoubleType

appName = "Stock dataframe"
master = "local"

# Create Spark session
spark = SparkSession.builder \
    .appName(appName) \
    .master(master) \
    .getOrCreate()

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


def create_df():
    msft_data = msft_stock()
    # tsla_data = tsla_stock()
    # aapl_data = aapl_stock()
    # nio_data = nio_stock()
    columns = ['symbol', 'recommendationKey', 'targetLowPrice', 'targetMedianPrice', 'currentPrice', 'targetMeanPrice']
    stock_dataframe = spark.createDataFrame([(msft_data,)], columns)
    stock_dataframe.show()


if __name__ == '__main__':
    create_df()
