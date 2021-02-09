from raster_processing import *
from config import *
from main import *



def create_raster(file_name, raster_array, nan_value=-9999.0):
    
    # check out driver
    driver = gdal.GetDriverByName('GTiff')
    driver.Register()

    # create raster dataset with number of cols and rows of the input array
    cols = raster_array.shape[1]
    rows = raster_array.shape[0]
    new_raster = driver.Create(file_name, cols, rows, 
                                bands=1, eType=gdal.GDT_Float32)    

    # geotransform and projection
    new_raster.SetGeoTransform(d_geot)
    new_raster.SetProjection(d_prj)
    
    # retrieve band number 1
    band = new_raster.GetRasterBand(1)
    band.SetNoDataValue(nan_value)
    band.WriteArray(raster_array)
    band.SetScale(1.0)

    # release raster band
    band.FlushCache()
    



# # set the name of the output GeoTIFF raster
# file_name = r"" + os.getcwd() + "/output_raster/hsi_dem.tif"

# # call create_raster to create a 1-m-resolution raster in EPSG:4326 projection
# create_raster(file_name, z) 

