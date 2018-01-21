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

    faults = []

    for i in range(data_size):
        f_name = df.loc[i][0]
        f_length = df.loc[i][1]
        f_type = df.loc[i][2]
        f_slope = df.loc[i][3]
        f_dspped = df.loc[i][5]
        f_westend = df.loc[i][7], df.loc[i][6]
        f_eastend = df.loc[i][9], df.loc[i][8]

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
        faults.append(fault)

    count = 0
    grid_chugoku_df = pd.read_csv("csv/grid-CHUGOKU.csv")
    # Count length of data
    chugoku_data_size = grid_chugoku_df.shape[0]
    chugoku_strain_rate_list = []
    for i in range(chugoku_data_size):
        center_lon = grid_chugoku_df.loc[i][1]
        center_lat = grid_chugoku_df.loc[i][2]
        xmin = grid_chugoku_df.loc[i][3]
        ymin = grid_chugoku_df.loc[i][4]
        xmax = grid_chugoku_df.loc[i][5]
        ymax = grid_chugoku_df.loc[i][6]

        count += 1
        print(count)
        grid = Grid(
            center_point=[center_lon, center_lat],
            bbox=[xmin, ymin, xmax, ymax]
        )

        for fault in faults:
            if grid.check_contain_fault(fault):
                print("fault is included---" + fault.name)
        grid.add_strain_rate()
        print(grid.strain_rate)
        chugoku_strain_rate_list.append(grid.strain_rate)

    chugoku_s = pd.Series(data=chugoku_strain_rate_list)
    grid_chugoku_df["strain-rate"] = chugoku_s
    grid_chugoku_df.to_csv("csv/result-chugoku-0121.csv", encoding="utf-8")

    print("--------------------------------------------------------")

    grid_kyusyu_df = pd.read_csv("csv/grid-KYUSYU.csv")
    # Count length of data
    kyusyu_data_size = grid_kyusyu_df.shape[0]
    kyusyu_strain_rate_list = []
    for i in range(kyusyu_data_size):
        center_lon = grid_kyusyu_df.loc[i][1]
        center_lat = grid_kyusyu_df.loc[i][2]
        xmin = grid_kyusyu_df.loc[i][3]
        ymin = grid_kyusyu_df.loc[i][4]
        xmax = grid_kyusyu_df.loc[i][5]
        ymax = grid_kyusyu_df.loc[i][6]

        count += 1
        print(count)
        grid = Grid(
            center_point=[center_lon, center_lat],
            bbox=[xmin, ymin, xmax, ymax]
        )

        for fault in faults:
            if grid.check_contain_fault(fault):
                print("fault is included---" + fault.name)
        grid.add_strain_rate()
        print(grid.strain_rate)
        kyusyu_strain_rate_list.append(grid.strain_rate)
    kyusyu_s = pd.Series(data=kyusyu_strain_rate_list)
    grid_kyusyu_df["strain-rate"] = kyusyu_s

    grid_kyusyu_df.to_csv("csv/result-kyusyu-0121.csv", encoding="utf-8")


if __name__ == '__main__':
    export_strain_rate()
