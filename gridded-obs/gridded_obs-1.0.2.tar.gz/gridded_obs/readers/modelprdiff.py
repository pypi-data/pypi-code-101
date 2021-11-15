class ModelPrDiff:
    
    def __init__(self, name=None, data_dir=None, pr_dt=None, quantity=None, prefix=None):
        """Estimate pecipitation rates by substracting PR at two different times
    
        args:
            data_dir:  [str]  /basse/dir/where/data/is/
            quantity:  [str]  quantity to verify  can only be: 'precip_rate' or 'accumulations'
            pr_dt:     [minutes] time for PR at previous time
            prefixt:   [strftime format] restrict search to files with this format
        """

        print('initializing "modelPrDiff" reader')

        if name is not None:
            self.name  = name
        else:
            raise ValueError('keyword "name" must be speficied')

        if data_dir is not None:
            self.data_dir  = data_dir
        else:
            raise ValueError('keyword "data_dir" must be speficied')

        if pr_dt is not None:
            self.pr_dt  = float(pr_dt)
        else:
            raise ValueError('keyword "pr_dt" must be speficied')

        if quantity is not None:
            self.quantity  = quantity
            if quantity == 'precip_rate':
                pass
            elif quantity == 'accumulations':
                pass
            else:
                raise ValueError('quantity can only be "precip_rate" or "accumulations"')
        else:
            raise ValueError('keyword "quantity" must be speficied')

        if prefix is not None:
            self.prefix  = prefix
        else:
            raise ValueError('keyword "prefix" must be speficied')



    def get_data(self, validity_date, leadtime=None):
        """read data from a standard file by substracting PR at two times

        args:
            validity_date:  [datetime object]  date at which data is desired
            leadtime:       [datetime timedelta object]  offset with respect to validity time

        """
        import datetime
        import logging
        import numpy as np
        import domcmc.fst_tools 

        #logging
        logger = logging.getLogger(__name__)

        #take leadtime into account
        if leadtime is None:
            this_date = validity_date
        else:
            this_date = validity_date + leadtime
    
        #beginning of filename
        this_prefix = validity_date.strftime(self.prefix)

        #get precipitation accumulation at validity date
        pr_t_dict   = domcmc.fst_tools.get_data(dir_name=self.data_dir, var_name='PR', prefix=this_prefix, datev=this_date, latlon=True)
        logger.info(f'model_pr_diff:  PR date_end:{this_date}')

        #get precipitation accumulation at validity date - pr_dt
        deltat = self.pr_dt*60. #convert minutes to seconds
        date_mdt = this_date - datetime.timedelta(seconds=deltat)
        pr_mdt_dict = domcmc.fst_tools.get_data(dir_name=self.data_dir, var_name='PR', prefix=this_prefix, datev=date_mdt)
        logger.info(f'model_pr_diff:  PR date_start:{date_mdt}')
    
        if (pr_t_dict is None) or (pr_mdt_dict is None):
            return None
        else:
            #forecast accumulation rate in mm
            #       *1000   -> conversion from meters to mm
            accumulation = (pr_t_dict['values'] - pr_mdt_dict['values'])*1000. 
            
            #forecast precip rate in mm/h
            #       *3600   -> for precip rate during one hour
            #       /deltat -> time difference between the two accumulation (PR) values that were read
            precip_rate = accumulation*3600./deltat

            if self.quantity == 'precip_rate':
                logger.info(f'model_pr_diff: outputting precip rates')
                output = precip_rate
            elif self.quantity == 'accumulations':
                logger.info(f'model_pr_diff: outputting accumulations')
                output = accumulation
            else:
                raise ValueError('Something very wrong going on here...')

            return {'values':output,
                    'qi_values':None,
                    'lats':pr_t_dict['lat'], 
                    'lons':pr_t_dict['lon']}
