import matplotlib.pyplot as plt
import numpy as np
import glob
from bias import bias
from flat import flat
from science import science
from sky import sky


def main():

    # Getting all image names:

    bias_tables = glob.glob("bias/*.fits")
    flat_tables = glob.glob("flat/*.fits")
    science_tables = glob.glob("science/*.fits")

    # Getting limits for SKY correction in first SCIENCE image:

    sky_inferior_abscissa_limit = input(
        "Please input inferior abscissa limit for sky correction based on first SCIENCE image: \n")
    sky_superior_abscissa_limit = input(
        "Please input superior abscissa limit for sky correction based on first SCIENCE image: \n")
    sky_inferior_ordinate_limit = input(
        "Please input inferior ordinate limit for sky correction based on first SCIENCE image: \n")
    sky_superior_ordinate_limit = input(
        "Please input superior ordinate limit for sky correction based on first SCIENCE image: \n")

    first_science_image = science_tables[0]

    # Calling each function to correct SCIENCE images for BIAS, FLAT and SKY:

    bias_correction = bias(bias_tables)
    bias_flat_correction = flat(flat_tables, bias_correction)
    sky_correction = sky(first_science_image, bias_correction, bias_flat_correction, sky_inferior_abscissa_limit,
                         sky_superior_abscissa_limit, sky_inferior_ordinate_limit, sky_superior_ordinate_limit)

    bias_flat_science_images = science(science_tables, bias_correction, bias_flat_correction, sky_correction)

    # Ask the user if he wants to combine all SCIENCE images:

    ask = input('Want to combine all SCIENCE images [yes/no]: ')

    if ask == 'yes':
        bias_flat_science_combination = np.median(bias_flat_science_images, axis=0)

        # Plot of single SCIENCE image:

        image = bias_flat_science_combination
        image.flatten()
        np.median(image)
        np.std(image)
        np.mean(image)

        plt.figure()
        plt.imshow(image, vmin=np.mean(image) - 2.5 * np.std(image), vmax=np.mean(image) + 2.5 * np.std(image),
                   cmap=plt.get_cmap('Greys'))
        plt.colorbar()
        plt.show()

    else:

        # Plot each SCIENCE image:

        for image in bias_flat_science_images:
            image.flatten()
            np.median(image)
            np.std(image)
            np.mean(image)

            plt.figure()
            plt.imshow(image, vmin=np.mean(image)-2.5*np.std(image), vmax=np.mean(image)+2.5*np.std(image),
                       cmap=plt.get_cmap('Greys'))
            plt.colorbar()
            plt.show()

main()
