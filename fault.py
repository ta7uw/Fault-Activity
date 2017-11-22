from cal_strain_rate import normal_f, slip_f


class Fault(object):

    def __init__(self, name, length, f_type, displacement_speed, slope=None, west_end=None, east_end=None):
        self.name = name
        self.length = int(length)
        self.f_type = f_type
        self.displacement_speed = displacement_speed
        self.slope = slope
        self.west_end = west_end  # This type is Tuple
        self.east_end = east_end  # This type is Tuple

        # Check fault type
        if self.f_type == "正":
            self.f_type = 0
        elif self.f_type == "逆":
            self.f_type = 1
        else:
            self.f_type = 2

        self.strain_rate = None

        if self.displacement_speed == "-":
            if self.f_type == 2:
                self.displacement_speed = 0.205
            else:
                self.displacement_speed = 0.275
        else:
            self.displacement_speed = float(self.displacement_speed)

    def __str__(self):
        return self.name

    def add_strain_rate(self):
        if self.f_type == 2:
            self.strain_rate = slip_f(length=self.length,
                                      displacement_speed=self.displacement_speed)

        else:
            self.strain_rate = normal_f(length=self.length,
                                        displacement_speed=self.displacement_speed,
                                        slope_gradient=self.slope)








