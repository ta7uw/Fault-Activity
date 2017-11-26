import numpy as np


def plot_grid():

    # xmin, ymin , xmax, ymax
    SHIKOKU_BOX = [31.0, 129.0, 34.0, 132.0]
    KYUSYU_BOX = [33.7, 130.7, 35.7, 135.0]

    # degree per 40km
    LON_DEGREE = 40 / 93.45286
    LAT_DEGREE = 40 / 111.263

    grid2SHIKOKU = []
    for lon in np.arange(start=SHIKOKU_BOX[0], stop=SHIKOKU_BOX[2], step=LON_DEGREE, dtype=float):
        for lat in np.arange(start=SHIKOKU_BOX[1], stop=SHIKOKU_BOX[3], step=LAT_DEGREE, dtype=float):
            center_point = lon, lat
            bbox = (lon - LON_DEGREE/2, lat - LAT_DEGREE/2, lon + LON_DEGREE/2, lat + LAT_DEGREE/2)
            grid_data = center_point, bbox
            grid2SHIKOKU.append(grid_data)

    grid2KYUSYU = []
    for lon in np.arange(start=KYUSYU_BOX[0], stop=KYUSYU_BOX[2], step=LON_DEGREE, dtype=float):
        for lat in np.arange(start=KYUSYU_BOX[1], stop=KYUSYU_BOX[3], step=LAT_DEGREE, dtype=float):
            center_point = lon, lat
            bbox = (lon - LON_DEGREE / 2, lat - LAT_DEGREE / 2, lon + LON_DEGREE / 2, lat + LAT_DEGREE / 2)
            grid_data = [center_point, bbox]
            grid2KYUSYU.append(grid_data)

    print(grid2SHIKOKU)
    print(grid2KYUSYU)
    print(len(grid2KYUSYU))
    print(len(grid2SHIKOKU))

if __name__ == '__main__':
    plot_grid()