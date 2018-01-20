import pandas as pd
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="Path to csv file")
    args = parser.parse_args()

    # Read CSV file
    df = pd.read_csv(args.csv)

    # Count length of data
    data_size = df.shape[0]

    strain_rate_cor = []

    for i in range(data_size):
        strain_rate = df.loc[i][8] * 4
        strain_rate_cor.append(strain_rate)
    strain_rate_cor_s = pd.Series(data=strain_rate_cor)
    df["strainratecor-ver2"] = strain_rate_cor_s
    name = args.csv.split("/")[1]
    df.to_csv(f"csv/correction-{name}", encoding="utf-8")


if __name__ == '__main__':
    main()