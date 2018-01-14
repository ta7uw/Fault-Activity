import pandas as pd
import argparse
import numpy as np


def rotate(deg):
    # Transport degree to radian
    r = np.radians(deg)

    cos = np.cos(r)
    sin = np.sin(r)

    # Rotation matrix
    rm = np.array([[cos, -sin],
                    [sin, cos]])
    return rm


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv")
    args = parser.parse_args()

    # Read CSV file
    df = pd.read_csv(args.csv)

    # Count length of data
    data_size = df.shape[0]

    vec = []

    for i in range(data_size):
        fault_type = df.loc[i][2]

        lat_1 = df.loc[i][6].split(".")
        lon_1 = df.loc[i][7].split(".")
        lat_1 = int(lat_1[0]) + int(lat_1[1]) / 60 + int(lat_1[2]) / 3600
        lon_1 = int(lon_1[0]) + int(lon_1[1]) / 60 + int(lon_1[2]) / 3600

        west_point = np.array([lat_1, lon_1])

        lat_2 = df.loc[i][8].split(".")
        lon_2 = df.loc[i][9].split(".")
        lat_2 = int(lat_2[0]) + int(lat_2[1]) / 60 + int(lat_2[2]) / 3600
        lon_2 = int(lon_2[0]) + int(lon_2[1]) / 60 + int(lon_2[2]) / 3600

        east_point = np.array([lat_2, lon_2])

        center_point = np.array([(lat_1+lat_2)/2, (lon_1 + lon_2) / 2])

        p1 = np.array(west_point - center_point)
        p2 = np.array(east_point - center_point)
        print(fault_type)

        degs = {"正": 0, "逆": 90, "左横ずれ": 45, "右横ずれ": 135}

        if fault_type in degs.keys():
            deg = degs[fault_type]
            rm = rotate(degs)

        else:
            continue





if __name__ == '__main__':
    main()