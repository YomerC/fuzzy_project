from fun import *
from config import *
from time import perf_counter


def fuzzy_control(ant_1, ant_2, cons_1):
    """
    Parameters
    ----------
    ant_1 : TYPE
        DESCRIPTION.
    ant_2 : TYPE
        DESCRIPTION.
    cons_1 : TYPE
        DESCRIPTION.

    Returns
    -------
    hsi_value : TYPE
        DESCRIPTION.

    """
  
    # generate fuzzy universe variables antecedent and consequent
    depth = ctrl.Antecedent(ant_1, 'depth')
    velocity = ctrl.Antecedent(ant_2, 'velocity')
    hsi = ctrl.Consequent(cons_1, 'hsi')
    
    # generate fuzzy membership functions
    depth['depth_low'] = fuzz.trapmf(depth.universe, [0, 0, 0.15, 0.35])
    depth['depth_medium'] = fuzz.trapmf(depth.universe, [0.15, 0.35, 0.8, 1.1])
    depth['depth_high'] = fuzz.trapmf(depth.universe, [0.8, 1.1, 1.45, 1.45])
    
    velocity['vel_low'] = fuzz.trapmf(velocity.universe, [0, 0, 0.4, 1])
    velocity['vel_medium'] = fuzz.trapmf(velocity.universe, [0.4, 1, 1.4, 2])
    velocity['vel_high'] = fuzz.trapmf(velocity.universe, [1.4, 2, 3.4, 3.4])
    
    hsi['hsi_low'] = fuzz.trapmf(hsi.universe, [0, 0, 0.1, 0.3])
    hsi['hsi_medium'] = fuzz.trapmf(hsi.universe, [0.1, 0.3, 0.7, 0.9])
    hsi['hsi_high'] = fuzz.trapmf(hsi.universe, [0.7, 0.9, 1, 1])
    
    # define the fuzzy rules
    rule_1 = ctrl.Rule(antecedent=(depth['depth_high'] & velocity['vel_high']),
                       consequent=hsi['hsi_low'])
    rule_2 = ctrl.Rule(antecedent=(depth['depth_high'] & velocity['vel_medium']),
                       consequent=hsi['hsi_medium'])
    rule_3 = ctrl.Rule(antecedent=(depth['depth_high'] & velocity['vel_low']),
                       consequent=hsi['hsi_low'])
    rule_4 = ctrl.Rule(antecedent=(depth['depth_medium'] & velocity['vel_high']),
                       consequent=hsi['hsi_high'])
    rule_5 = ctrl.Rule(antecedent=(depth['depth_medium'] & velocity['vel_medium']),
                       consequent=hsi['hsi_high'])
    rule_6 = ctrl.Rule(antecedent=(depth['depth_medium'] & velocity['vel_low']),
                       consequent=hsi['hsi_low'])
    rule_7 = ctrl.Rule(antecedent=(depth['depth_low'] & velocity['vel_high']),
                       consequent=hsi['hsi_low'])
    rule_8 = ctrl.Rule(antecedent=(depth['depth_low'] & velocity['vel_medium']),
                       consequent=hsi['hsi_medium'])
    rule_9 = ctrl.Rule(antecedent=(depth['depth_low'] & velocity['vel_low']),
                       consequent=hsi['hsi_low'])
    
    # Aggregate the output membership functions 
    aggregate = ctrl.ControlSystem(rules=[rule_1, rule_2, rule_3, 
                                       rule_4, rule_5, rule_6, 
                                       rule_7, rule_8, rule_9])
    
    # Calculate results from the Control System 
    hsi_value = ctrl.ControlSystemSimulation(aggregate)
    
    return (hsi_value)


@logger
def main():
    # get hsi result 
    hsi_result = fuzzy_control(depth_univ, vel_univ, hsi_univ)

   # load both rasters as arrays
   # raster_processing(raster_depth, depth_array, d_geot, d_prj)
   # raster_processing(raster_velocity, vel_array, v_geot, v_prj)

    raster_depth, depth_array, d_geot, d_prj  = ras.raster2array(depth_file)
    raster_velocity, vel_array, v_geot, v_prj = ras.raster2array(velocity_file)
    output_hsi = np.zeros_like(depth_array)

    # iterate over depth and velocity values
    for i in range(975):
        for j in range(1151):
            hsi_result.input["depth"] = depth_array[i, j]
            hsi_result.input["velocity"] = vel_array[i, j]
            hsi_result.compute()
            output_hsi[i, j] = hsi_result.output["hsi"]
    
   # create hsi raster 
    ras.create_raster(file_name, output_hsi, origins, pixel_width=1,
                  pixel_height=-1, epsg=5668)

if __name__ == '__main__':
    
    # Initialize universe variables 
    depth_univ = np.linspace(0, 1.5, 100)
    vel_univ = np.linspace(0, 3.1, 100)
    hsi_univ = np.linspace(0, 1, 100)
    
    # define variables
    depth_file = r"" + os.getcwd() + "/data/water_depth.tif"
    velocity_file = r"" + os.getcwd() + "/data/flow_velocity.tif" 
    
    # define a raster origin in EPSG:3857
    origins = (786986.1064724320312962, 156145.3739023693779018)

    # set the name of the output GeoTIFF raster
    file_name = r"" + os.getcwd() + "/output_raster/hsi_prueba11.tif"

    # run code and evaluate performance
    t0 = perf_counter()
    main()
    t1 = perf_counter()
    print("Time elapsed: " + str(t1 - t0))
    









