import numpy as np
import pandas as pd


def plot_grid():

    # xmin, ymin , xmax, ymax
    KYUSYU_BOX = [129.0, 31.0, 132.0, 34.0]
    SHIKOKU_BOX = [130.7, 33.7, 135.0, 35.7]

    # degree per 20km
    LON_DEGREE = 20 / 93.45286
    LAT_DEGREE = 20 / 111.263

    grid2SHIKOKU = pd.DataFrame(index=[], columns=["center-lon", "center-lat", "xmin", "ymin", "xmax", "ymax"])
    for lon in np.arange(start=SHIKOKU_BOX[0], stop=SHIKOKU_BOX[2], step=LON_DEGREE, dtype=float):

        for lat in np.arange(start=SHIKOKU_BOX[1], stop=SHIKOKU_BOX[3], step=LAT_DEGREE, dtype=float):

            center_point_lon = lon
            center_point_lat = lat
            bbox = [lon - LON_DEGREE, lat - LAT_DEGREE, lon + LON_DEGREE, lat + LAT_DEGREE]
            grid_data = [center_point_lon, center_point_lat, bbox[0], bbox[1], bbox[2], bbox[3]]
            grid_data = pd.Series(grid_data, index=grid2SHIKOKU.columns)
            grid2SHIKOKU = grid2SHIKOKU.append(grid_data, ignore_index=True)

    grid2KYUSYU = pd.DataFrame(index=[], columns=["center-lon", "center-lat", "xmin", "ymin", "xmax", "ymax"])
    for lon in np.arange(start=KYUSYU_BOX[0], stop=KYUSYU_BOX[2], step=LON_DEGREE, dtype=float):

        for lat in np.arange(start=KYUSYU_BOX[1], stop=KYUSYU_BOX[3], step=LAT_DEGREE, dtype=float):
            center_point_lon = lon
            center_point_lat = lat
            bbox = [lon - LON_DEGREE, lat - LAT_DEGREE, lon + LON_DEGREE, lat + LAT_DEGREE]
            grid_data = [center_point_lon, center_point_lat, bbox[0], bbox[1], bbox[2], bbox[3]]
            grid_data = pd.Series(grid_data, index=grid2SHIKOKU.columns)
            grid2KYUSYU = grid2KYUSYU.append(grid_data, ignore_index=True)

    grid2KYUSYU.to_csv("csv/grid-KYUSYU.csv", encoding="utf-8")
    grid2SHIKOKU.to_csv("csv/grid-SHIKOKU.csv",  encoding="utf-8")

if __name__ == '__main__':
    plot_grid()