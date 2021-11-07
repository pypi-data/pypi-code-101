import rasterio
import urllib
import xarray as xr
import numpy as np
from tqdm import tqdm
import owslib.wcs as wcs
import requests


class EMODnetData:
    def __init__(self, identifier, url, version, resolutionx, resolutiony, column_name):
        self.identifier = identifier
        self.url = url
        self.resolutionx = resolutionx
        self.resolutiony = resolutiony
        self.w = wcs.WebCoverageService(self.url, version=version)
        self.column_name = column_name

    def __call__(self, df):
        return self.assign_wcs_df(df)

    def get_bbox(self, df):
        bbox = df.total_bounds
        # Make sure the bbox is big enough to download some data
        if abs(bbox[2] - bbox[0]) <= self.resolutionx * 2:
            bbox[0] -= 2 * self.resolutionx
            bbox[2] += 2 * self.resolutionx
        if abs(bbox[3] - bbox[1]) <= self.resolutiony * 2:
            bbox[1] -= 2 * self.resolutiony
            bbox[3] += 2 * self.resolutiony

        return list(bbox)

    def assign_wcs_df(self, df):
        df_4326 = df.to_crs(epsg=4326)
        bbox = self.get_bbox(df_4326)
        wcs_response = self.w.getCoverage(identifier=self.identifier, bbox=bbox,
                                          crs=df_4326.crs.to_string(), format='image/tiff',
                                          resx=self.resolutionx, resy=self.resolutiony)
        try:
            tif_file = urllib.request.urlretrieve(wcs_response.geturl())
            tif_raster = xr.open_rasterio(tif_file[0])
            lat_points = xr.DataArray(df_4326.geometry.y, dims='points')
            lon_points = xr.DataArray(df_4326.geometry.x, dims='points')
            df[self.column_name] = tif_raster.sel(x=lon_points, y=lat_points, method='nearest').values[0]
        except rasterio.errors.RasterioIOError:
            print('url %s was not downloaded. Check possible errors' % wcs_response.geturl())

        return df


class ShippingData(EMODnetData):
    def __init__(self, layer_name='rd', boat_type='All'):
        """
        Will return the shipping intensity of the year and month of each sample from EMODnet Human Activities
        https://www.emodnet-humanactivities.eu/

        Parameters
        ----------
        layer_name: str
            Can be 'rd' for Route Density or 'st' for Shipping intensity
        boat_type: str

        """
        resolutionx = 0.00833333
        resolutiony = 0.00833333
        url = 'https://ows.emodnet-humanactivities.eu/wcs'
        self.column_name = None
        self.identifier = None
        self.layer_name = None
        self.boat_type = None
        self.set_layer_type(layer_name, boat_type)
        self.set_layer_date(2020, 10)
        version = '1.0.0'
        super().__init__(self.identifier, url, version, resolutionx, resolutiony, column_name=self.column_name)

    def __call__(self, df):
        """
        Add the specified layer data to the df

        Parameters
        ----------
        df : GeoDataFrame
            datetime as index and a column geometry

        Returns
        -------
        The GeoDataFrame updated
        """
        for (year, month), df_slice in tqdm(df[['geometry']].groupby([df.index.year, df.index.month])):
            self.set_layer_date(year, month)
            super().__call__(df_slice)
        return df

    def set_layer_date(self, year, month):
        """
        Set the layer year and month

        Parameters
        ----------
        year: int
            Year to download
        month: int
            Month of the year to download

        Returns
        -------
        String with the layer identifier as a string
        """
        self.identifier = 'emodnet:%s_%02d_%s_%s' % (year, month, self.layer_name, self.boat_type)
        return self.identifier

    def set_layer_type(self, layer_name, boat_type):
        """
        Change the layer type (type of layer and type of boat)

        Parameters
        ----------
        layer_name: string
            Can be 'rd' for route density or 'st' for vessel density
        boat_type: string
            Can be All, Cargo, Fishing, Passenger, Tanker or Other

        """
        if layer_name == 'rd':
            self.column_name = 'route_density'
        elif layer_name == 'st':
            self.column_name = 'ship_density'
        else:
            raise ValueError('%s is not a known layer' % layer_name)
        self.layer_name = layer_name
        self.boat_type = boat_type


class BathymetryData(EMODnetData):
    def __init__(self):
        """
        Read the bathymetry from EMODnet
        """
        resolutionx = 0.00833333
        resolutiony = 0.00833333
        identifier = 'emodnet:mean'
        url = 'https://ows.emodnet-bathymetry.eu/wcs'
        version = '1.0.0'
        column_name = 'bathymetry'
        super().__init__(identifier, url, version, resolutionx, resolutiony, column_name)

    @staticmethod
    def get_bathymetry(location):
        """
        Return the bathymetry of a certain point from EMODnet
        Parameters
        ----------
        location : geometry object
            Location

        Returns
        -------
        Bathymetry as a positive number
        """
        point_str = str(location)
        response = requests.get("https://rest.emodnet-bathymetry.eu/depth_sample?geom=%s" % point_str)
        if response.status_code == 200:
            depth = response.json()['avg']
        else:
            depth = np.nan
        return depth
