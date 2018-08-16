#!/usr/bin/env python
import gdal
from osgeo import gdal_array


def load_img_file_as_array(img_path):
    img_ds = gdal.Open(img_path)
    img_array = gdal_array.DatasetReadAsArray(img_ds)

    return img_array

