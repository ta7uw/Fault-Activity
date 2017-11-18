import pandas as pd


def import_files():

    file_path = "data-10-21(version-2.00).csv"
    df = pd.read_csv(file_path)
    name_data = df["断層名"]
    length = df["長さ(km)"]
    f_type = df["断層型"]
    displacement_speed = df["平均変位速度[m/千年]"]
    print(displacement_speed.describe())

    for type in f_type:
        if type == "正":
            print("正断層")

        elif type == "逆":
            print("逆断層")

        elif type in "横ずれ":
            print("横ずれ")

        else:
            print(type)

    for x in displacement_speed:
        if x != "-":
            print(x)


def main():
    import_files()


if __name__ == '__main__':
    main()