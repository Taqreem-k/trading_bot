import os
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:

    def __init__(self):
        api_key = os.getenv("BINANCE_TESTNET_API_KEY")
        api_secret = os.getenv("BINANCE_TESTNET_SECRET_KEY")

        if not api_key or not api_secret:
            raise ValueError("API keys not found. Please check your .env file.")

        self.client = Client(api_key, api_secret, testnet=True)

    def place_market_order(self, symbol: str, side: str, quantity: float) -> dict:
        try:
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )
            return response
        except Exception as e:
            raise e

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float) -> dict:
        try:
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=FUTURE_ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,  
            )
            return response
        except Exception as e:
            raise e