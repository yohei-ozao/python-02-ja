def apply_discount(
    products,
    minimum_price,
    discount_rate,
):
    calculate_price = lambda price: price * (1 - discount_rate * 0.01)

    return [
        (
            elem["name"],
            calculate_price(elem["price"]),
        )
        for elem in products
        if elem["price"] >= minimum_price
    ]