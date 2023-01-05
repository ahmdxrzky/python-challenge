def hide_cc_number(cc_num):
    """
    Convert value from radians into degrees unit.

    :param cc_num: (string) Credit card number that wants to be hide.
    """
    longs = len(cc_num)
    if longs == 16:
        show_num = cc_num[-4:]
        print("Credit card number after being processed: " + "*" * (longs-4) + show_num)
    else:
        print("It doesn't seems as cc number, since the total digits is not 16.")

if __name__ == '__main__':
    try:
        cc_num = int(input("Input credit card number: "))
        hide_cc_number(str(cc_num))
    except ValueError:
        print("Only accept numeral input.")