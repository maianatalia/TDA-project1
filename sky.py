import astropy.io.fits as fits
import numpy as np


def sky(first_science_image, bias_correction, bias_flat_correction, sky_inferior_abscissa_limit,
        sky_superior_abscissa_limit, sky_inferior_ordinate_limit, sky_superior_ordinate_limit):

    # Opening first SCIENCE image to measure the SKY:

    image = fits.open(first_science_image)
    sky_data = image[0].data

    # Delimiting portion of first SCIENCE image that gives us the SKY:

    inferior_ordinate_limit = int(sky_inferior_ordinate_limit) - 1
    inferior_abscissa_limit = int(sky_inferior_abscissa_limit) - 1
    superior_ordinate_limit = int(sky_superior_ordinate_limit)
    superior_abscissa_limit = int(sky_superior_abscissa_limit)

    sky_image = sky_data[inferior_ordinate_limit:superior_ordinate_limit,
                         inferior_abscissa_limit:superior_abscissa_limit]

    # Sampling the same portion of BIAS correction and FLAT correction to apply to SKY image:

    sky_bias_correction = bias_correction[inferior_ordinate_limit:superior_ordinate_limit,
                                          inferior_abscissa_limit:superior_abscissa_limit]
    sky_bias_flat_correction = bias_flat_correction[inferior_ordinate_limit:superior_ordinate_limit,
                                                    inferior_abscissa_limit:superior_abscissa_limit]

    # BIAS and FLAT correction applied to SKY images:

    sky_correction = (sky_image - sky_bias_correction)/sky_bias_flat_correction

    # Combining values of SKY correction:

    sky_correction = np.median(sky_correction)

    return sky_correction
