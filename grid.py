

class Grid(object):

    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        self.center_point = ((xmax - xmin) / 2, (ymax -ymin) / 2)
        self.sum_strain_rate = None

    def add_strain_rate(self, fault_obj):
        if fault_obj.west_end[0]



    def export_value(self):
        return self.center_point, self.sum_strain_rate





