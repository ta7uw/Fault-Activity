from cal_strain_rate import normal_f, slip_f
from sympy.geometry import Point, Polygon, Segment
import math


km_per_lon = 93.45286
km_per_lat = 111.263


class Grid(object):
    """
    This is Grid for calculating　horizontal strain rate
    """

    def __init__(self, center_point, bbox):
        # center point of this grid
        self.center_poinst = center_point
        # bounding box is expressed as [xmin, ymin, xmax, ymax]
        self.bbox = bbox
        # Create polygon by using this bounding box
        self.poly = Polygon((self.bbox[0], self.bbox[1]),  # (xmin, ymin)
                            (self.bbox[2], self.bbox[1]),  # (xmax, ymin)
                            (self.bbox[2], self.bbox[3]),  # (xmax, ymax)
                            (self.bbox[0], self.bbox[3]))  # (xmin, ymax)

        # Faults are included in this grid
        self.include_fault = []
        # Length of faults included in this grid
        self.f_length = []
        # horizontal strain rate in this grid
        self.strain_rate = 0

    def check_contain_fault(self, fault):
        """
        This method is for checking whether faults is included in the grid
        :param fault: fault is a "Fault" class object
        :return: True or False
                    True is that faults is included in the grid
                    False is that faults is not included in the grid
        """
        # Extact elements from the fault object
        fault_westend = fault.west_end
        fault_eastend = fault.east_end
        fault_length = fault.length

        # Create geometry Point and Segment class object
        westend = Point(fault_westend)
        eastend = Point(fault_eastend)
        line = Segment(westend, eastend)

        # Check whether the fault is completely included in this grid
        if self.poly.encloses_point(westend) and self.poly.encloses_point(eastend):
            self.include_fault.append(fault)
            self.f_length.append(fault_length)
            return True

        # Check whether the fault crosses one line of this grid
        elif len(self.poly.intersection(line)) == 1:
            self.include_fault.append(fault)

            # westend is included
            if self.poly.encloses_point(westend):
                grid_intersection = self.poly.intersection(line)
                margin_x = eastend[0] - grid_intersection[0].x
                margin_y = eastend[1] - grid_intersection[0].y
                margin = margin_x, margin_y
                margin_lon = margin[0]
                margin_lat = margin[1]
                margin_x = margin_lon * km_per_lon
                margin_y = margin_lat * km_per_lat
                length = math.sqrt(margin_x**2 + margin_y**2)
                self.f_length.append(length)
                return True
            # eastend is included
            else:
                grid_intersection = self.poly.intersection(line)
                margin_x = eastend[0] - grid_intersection[0].x
                margin_y = eastend[1] - grid_intersection[0].y
                margin = margin_x, margin_y
                margin_lon = margin[0]
                margin_lat = margin[1]
                margin_x = margin_lon * km_per_lon
                margin_y = margin_lat * km_per_lat
                length = math.sqrt(margin_x ** 2 + margin_y ** 2)
                self.f_length.append(length)

                return True

        # Check whether the fault crosses two lines of this grid
        elif len(self.poly.intersection(line)) == 2:
            self.include_fault.append(fault)
            grid_intersection = [intersection for intersection in self.poly.intersection(line)]
            intersection_1 = [grid_intersection[0].x, grid_intersection[0].y]
            intersection_2 = [grid_intersection[1].x, grid_intersection[1].y]
            margin = [a - b for a, b in zip(intersection_1, intersection_2)]
            margin_lon = margin[0]
            margin_lat = margin[1]
            margin_x = margin_lon * km_per_lon
            margin_y = margin_lat * km_per_lat
            length = math.sqrt(margin_x ** 2 + margin_y ** 2)
            self.f_length.append(length)
            return True

        # Fault is not included
        else:
            return False

    def add_strain_rate(self):
        """
        Calcultate horizontal strain rate of each fault is included in this grid, and
        Add strain rate to this grid
        :return:
        """

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







