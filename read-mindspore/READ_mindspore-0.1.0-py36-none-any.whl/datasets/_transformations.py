import cv2
from PIL import Image
from albumentations import(
    OneOf, Resize, Normalize, Compose, Transpose,
    HorizontalFlip, VerticalFlip, Flip, Cutout, RandomCrop,
    CenterCrop, ShiftScaleRotate, Rotate, 
    RandomContrast, RandomBrightness, RandomBrightnessContrast,
    RandomGamma, CLAHE, IAASharpen, IAAEmboss, FancyPCA, 
    GaussianBlur, GaussNoise, Blur, MotionBlur, MedianBlur, 
    HueSaturationValue, OpticalDistortion, GridDistortion
)

def randomcrop_transform_plus(img_size = (256, 256), crop_size = (224, 224), mean=[0,0,0], std=[1,1,1], rotation=180, border_mode=0):
    '''
    Transformations include (Resize, RandomCrop, RandomHorizontalFlip, \
    RandomVerticalFlip, Randomrotation, and normalize)
    '''
    # img_size = (height, width)
    # crop_size = (height, width)
    if isinstance(img_size, int):
        img_size = (img_size, img_size)
    if isinstance(crop_size, int):
        crop_size = (crop_size, crop_size)
    transforms_list = []
    transforms_list.extend([
        Resize(img_size[0], img_size[1], interpolation=Image.BILINEAR),
        VerticalFlip(p=0.5),
        HorizontalFlip(p=0.5),
        Rotate(rotation, p=1.0, border_mode=border_mode),
        RandomCrop(crop_size[0], crop_size[1]),
        Normalize(mean=mean, std=std, p=1),
        ]) 
    transforms = Compose(transforms_list)
    return transforms

def randomcrop_transform(img_size = (256, 256), crop_size = (224, 224), mean=[0,0,0], std=[1,1,1], border_mode=0):
    '''
    Transformations include (Resize, RandomCrop and normalize)
    '''
    # img_size = (height, width)
    # crop_size = (height, width)
    if isinstance(img_size, int):
        img_size = (img_size, img_size)
    if isinstance(crop_size, int):
        crop_size = (crop_size, crop_size)
    transforms_list = []
    transforms_list.extend([
        Resize(img_size[0], img_size[1], interpolation=Image.BILINEAR),
        RandomCrop(crop_size[0], crop_size[1]),
        Normalize(mean=mean, std=std, p=1),
        ]) 
    transforms = Compose(transforms_list)
    return transforms

def centercrop_tranform(img_size = (256, 256), crop_size = (224, 224), mean=(0,0,0), std=(1,1,1)):
    '''
    Basic transformations only include (resize, centercrop and normalize)
    '''
    # img_size = (height, width)
    # crop_size = (height, width) 
    if isinstance(img_size, int):
        img_size = (img_size, img_size)
    if isinstance(crop_size, int):
        crop_size = (crop_size, crop_size)
    transforms_list = []
    transforms_list.extend([
        Resize(img_size[0], img_size[1], interpolation=Image.BILINEAR),
        CenterCrop(crop_size[0], crop_size[1]),
        Normalize(mean=mean, std=std, p=1),
        ]) 
    transforms = Compose(transforms_list)
    return transforms

def randomflip_transform(img_size = (256, 256), mean=[0,0,0], std=[1,1,1]):
    '''
    Transformations include (Resize,RandomHorizontalFlip, RandomHorizontalFlip, \
    RandomVerticalFlip, and normalize)
    '''
    # img_size = (height, width)
    # crop_size = (height, width)
    if isinstance(img_size, int):
        img_size = (img_size, img_size)
    transforms_list = []
    transforms_list.extend([
        Resize(img_size[0], img_size[1], interpolation=Image.BILINEAR),
        VerticalFlip(p=0.5),
        HorizontalFlip(p=0.5),
        Normalize(mean=mean, std=std, p=1),
        ]) 
    transforms = Compose(transforms_list)
    return transforms

def resize_transform_basic(img_size = (256, 256), mean=[0,0,0], std=[1,1,1]):
    '''
    Transformations only include (Resize and normalize)
    '''
    # img_size = (height, width)
    # crop_size = (height, width)
    if isinstance(img_size, int):
        img_size = (img_size, img_size)
    transforms_list = []
    transforms_list.extend([
        Resize(img_size[0], img_size[1], interpolation=Image.BILINEAR),
        Normalize(mean=mean, std=std, p=1),
        ]) 
    transforms = Compose(transforms_list)
    return transforms

def rotationflip_transform(img_size = (256, 256), mean=[0,0,0], std=[1,1,1], rotation=180, border_mode=0):
    '''
    Transformations only include (Resize, RandomHorizontalFlip,  RandomVerticalFlip, Randomrotation, and Normalize)
    '''
    # img_size = (height, width)
    # crop_size = (height, width)
    if isinstance(img_size, int):
        img_size = (img_size, img_size)
    transforms_list = []
    transforms_list.extend([
        Resize(img_size[0], img_size[1], interpolation=Image.BILINEAR),
        VerticalFlip(p=0.5),
        HorizontalFlip(p=0.5),
        Rotate(rotation, p=1.0, border_mode=border_mode),
        Normalize(mean=mean, std=std, p=1),
        ]) 
    transforms = Compose(transforms_list)
    return transforms