"""
Test task

in Python 3.10

Split script

@author: Stanislav Ermokhin

"""

import numpy as np

from os import mkdir, listdir
from skimage.io import imread, imsave


def read_image(filename: str) -> np.ndarray:
    """
    Doc on function

    :param filename: Use 3rd party library to open image from 'filename';
    :return: Numpy representation of that image
    """

    return imread(filename)


def process_image(image_to_process: np.ndarray,
                  x: int, y: int, w: int,
                  h: int, save: bool = False, out_filename: str = "") -> list | bool:
    """
    Doc on function

    :param x: width shift;
    :param y: height shift;
    :param w: width of output window;
    :param h: height of output window;
    :param image_to_process: np.ndarray returned by a read function;
    :param save: True to save output to a file, else False to return image;
    :param out_filename: must be specified if 'save' is True;
    :return: True or False – if image was saved, else image
    """

    assert x <= w and y <= h, """X Step must be less than (or equal to) width and"""
    """Y step must be less than (or equal to) height"""

    out_filename = out_filename.split(".")[0] or "Unknown"
    out_directory_name = f"x{x}_y{y}_w{w}_h{h}_{out_filename}"
    im_width, im_height, _ = image_to_process.shape

    out_images = []
    for y_step in range(0, im_height, y):
        for x_step in range(0, im_width, x):
            out_images.append((f"x{x_step}_y{y_step}_{out_filename}.png",
                               image_to_process[y_step:y_step + h, x_step:x_step + w, ...]))

    if save:
        if out_directory_name not in listdir():
            mkdir(out_directory_name)

        for image_name, image_data in out_images:
            save_image(image_data, f"{out_directory_name}/{image_name}")

        return True

    else:

        return out_images


def save_image(image_to_save: np.ndarray, output_filename: str) -> bool:
    """
    Doc on function

    :param image_to_save:
    :param output_filename:
    :return:
    """

    imsave(arr=image_to_save, fname=output_filename, check_contrast=False)

    return True


def main(input_file: str,
         coordinates: dict[str, int]) -> bool:
    """
    Doc on function

    :param coordinates: x, y, w, h
    :param input_file: filename to open;
    :return:
    """

    image: np.ndarray = read_image(input_file)
    new_image: bool = process_image(image, **coordinates, save=True)

    return new_image


if __name__ == "__main__":
    coords = {"x": 15, "y": 18, "w": 15, "h": 18}
    main(input_file="Unknown.jpg",
         coordinates=coords)
