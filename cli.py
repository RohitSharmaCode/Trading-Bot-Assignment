import argparse

from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Required for LIMIT orders"
    )

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)

        if args.type.upper() == "LIMIT":
            validate_price(args.price)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {args.symbol.upper()}")
        print(f"Side     : {args.side.upper()}")
        print(f"Type     : {args.type.upper()}")
        print(f"Quantity : {args.quantity}")

        if args.type.upper() == "LIMIT":
            print(f"Price    : {args.price}")

        order_manager = OrderManager()

        if args.type.upper() == "MARKET":
            result = order_manager.place_market_order(
                symbol=args.symbol.upper(),
                side=args.side.upper(),
                quantity=args.quantity
            )

        else:
            result = order_manager.place_limit_order(
                symbol=args.symbol.upper(),
                side=args.side.upper(),
                quantity=args.quantity,
                price=args.price
            )

        print("\n========== ORDER RESPONSE ==========")

        if result["success"]:
            data = result["data"]

            print(f"Order ID      : {data.get('orderId')}")
            print(f"Status        : {data.get('status')}")
            print(f"Executed Qty  : {data.get('executedQty', 'N/A')}")
            print(f"Avg Price     : {data.get('avgPrice', 'N/A')}")

            print("\n✅ Order placed successfully.")

        else:
            print(f"\n❌ Order placement failed.")
            print(result["error"])

    except ValueError as e:
        print(f"\n❌ Validation Error: {e}")

    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")


if __name__ == "__main__":
    main()
