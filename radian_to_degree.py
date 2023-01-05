from math import pi

def convert_rad_to_deg(rad):
    """
    Convert value from radians into degrees unit.

    :param rad: (integer) Value in radians unit.
    """
    
    factor = 360 / (2*pi)
    deg = round(factor * rad, 2)
    print(f'Value in degrees: {deg}')

if __name__ == '__main__':
    try:
        rad = int(input("Input value in radians: "))
        convert_rad_to_deg(rad)
    except ValueError:
        print("Only accept numeral input.")