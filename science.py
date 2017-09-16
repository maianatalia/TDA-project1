import astropy.io.fits as fits
import numpy as np


def science(science_tables, bias_correction, bias_flat_correction, sky_correction):
    science_images = science_tables

    # Opening data for each SCIENCE image:

    bias_flat_science_images = []
    for value in science_images:
        image, header = fits.getdata(value, header=True)
        image = np.array(image, dtype=np.float)

        # BIAS, FLAT and SKY correction applied to SCIENCE images:

        bias_flat_science_images.append(((image - bias_correction) / bias_flat_correction) - sky_correction)

    # Freeing system memory:

    del science_images

    return bias_flat_science_images
