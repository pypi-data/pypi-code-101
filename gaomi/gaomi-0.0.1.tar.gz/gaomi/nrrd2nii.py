# A script to convert nrrd format segmentation to nii.gz format segmentation
# I'm certain that it works well when the direction is (1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 1.0)
# To do : validate the script on other direction conditions
# @GHJ 2021-11-3 15:35:15

# Change the script to the format of Python function
# I could almost say that this function works well no matter what the direction of your image is!
# @GHJ 2021-11-8 18:36:43

import SimpleITK as sitk
import numpy as np

def ReadNrrdAsSitkImage(seg_nrrd_path:str, base_image_path:str):
    """Read .nrrd format segmentation file as SimpleITK image.
    
    Parameters
    ----------
    seg_nrrd_path:
        
      file path of .nrrd format segmentation file
    
    base_image_path:
        
      file path of the base image of the segmentation above
      
    Make sure all paths do not contain any Chinese Characters!
        
    Returns
    ----------
    An image in the format of SimpleITK
    """
    seg = sitk.ReadImage(seg_nrrd_path)
    arr_seg = sitk.GetArrayFromImage(seg)
    origin_seg = seg.GetOrigin()
    spacing_seg = seg.GetSpacing()
    direction_seg = seg.GetDirection()
    # print(direction_seg)

    img = sitk.ReadImage(base_image_path)
    arr_img = sitk.GetArrayFromImage(img)
    origin_img = img.GetOrigin()
    spacing_img = img.GetSpacing()
    direction_img = img.GetDirection()

    # print(origin_img, origin_seg)
    # print(spacing_img, spacing_seg)
    # print(direction_img, direction_seg)

    diff_0 = abs(round((origin_img[0] - origin_seg[0]) / spacing_seg[0]))
    diff_1 = abs(round((origin_img[1] - origin_seg[1]) / spacing_seg[1]))
    diff_2 = abs(round((origin_img[2] - origin_seg[2]) / spacing_seg[2]))
    # print(diff_0, diff_1, diff_2)


    arr_new = np.pad(arr_seg, ((diff_2, arr_img.shape[0]-arr_seg.shape[0]-diff_2), \
                            (diff_1, arr_img.shape[1]-arr_seg.shape[1]-diff_1), \
                            (diff_0, arr_img.shape[2]-arr_seg.shape[2]-diff_0)),'constant', constant_values=(0, 0))

    # print(arr_seg.shape)
    # print(arr_new.shape)
    # print(arr_img.shape)

    seg_new = sitk.GetImageFromArray(arr_new)
    seg_new.SetDirection(direction_img)
    seg_new.SetOrigin(origin_img)
    seg_new.SetSpacing(spacing_img)
    return seg_new

def SaveNrrdAsNiiGz(nrrd_path:str, image_path:str, save_path:str):
    """Save .nrrd format segmentation As .nii.gz format.

    Parameters
    ----------
    nrrd_path:

      file path of .nrrd format segmentation file

    image_path:

      file path of the base image of the segmentation above

    save_path:
    
      the path you want to save the .nii.gz format segmentation
      
    Make sure all paths do not contain any Chinese Characters!
    """
    seg = sitk.ReadImage(nrrd_path)
    arr_seg = sitk.GetArrayFromImage(seg)
    origin_seg = seg.GetOrigin()
    spacing_seg = seg.GetSpacing()
    direction_seg = seg.GetDirection()
    # print(direction_seg)

    img = sitk.ReadImage(image_path)
    arr_img = sitk.GetArrayFromImage(img)
    origin_img = img.GetOrigin()
    spacing_img = img.GetSpacing()
    direction_img = img.GetDirection()

    # print(origin_img, origin_seg)
    # print(spacing_img, spacing_seg)
    # print(direction_img, direction_seg)

    diff_0 = abs(round((origin_img[0] - origin_seg[0]) / spacing_seg[0]))
    diff_1 = abs(round((origin_img[1] - origin_seg[1]) / spacing_seg[1]))
    diff_2 = abs(round((origin_img[2] - origin_seg[2]) / spacing_seg[2]))
    # print(diff_0, diff_1, diff_2)


    arr_new = np.pad(arr_seg, ((diff_2, arr_img.shape[0]-arr_seg.shape[0]-diff_2), \
                            (diff_1, arr_img.shape[1]-arr_seg.shape[1]-diff_1), \
                            (diff_0, arr_img.shape[2]-arr_seg.shape[2]-diff_0)),'constant', constant_values=(0, 0))

    # print(arr_seg.shape)
    # print(arr_new.shape)
    # print(arr_img.shape)

    seg_new = sitk.GetImageFromArray(arr_new)
    seg_new.SetDirection(direction_img)
    seg_new.SetOrigin(origin_img)
    seg_new.SetSpacing(spacing_img)
    sitk.WriteImage(seg_new, save_path)