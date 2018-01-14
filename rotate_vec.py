import pandas as pd
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv")
    args = parser.parse_args()

    # Read CSV file
    df = pd.read_csv(args.csv)
    print(df)

    # Count length of data
    data_size = df.shape[0]

    for i in range(data_size):




if __name__ == '__main__':
    main()