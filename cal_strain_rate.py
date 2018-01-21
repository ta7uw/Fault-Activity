import math


def normal_f(length, displacement_speed, slope_gradient):
    """
    Calculatate horizontal strain rate of normal fault and reverse fault
    :param length: Lenghth of fault (km)
    :param displacement_speed: Displacement speed of fault (m/10^3year)
    :param slope_gradient: Slope gradeint of fault (degree)
    :return: Crustal strain rate (/year)
    """

    deg = slope_gradient
    rad = math.radians(deg)
    tan = math.tan(rad)
    strain_rate = length * 0.001 * 0.001 * displacement_speed / tan
    strain_rate = strain_rate / (40 * 40)
    return strain_rate


def slip_f(length, displacement_speed):
    """
    Calcultate horizontal strain rate of strike slip fault
    :param length: Lenghth of fault (km)
    :param displacement_speed: Displacement speed of fault (m/10^3year)
    :return: Crustal strain rate (/year)
    """
    cos = math.cos(math.pi / 4)
    strain_rate = length * 0.001 * 0.001 * displacement_speed * cos * cos
    strain_rate = strain_rate / (40 * 40)
    return strain_rate


