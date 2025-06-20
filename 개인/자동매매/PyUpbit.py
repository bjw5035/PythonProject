import pyupbit
import jwt
import uuid

df = pyupbit.get_ohlcv("KRW-BTC", count=7)
print(df)