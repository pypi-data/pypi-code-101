# @GHJ 2021-11-8 20:30:17

import SimpleITK as sitk
import os
import numpy as np

def ReadDcmAsSitkImage(dcm_dir:str):
    """Read a dicom series as SimpleITK image.

    Parameters
    ----------
    dcm_dir:

      path of the folder that contains dicom series
      
      Make sure it does not contain any Chinese Characters!
      
      The file structure should be like:
      
        dcm_dir/
        
            1.DCM
        
            2.DCM
        
            ...
            
            xx.DCM

    Returns
    ----------
    An image in the format of SimpleITK
    """
    if dcm_dir[-1] != '/':
        dcm_dir += '/'
    for i in range(1, len(os.listdir(dcm_dir)) + 1):
        dcm1 = sitk.ReadImage(dcm_dir + '%d.DCM'%i)
        if i == 1:
            origin = dcm1.GetOrigin()
            arr = sitk.GetArrayFromImage(dcm1)
            spacing = list(dcm1.GetSpacing())
            direction = dcm1.GetDirection()
        elif i == 2:
            spacing[2] = abs(dcm1.GetOrigin()[2] - origin[2])
            arr = np.concatenate((arr, sitk.GetArrayFromImage(dcm1)), 0)
        else:
            arr = np.concatenate((arr, sitk.GetArrayFromImage(dcm1)), 0)
        # print(arr.shape)

    result = sitk.GetImageFromArray(arr)
    result.SetDirection(direction)
    result.SetOrigin(origin)
    result.SetSpacing(spacing)
    
    return result  