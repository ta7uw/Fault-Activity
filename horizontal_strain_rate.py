import pandas as pd
from fault import Fault
import argparse


def export_strain_rate():

    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="Path to csv file")
    args = parser.parse_args()

    # Read CSV file
    df = pd.read_csv(args.csvfile_path)

    # Count length of data
    data_size = df.shape[0]
    for i in data_size:
        f_name = df.loc[i][0]
        f_length = df.loc[i][1]
        f_type = df.loc[i][2]
        f_dspped = df.loc[i][3]
        f_slope = df.loc[i][4]
        f_westend = (df.loc[i][5], df.loc[i][6])
        f_eastend = (df.loc[i][6], df.loc[i][7])

        # Create 'Fault' object
        fault = Fault(
            name=f_name,
            length=f_length,
            type=f_type,
            displacement_speed=f_dspped,
            slope=f_slope,
            west_end=f_westend,
            east_end=f_eastend,
        )
        # Calcurate horizontal strain rate from fault object data
        fault.add_strain_rate()

        # Display Result of calcuration
        print("Strain rate: {}".format(fault.strain_rate))


if __name__ == '__main__':
    export_strain_rate()