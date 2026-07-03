import argparse
from bot.validators import (
    validate_side,
    validate_order_type
)
from bot.orders import (
    place_market_order,
    place_limit_order
)


def main():

    parser = argparse.ArgumentParser(
        description="Binance Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float
    )

    parser.add_argument(
        "--price",
        type=float
    )

    args = parser.parse_args()

    try:

        side = validate_side(args.side)
        order_type = validate_order_type(args.type)

        print("\n===== ORDER REQUEST =====")
        print("Symbol :", args.symbol)
        print("Side   :", side)
        print("Type   :", order_type)
        print("Qty    :", args.quantity)

        if order_type == "MARKET":

            response = place_market_order(
                args.symbol,
                side,
                args.quantity
            )

        elif order_type == "LIMIT":

            if args.price is None:
                raise ValueError(
                    "Price is required for LIMIT order"
                )

            print("Price  :", args.price)

            response = place_limit_order(
                args.symbol,
                side,
                args.quantity,
                args.price
            )

        print("\n===== RESPONSE =====")
        print("Order ID :", response["orderId"])
        print("Status   :", response["status"])
        print("Symbol   :", response["symbol"])
        print("Side     :", response["side"])
        print("Executed :", response.get("executedQty", "N/A"))
        print("Price    :", response.get("price", "N/A"))

        print("\nSUCCESS")

    except Exception as e:
        print("\nFAILED")
        print(e)


if __name__ == "__main__":
    main()