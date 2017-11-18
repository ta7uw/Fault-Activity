from cal_strain_rate import normal_f, slip_f


class Fault(object):

    def __init__(self, name, length, type, displacement_speed, slope=None, west_end, east_end):
        self.name = name
        self.length = length
        self.displacement_speed = displacement_speed
        self.slope = slope
        self.west_end = west_end  # This type is Tuple
        self.east_end = east_end  # This type is Tuple

        # Check fault type
        if type == "正":
            self.type = 0
        elif type == "逆":
            self.type = 1
        else:
            self.type = 2

        self.strain_rate = None

    def __str__(self):
        return self.name

    def add_strain_rate(self):
        if self.type == 2:
            self.strain_rate = slip_f(length=self.length,
                                      displacement_speed=self.displacement_speed)

        else:
            self.strain_rate = normal_f(length=self.length,
                                        displacement_speed=self.displacement_speed,
                                        slope_gradient=self.slope)








