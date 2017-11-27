import pandas as pd
import argparse
from fault import Fault
from grid import Grid


def export_strain_rate():

    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="Path to csv file")
    args = parser.parse_args()

    # Read CSV file
    df = pd.read_csv(args.csv)

    # Count length of data
    data_size = df.shape[0]

    for i in range(data_size):
        f_name = df.loc[i][0]
        f_length = df.loc[i][1]
        f_type = df.loc[i][2]
        f_slope = df.loc[i][3]
        f_dspped = df.loc[i][4]
        f_westend = (df.loc[i][5], df.loc[i][6])
        f_eastend = (df.loc[i][7], df.loc[i][8])

        # Create 'Fault' object
        fault = Fault(
            name=f_name,
            length=f_length,
            f_type=f_type,
            displacement_speed=f_dspped,
            slope=f_slope,
            west_end=f_westend,
            east_end=f_eastend,
        )

        # Display Result of calcuration
        print("Strain rate: {}".format(fault.strain_rate))
        df["歪速度"] = fault.strain_rate
    df.to_csv("csv/result.csv", encoding="utf-8")


if __name__ == '__main__':
    export_strain_rate()