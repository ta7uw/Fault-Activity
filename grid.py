from cal_strain_rate import normal_f, slip_f


class Grid(object):

    def __init__(self, center_point, bbox):
        self.center_poinst = center_point
        self.bbox = bbox
        self.fault = None
        self.length = None
        self.strain_rate = None


    def check_contain_fault(self, fault_westend, fault_eastend):

        if

        elif


        else


    def add_strain_rate(self, f_type, displacement_speed , slope=None):
        if f_type == 2:
            self.strain_rate = slip_f(length=self.length,
                                      displacement_speed=displacement_speed)

        else:
            self.strain_rate = normal_f(length=self.length,
                                        displacement_speed=displacement_speed,
                                        slope_gradient=slope)







