"""
비트코인 자동매매 프로그램 (풀옵션 버전)
- 전략: 이동평균 골든크로스 + RSI + 볼린저밴드
- 기능: 스탑로스, 목표가, 텔레그램 알림, 백테스트, FastAPI 대시보드
"""

import os
import time
import datetime
import pyupbit
import requests
import pandas as pd
from fastapi import FastAPI
from threading import Thread
from dotenv import load_dotenv

# .env 파일 로드 (API 키 등)
load_dotenv()

access_key = os.getenv("UPBIT_ACCESS_KEY")
secret_key = os.getenv("UPBIT_SECRET_KEY")
telegram_token = os.getenv("TELEGRAM_TOKEN")
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

upbit = pyupbit.Upbit(access_key, secret_key)

ticker = "KRW-BTC"

# 거래 파라미터
STOP_LOSS_PERCENT = -3.0  # -3% 손절매
TARGET_PROFIT_PERCENT = 5.0  # 5% 목표가

def get_ma(df, window):
    return df['close'].rolling(window=window).mean()

def get_rsi(df, period=14):
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def get_bollinger_bands(df, window=20, num_std=2):
    rolling_mean = df['close'].rolling(window=window).mean()
    rolling_std = df['close'].rolling(window=window).std()
    upper_band = rolling_mean + (rolling_std * num_std)
    lower_band = rolling_mean - (rolling_std * num_std)
    return upper_band, lower_band

def send_telegram(message):
    if telegram_token and telegram_chat_id:
        url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        requests.post(url, data={"chat_id": telegram_chat_id, "text": message})

def log_trade(message):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("trade_log.txt", "a") as f:
        f.write(f"{now} {message}\n")

def execute_trade():
    bought_price = None
    while True:
        try:
            now = datetime.datetime.now()
            if now.minute == 0 and now.second < 5:
                df = pyupbit.get_ohlcv(ticker, interval="day", count=30)
                ma5 = get_ma(df, 5).iloc[-1]
                ma20 = get_ma(df, 20).iloc[-1]
                rsi = get_rsi(df).iloc[-1]
                upper_band, lower_band = get_bollinger_bands(df)
                current_price = pyupbit.get_current_price(ticker)
                balance = upbit.get_balance("KRW")
                btc_balance = upbit.get_balance(ticker)

                send_telegram(f"📊 현재가: {current_price}, MA5: {ma5:.0f}, MA20: {ma20:.0f}, RSI: {rsi:.1f}")

                # 매수 조건
                if ma5 > ma20 and rsi < 70 and bought_price is None and balance > 5000:
                    upbit.buy_market_order(ticker, balance * 0.9995)
                    bought_price = current_price
                    send_telegram(f"✅ 매수: {current_price}")
                    log_trade(f"매수: {current_price}")

                # 매도 조건
                elif bought_price is not None:
                    profit_percent = ((current_price - bought_price) / bought_price) * 100
                    if profit_percent >= TARGET_PROFIT_PERCENT:
                        upbit.sell_market_order(ticker, btc_balance)
                        send_telegram(f"🎯 목표가 매도: {current_price} (+{profit_percent:.2f}%)")
                        log_trade(f"목표가 매도: {current_price} (+{profit_percent:.2f}%)")
                        bought_price = None
                    elif profit_percent <= STOP_LOSS_PERCENT:
                        upbit.sell_market_order(ticker, btc_balance)
                        send_telegram(f"⛔ 손절매도: {current_price} ({profit_percent:.2f}%)")
                        log_trade(f"손절매도: {current_price} ({profit_percent:.2f}%)")
                        bought_price = None

            time.sleep(1)
        except Exception as e:
            print(f"❌ 에러 발생: {e}")
            log_trade(f"에러: {e}")
            time.sleep(10)

# FastAPI 웹 대시보드
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "비트코인 자동매매 시스템"}

@app.get("/status")
def read_status():
    try:
        price = pyupbit.get_current_price(ticker)
        return {"ticker": ticker, "current_price": price}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # 백테스트 함수 (간단)
    def backtest():
        df = pyupbit.get_ohlcv(ticker, interval="day", count=100)
        df['ma5'] = get_ma(df, 5)
        df['ma20'] = get_ma(df, 20)
        df['position'] = (df['ma5'] > df['ma20']).astype(int)
        df['daily_return'] = df['close'].pct_change()
        df['strategy_return'] = df['daily_return'] * df['position'].shift(1)
        cumulative = (1 + df['strategy_return']).cumprod()[-1]
        print(f"백테스트 결과(100일): 누적 수익률 {((cumulative - 1) * 100):.2f}%")

    # 쓰레드로 자동매매 실행
    trade_thread = Thread(target=execute_trade)
    trade_thread.start()

    # FastAPI 서버 실행
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
