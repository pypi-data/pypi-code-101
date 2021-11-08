# flake8: noqa

import numpy
import numpy as np
import scipy
from aydin.features.fast.fast_features import FastFeatureGenerator
from skimage.data import camera
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

from aydin.io.datasets import normalise, add_noise
from aydin.it.fgr import ImageTranslatorFGR
from aydin.regression.lgbm import LGBMRegressor
from aydin.util.log.log import Log


def demo(image, name):
    """
    Demo for self-supervised denoising using camera image with synthetic noise
    """

    Log.enable_output = True

    image = image[0:510, 0:510]
    image = normalise(image.astype(np.float32))

    noisy = add_noise(image)
    kernel = numpy.array([[0.25, 0.5, 0.25]])
    noisy = scipy.ndimage.convolve(noisy, kernel, mode='mirror')

    # brute-force feature-exclusion based extended blindspot:
    generator = FastFeatureGenerator(
        include_corner_features=True,
        include_scale_one=True,
        include_fine_features=True,
        include_line_features=True,
        include_spatial_features=True,
    )
    regressor = LGBMRegressor(patience=20, max_num_estimators=2048)

    itnbs = ImageTranslatorFGR(feature_generator=generator, regressor=regressor)

    itwbs = ImageTranslatorFGR(
        feature_generator=generator, regressor=regressor, blind_spots='auto'
    )

    itnbs.train(noisy)
    denoised_nbs = itnbs.translate(noisy)

    itwbs.train(noisy)
    denoised_wbs = itwbs.translate(noisy)

    image = numpy.clip(image, 0, 1)
    noisy = numpy.clip(noisy, 0, 1)
    denoised_nbs = numpy.clip(denoised_nbs, 0, 1)
    denoised_wbs = numpy.clip(denoised_wbs, 0, 1)

    psnr_noisy = psnr(image, noisy)
    ssim_noisy = ssim(image, noisy)
    psnr_denoised_nbs = psnr(image, denoised_nbs)
    ssim_denoised_nbs = ssim(image, denoised_nbs)
    psnr_denoised_wbs = psnr(image, denoised_wbs)
    ssim_denoised_wbs = ssim(image, denoised_wbs)

    print("noisy      :", psnr_noisy, ssim_noisy)
    print("denoised no extended blind-spot  :", psnr_denoised_nbs, ssim_denoised_nbs)
    print("denoised with extended blind-spot:", psnr_denoised_wbs, ssim_denoised_wbs)

    import napari

    with napari.gui_qt():
        viewer = napari.Viewer()
        viewer.add_image(image, name='image')
        viewer.add_image(noisy, name='noisy')
        viewer.add_image(denoised_nbs, name='denoised_nbs')
        viewer.add_image(denoised_wbs, name='denoised_wbs')


camera_image = camera()
demo(camera_image, "camera")
# lizard_image = lizard()
# demo(lizard_image, "lizard")
# pollen_image = pollen()
# demo(pollen_image, "pollen")
# dots_image = dots()
# demo(dots_image, "dots")
# newyork_image = newyork()
# demo(newyork_image, "newyork")
