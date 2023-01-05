def count_discount(full_price, discount):
    """
    Count price of an item after discount being applied.

    :param full_price: (integer) Price of an item before discount.
    :param discount: (integer) Percentage of discount.
    """

    total_discount = (discount / 100) * full_price
    final_price = full_price - total_discount
    print(f'Final price of the item: {final_price}')

if __name__ == '__main__':
    price = int(input("Input price of the item: "))
    disc = int(input("Input percentage of the discount: "))
    count_discount(price, disc)