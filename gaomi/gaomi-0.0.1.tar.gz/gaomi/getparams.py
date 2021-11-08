# @GHJ 2021-11-8 20:29:47

import SimpleITK as sitk
import copy

def GetParams(image:sitk.Image):
    """Get the Spacing, Origion, Direction of a SimpleITK Image and save them into a list.
    
    Parameters
    ----------
    image:

      a SimpleITK Image
    """
    return [image.GetSpacing(), image.GetOrigin(), image.GetDirection()]

def SetParams(image:sitk.Image, params:list):
    """Set the Spacing, Origin, Direction of a SimpleITK Image.
    
    No replacement.
    
    Parameters
    ----------
    image:

      a SimpleITK Image (the params of this Image will NOT change!)
      
    params:
    
      a list contains Spacing, Origin, Direction you want to set
      
    Returns
    ----------
    a SimpleITK Image with the params you want
    """
    image_new = copy.deepcopy(image)
    image_new.SetSpacing(params[0])
    image_new.SetOrigin(params[1])
    image_new.SetDirection(params[2])
    
    return image_new

def SetParams_(image:sitk.Image, params:list):
    """Set the Spacing, Origin, Direction of a SimpleITK Image.

    Replace the origin Image.
    
    Parameters
    ----------
    image:

      a SimpleITK Image (the params of this Image WILL change!)

    params:

      a list contains Spacing, Origin, Direction you want to set
    """
    image.SetSpacing(params[0])
    image.SetOrigin(params[1])
    image.SetDirection(params[2])