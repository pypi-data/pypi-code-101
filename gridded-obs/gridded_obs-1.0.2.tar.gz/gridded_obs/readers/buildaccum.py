class BuildAccum:
    
    def __init__(self, name=None, data_dir=None, accum_dt=None, data_recipe=None,
                       interpolate=None, median_filt=None, smooth_radius=None):
        """build accumulations

        args:
            data_dir:  [str]  /basse/dir/where/data/is/
            accum_dt:     [minutes] time during which accumulations are desired
            prefixt:   [strftime format] restrict search to files with this format
        """
        import numpy as np

        print('initializing "BuildAcum" reader')

        if name is not None:
            self.name  = name
        else:
            raise ValueError('keyword "name" must be speficied')

        if data_dir is not None:
            self.data_dir  = data_dir
        else:
            raise ValueError('keyword "data_dir" must be speficied')

        if accum_dt is not None:
            self.accum_dt  = float(accum_dt)
        else:
            raise ValueError('keyword "accum_dt" must be speficied')

        if data_recipe is not None:
            self.data_recipe  = data_recipe
        else:
            raise ValueError('keyword "data_recipe" must be speficied')

        if interpolate == 'yes':
            self.interpolate = 'yes'
        else:
            self.interpolate = 'no'

        if median_filt is not None:
            self.median_filt = np.float(median_filt)
        else:
            self.median_filt = None

        if smooth_radius is not None:
            self.smooth_radius = np.float(smooth_radius)
        else:
            self.smooth_radius = None

        #by default, data is returned on native grid
        #if needed, these variables are initialized after argument parsing in verify.py
        self.dest_lat = None
        self.dest_lon = None


    def get_data(self, validity_date, leadtime=None):
        """Build accumulation from various sources

        args:
            validity_date:  [datetime object]  date at which data is desired
            leadtime:       [datetime timedelta object]  offset with respect to validity time

        """
        import datetime
        import numpy as np
        import domcmc.fst_tools 
        import domutils.radar_tools as radar_tools

        #take leadtime into account
        if leadtime is None:
            end_date = validity_date
        else:
            end_date = validity_date + leadtime

        #get precipitation accumulation at validity date
        dat_dict = radar_tools.get_accumulation(end_date=end_date,
                                                duration=self.accum_dt,
                                                data_path=self.data_dir,
                                                data_recipe=self.data_recipe,
                                                latlon=True,
                                                dest_lat=self.dest_lat,
                                                dest_lon=self.dest_lon,
                                                median_filt=self.median_filt,
                                                smooth_radius=self.smooth_radius)


        if dat_dict is None :
            return None
        else:
            return {'values':dat_dict['accumulation'],
                    'qi_values':dat_dict['total_quality_index'],
                    'lats':dat_dict['latitudes'], 
                    'lons':dat_dict['longitudes']}
