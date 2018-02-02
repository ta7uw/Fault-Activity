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
    df.assign(lat=0)
    df.assign(lon=0)

    for i in range(0, data_size):
        lat_1 = df.loc[i][3].split("°")
        lon_1 = df.loc[i][4].split("°")

        lat_2 = lat_1[1].split(".")
        lon_2 = lon_1[1].split(".")

        lat_3 = lat_2[1].split("′")
        lon_3 = lon_2[1].split("′")

        lat = int(lat_1[0]) + int(lat_2[0])/60 + int(lat_3[0])/3600
        lon = int(lon_1[0]) + int(lon_2[0])/60 + int(lon_3[0])/3600

        df["lat"] = lat
        df["lon"] = lon
    f_name = "csv/dms2" + args.csv.split("/")[1]
    df.to_csv(f_name)

if __name__ == '__main__':
    dms2degree_epicenter()