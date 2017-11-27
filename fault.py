

class Fault(object):

    def __init__(self, name, length, f_type, displacement_speed, slope=None, west_end=None, east_end=None):
        self.name = name
        self.length = int(length)
        self.f_type = f_type
        self.displacement_speed = displacement_speed
        self.slope = slope
        west_end_lat = west_end[1].split(".")
        west_end_lon = west_end[0].split(".")
        west_end_lat = int(west_end_lat[0]) + int(west_end_lat[1]) / 60 + int(west_end_lat[2]) / 3600
        west_end_lon = int(west_end_lon[0]) + int(west_end_lon[1]) / 60 + int(west_end_lon[2]) / 3600

        self.west_end = west_end_lon, west_end_lat  # This type is Tuple

        east_end_lat = east_end[1].split(".")
        east_end_lon = east_end[0].split(".")
        east_end_lat = int(east_end_lat[0]) + int(east_end_lat[1]) / 60 + int(east_end_lat[2]) / 3600
        east_end_lon = int(east_end_lon[0]) + int(east_end_lon[1]) / 60 + int(east_end_lon[2]) / 3600

        self.east_end = east_end_lon, east_end_lat  # This type is Tuple

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









