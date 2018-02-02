import pandas as pd
import argparse
import numpy as np
import math


def rotate(deg):
    # Transport degree to radian
    r = np.radians(deg)

    cos = np.cos(r)
    sin = np.sin(r)

    # Rotation matrix
    rm = np.array([[cos, -sin], [sin, cos]])
    return rm


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv")
    args = parser.parse_args()

    # Read CSV file
    df = pd.read_csv(args.csv)

    # Count length of data
    data_size = df.shape[0]

    number = 0

    for i in range(data_size):
        fault_type = df.loc[i][2]

        lat_1 = df.loc[i][6].split(".")
        lon_1 = df.loc[i][7].split(".")
        lat_1 = int(lat_1[0]) + int(lat_1[1]) / 60 + int(lat_1[2]) / 3600
        lon_1 = int(lon_1[0]) + int(lon_1[1]) / 60 + int(lon_1[2]) / 3600

        west_point = np.array([lon_1, lat_1])

        lat_2 = df.loc[i][8].split(".")
        lon_2 = df.loc[i][9].split(".")
        lat_2 = int(lat_2[0]) + int(lat_2[1]) / 60 + int(lat_2[2]) / 3600
        lon_2 = int(lon_2[0]) + int(lon_2[1]) / 60 + int(lon_2[2]) / 3600

        east_point = np.array([lon_2, lat_2])

        center_point = np.array([(lon_1+lon_2)/2, (lat_1 + lat_2) / 2])

        # center_point to (0, 0)
        p1 = np.array(west_point - center_point)
        p2 = np.array(east_point - center_point)

        degs = {"正": 0, "逆": 90, "左横ずれ": 45, "右横ずれ": 135}

        if fault_type in degs.keys():

            number += 1
            deg = degs[fault_type]
            rm = rotate(deg)
            p1 = rm.dot(p1)
            p2 = rm.dot(p2)

            gradient = p1[1] / p1[0]
            length = 0.1

            delta_x1 = math.sqrt(length**2 / (1 + gradient ** 2))
            delta_y1 = delta_x1 * gradient
            delta_x2 = - delta_x1
            delta_y2 = delta_x2 * gradient

            p1 = np.array([delta_x1, delta_y1])
            p2 = np.array([delta_x2, delta_y2])

            west_point = np.array(p1 + center_point)
            east_point = np.array(p2 + center_point)

            wkt = f"LINESTRING({west_point[0]} {west_point[1]}, {east_point[0]} {east_point[1]})"
            text = str(number) + ";" + wkt + ";\n"
            print(text)
            file = open("text/vec5.txt", "a+")
            file.writelines(text)
            file.close()
        else:
            continue


if __name__ == '__main__':
    main()