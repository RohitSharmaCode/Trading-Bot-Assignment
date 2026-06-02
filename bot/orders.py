from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.client import BinanceClient
from bot.logging_config import logger


class OrderManager:
    def __init__(self):
        self.client = BinanceClient().get_client()

    def place_market_order(self, symbol, side, quantity):
        try:
            logger.info(
                f"MARKET ORDER REQUEST | Symbol={symbol} | Side={side} | Quantity={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"MARKET ORDER RESPONSE | {response}")

            return {
                "success": True,
                "data": response
            }

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            return {
                "success": False,
                "error": f"Binance API Error: {e}"
            }

        except BinanceRequestException as e:
            logger.error(f"Network Error: {e}")
            return {
                "success": False,
                "error": f"Network Error: {e}"
            }

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info(
                f"LIMIT ORDER REQUEST | Symbol={symbol} | Side={side} | Quantity={quantity} | Price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(f"LIMIT ORDER RESPONSE | {response}")

            return {
                "success": True,
                "data": response
            }

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            return {
                "success": False,
                "error": f"Binance API Error: {e}"
            }

        except BinanceRequestException as e:
            logger.error(f"Network Error: {e}")
            return {
                "success": False,
                "error": f"Network Error: {e}"
            }

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            return {
                "success": False,
                "error": str(e)
            }