from cal_strain_rate import normal_f, slip_f
from sympy.geometry import Point, Polygon, Segment


class Grid(object):

    def __init__(self, center_point, bbox):
        self.center_poinst = center_point
        self.bbox = bbox  # [xmin, ymin, xmax, ymax]
        self.poly = Polygon([(self.bbox[0], self.bbox[1]),
                             (self.bbox[0], self.bbox[3]),
                             (self.bbox[2], self.bbox[1],
                              self.bbox[2],self.bbox[3])])
        self.include_fault = []
        self.f_length = None
        self.strain_rate = None

    def check_contain_fault(self, fault):
        fault_westend = fault.west_end
        fault_eastend = fault.eastend
        fault_length = fault.length

        westend = Point(fault_westend)
        eastend = Point(fault_eastend)
        line = Segment(westend, eastend)

        # Check whether the fault is completely included in this grid
        if self.poly.encloses_point(westend) and self.poly.encloses_point(eastend):
            self.include_fault.append(fault)
            self.f_length.append(fault_length)
            return True

        # Check whether the fault crosses one line of this grid
        elif (self.poly.encloses_point(westend)==True and self.poly.encloses_point(eastend)==False) or \
                (self.poly.encloses_point(westend)==False and self.poly.encloses_point(eastend)==True):
            self.include_fault.append(fault)

            # westend is included
            if self.poly.encloses_point(westend):
                grid_intersection = self.poly.intersection(line)
                print(grid_intersection)
                return True

            else:
                grid_intersection = self.poly.intersection(line)
                print(grid_intersection)
                return True

        # Check whether the fault crosses two lines of this grid
        elif len(self.poly.intersection(line)) > 1:
            print(self.poly.intersection(line))
            self.include_fault.append(fault)
            return True

        # Fault is not included
        else:
            return False

    def add_strain_rate(self):

        for fault, f_length in zip(self.include_fault, self.f_length):
            displacement_speed = fault.displacement_speed
            slope = fault.slope
            f_type = fault.f_type
            if f_type == 2:
                self.strain_rate += slip_f(length=f_length,
                                           displacement_speed=displacement_speed)

            else:
                self.strain_rate += normal_f(length=f_length,
                                             displacement_speed=displacement_speed,
                                             slope_gradient=slope)
            return self.strain_rate







