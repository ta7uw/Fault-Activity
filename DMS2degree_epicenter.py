import argparse
import pandas as pd


def dms2degree_epicenter():
    """
    Transform DMS to degree type
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="Path to csv file")
    args = parser.parse_args()

    # Read CSV file
    df = pd.read_csv(args.csv)
    data_size = df.shape[0]
    print(data_size)

    for i in range(0, data_size):
        lat_1 = df.loc[i][4].split("°")[0]
        lon_1 = df.loc[i][3].split("°")[0]

        lat_2 = df.loc[i][4].split(".")[0]
        lon_2 = df.loc[i][3].split(".")[0]

        lat_3 = df.loc[i][4].split("'")[0]
        lon_3 = df.loc[i][3].split("'")[0]

        lat = int(lat_1[0]) + int(lat_2[1])/60 + int(lat_3[2])/3600
        lon = int(lon_1[0]) + int(lon_2[1])/60 + int(lon_3[2])/3600

        df.loc[i][3] = lat
        df.loc[i][4] = lon
    df.to_csv(args.csv)

if __name__ == '__main__':
    dms2degree_epicenter()