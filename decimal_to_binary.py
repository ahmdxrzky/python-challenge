def convert_dec_to_bin(dec):
    """
    Convert value below 1024 from decimal to binary format.

    :param dec: (integer) Value in decimal format.
    """

    factor = 512
    buffer = []
    while factor > 1 and dec > 0:
        if dec >= factor:
            buffer.append(1)
            dec -= factor
        else:
            buffer.append(0)
        factor /= 2
    for i in range(10 - len(buffer)):
        buffer.append(int(dec))
    bin = ""
    for val in buffer:
        bin += str(val)
    print(f'Value in binary: {bin}')

if __name__ == '__main__':
    try:
        dec = int(input("Input value in decimal: "))
        if dec < 1024:
            convert_dec_to_bin(dec)
        else:
            print("Fail. Value bigger than 1023.")
    except ValueError:
        print("Only accept numeral input.")