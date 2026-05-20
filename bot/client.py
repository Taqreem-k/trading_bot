import os
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv
from .logging_config import logger

load_dotenv()

class BinanceFuturesClient:
   
    def __init__(self):
        api_key = os.getenv("BINANCE_TESTNET_API_KEY")
        api_secret = os.getenv("BINANCE_TESTNET_SECRET_KEY")

        if not api_key or not api_secret:
            logger.error("Failed to initialize client: Missing API keys in .env")
            raise ValueError("API keys not found. Please check your .env file.")

        self.client = Client(api_key, api_secret, testnet=True)
        logger.info("BinanceFuturesClient initialized successfully on Testnet.")

    def place_market_order(self, symbol: str, side: str, quantity: float) -> dict:
        logger.info(f"Attempting MARKET order: {side} {quantity} {symbol}")
        try:
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logger.info(f"MARKET order successful! OrderID: {response.get('orderId')} | Status: {response.get('status')}")
            return response
            
        except (BinanceAPIException, BinanceRequestException) as e:
            logger.error(f"Binance API Error during MARKET order: {e.message}")
            raise e
        except Exception as e:
            logger.error(f"Unexpected error during MARKET order: {str(e)}")
            raise e

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float) -> dict:
        logger.info(f"Attempting LIMIT order: {side} {quantity} {symbol} @ {price}")
        try:
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=FUTURE_ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logger.info(f"LIMIT order successful! OrderID: {response.get('orderId')} | Status: {response.get('status')}")
            return response
            
        except (BinanceAPIException, BinanceRequestException) as e:
            logger.error(f"Binance API Error during LIMIT order: {e.message}")
            raise e
        except Exception as e:
            logger.error(f"Unexpected error during LIMIT order: {str(e)}")
            raise e