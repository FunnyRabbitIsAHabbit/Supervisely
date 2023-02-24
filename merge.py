"""
Test task

in Python 3.10

Merge script

@author: Stanislav Ermokhin

"""

import numpy as np

from os import listdir
from skimage.io import imread

from split import read_image, save_image


def read_image_directory(image_directory: str) -> list:
    """
    Doc on function

    :param image_directory: Use 3rd party library to open image from 'filename';
    :return: Numpy representation of that image
    """

    out_images: list = []
    all_filenames: list = listdir(image_directory)

    for image_name in all_filenames:
        out_images.append((image_name, imread(f"{image_directory}/{image_name}")))

    return out_images


def process_images(images_to_process: list[np.ndarray],
                   w: int, h: int, original_shape: tuple,
                   original_d_type: np.ndarray, save: bool = False, out_filename: str = "") -> np.ndarray:
    """
    Doc on function

    :param original_d_type: data type of values;
    :param original_shape: [height, width, num of channels];
    :param x: width shift;
    :param y: height shift;
    :param w: width of output window;
    :param h: height of output window;

    :param images_to_process: np.ndarray returned by a read function;
    :param save: True to save output to a file, else False to return image;
    :param out_filename: must be specified if 'save' is True;
    :return: True or False – if image was saved, else image
    """

    out_image: np.ndarray = np.zeros(shape=original_shape, dtype=original_d_type)

    for image_name, image_data in images_to_process:
        im_atts: list = image_name.split("_")
        x_step: int = int(im_atts[0][1:])
        y_step: int = int(im_atts[1][1:])

        out_image[y_step:y_step + h, x_step:x_step + w, ...] = image_data

    if save:
        save_image(out_image, out_filename)

    return out_image


def main(input_directory: str, original_image: str) -> str:
    """
    Doc on function

    :param original_image:
    :param input_directory: file directory to open;
    :return:
    """

    images: list = read_image_directory(input_directory)
    image_attributes: list = input_directory.split("_")

    w: int = int(image_attributes[2][1:])
    h: int = int(image_attributes[3][1:])

    original: np.ndarray = read_image(original_image)
    original_shape: tuple = original.shape
    original_d_type = original.dtype

    new_image: np.ndarray = process_images(images_to_process=images,
                                           w=w, h=h, save=True,
                                           original_shape=original_shape,
                                           original_d_type=original_d_type, out_filename="new.jpg")

    valid: str = "VALID" if np.array_equal(new_image, original) else "INVALID"

    return valid


if __name__ == "__main__":
    out: str = main(input_directory="x15_y18_w15_h18_Unknown",
                    original_image="Unknown.jpg")
    print(out)
