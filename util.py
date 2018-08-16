#!/usr/bin/env python
import gdal
import numpy
import geojson
from osgeo import gdal_array
from shapely.geometry import shape


def load_img_file_as_array(img_path):
    img_ds = gdal.Open(img_path)
    img_array = gdal_array.DatasetReadAsArray(img_ds)

    return img_array


class Raster(object):

    def __init__(self):
        self.file_path = None
        self.band_array = None
        self.data_type = None
        self.projection = None
        self.num_bands = None
        self.geo_transform = None

    def load(self, file_path):
        img_ds = gdal.Open(file_path)

        self.band_array = img_ds.ReadAsArray(
            xoff=0, yoff=0, xsize=img_ds.RasterXSize, ysize=img_ds.RasterYSize)
        self.data_type = img_ds.GetRasterBand(1).DataType
        self.file_path = file_path
        self.num_bands = img_ds.RasterCount
        self.projection = img_ds.GetProjection()
        self.geo_transform = img_ds.GetGeoTransform()

    @staticmethod
    def ndvi_array(red_array, nir_array):
        return numpy.nan_to_num((red_array.astype(numpy.float32) -
                nir_array.astype(numpy.float32)) / \
               (red_array.astype(numpy.float32) +
                nir_array.astype(numpy.float32)))


class VectorGJ(object):

    def __init__(self):
        self.file_path = None
        self.dict = None

    def load(self, file_path):
        with open(file_path) as gj:
            self.dict = geojson.load(gj)

        self.file_path = file_path

    def save(self, output_file_path):
        with open(output_file_path, 'w') as fp:
            geojson.dump(self.dict, fp)

    @property
    def feature_type(self):
        return self.dict['type']

    def load_shapely(self):
        """
        loads geojson dict to a shapely object
        :return: Array of shapely objects (even if single gj feature is passed)
        """
        if self.dict is None:
            raise Exception('Geojson has not be loaded')

        if self.feature_type == 'FeatureCollection':
            return [shape(f['geometry'] for f in self.dict['features'])]
        else:
            try:
                shapely_obj = shape(self.dict)
            except:
                raise Exception(
                    'Type %s not handled by load_shapely method' % self.feature_type)
            return [shapely_obj]

    def shapely_to_geojson(self, shapelyds):
        pass


