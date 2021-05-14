"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 3
N_COLS = 4
PATCH_SIZE = 129
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'simba.jpg'


def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    # This is an example which should generate a pinkish patch
    for x_loc in range(N_COLS):
        for y_loc in range(N_ROWS):
            r = random.uniform(0, 2)
            g = random.uniform(0, 1)
            b = random.uniform(0, 1.5)
            patch = make_recolored_patch(r, g, b)
            final_image = put_patch(final_image, patch, x_loc, y_loc)
    final_image.show()


def put_patch(main_img, patch_img, row, col):
    x_start = row * PATCH_SIZE
    y_start = col * PATCH_SIZE
    for y in range(patch_img.height):
        for x in range(patch_img.width):
            pix = patch_img.get_pixel(x, y)
            main_img.set_pixel(x + x_start, y + y_start, pix)
    return main_img


def make_recolored_patch(red_scale, green_scale, blue_scale):
    """
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    """
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red = red_scale * pixel.red
        pixel.green = green_scale * pixel.green
        pixel.blue = blue_scale * pixel.blue
    return patch


if __name__ == '__main__':
    main()
