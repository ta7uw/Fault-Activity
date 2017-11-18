import argparse
import pandas as pd



def dms2degree():
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
        lat = df.loc[i][1].split(".")
        lon = df.loc[i][2].split(".")
        print(lat)
        lat = int(lat[0]) + int(lat[1])/60 + int(lat[2])/3600
        lon = int(lon[0]) + int(lon[1])/60 + int(lon[2])/3600

        df.loc[i][1] = lat
        df.loc[i][2] = lon
    df.to_csv(args.csv)

if __name__ == '__main__':
    dms2degree()