import math


def normal_f(length, displacement_speed, slope_gradient):
    """
    正断層及び逆断層の水平歪速度を求める
    :param length: Lenghth of fault
    :param displacement_speed: Displacement speed of fault
    :param slope_gradient: Slope gradeint of fault
    :return: Crustal strain rate
    """

    deg = slope_gradient
    rad = math.radians(deg)
    tan = math.tan(rad)
    strain_rate = length * 0.001 * 0.001 * displacement_speed / tan
    strain_rate = strain_rate / (40 * 40)
    return strain_rate


def slip_f(length, displacement_speed):
    """
    横ずれ断層の水平歪速度を求める
    :param length: Lenghth of fault
    :param displacement_speed: Displacement speed of fault
    :return: Crustal strain rate
    """
    cos = math.cos(math.pi / 4)
    strain_rate = length * 0.001 * 0.001 * displacement_speed * cos * cos
    strain_rate = strain_rate / (40 * 40)
    return strain_rate


