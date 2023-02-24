"""
Test task

in Python 3.10

DAVIS dataset processing script

@author: Stanislav Ermokhin

"""

import numpy as np
import skvideo.io as skvio

from skimage.transform import resize
from random import randint, sample
from os import listdir

from split import read_image


RESOLUTION_P: int = 480
RESOLUTION_OTHER: int = 800
CHANNELS: int = 3
BASE_DIR: str = f"DAVIS/JPEGImages/{RESOLUTION_P}p"


def save_dataset_as_single_video(dataset: list,
                                 output_video_name: str = "output.mp4") -> None:

    with skvio.FFmpegWriter(filename=output_video_name) as writer:
        for video in dataset:
            for image in video:
                writer.writeFrame(im=image)
    
    return


def process_categories_dir(n: int = 1, dir_name: str = BASE_DIR) -> list[np.ndarray] | bool:
    
    categories: list[str] = listdir(dir_name)
    n: int = min(len(categories), n)
    target_categories: list[str] = sample(categories, n)

    video_collection_dataset: list[np.ndarray] = []

    for category in target_categories:
        inner_dir: str = f"{dir_name}/{category}"
        image_names: list[str] = list(sorted(listdir(inner_dir)))
        num_images: int = len(image_names)

        if num_images:
            image_dataset: np.ndarray = np.empty(shape=[num_images, RESOLUTION_P, RESOLUTION_OTHER, CHANNELS],
                                                 dtype=np.uint8)

            for i in range(num_images):
                image: np.ndarray = read_image(f"{inner_dir}/{image_names[i]}")
                new_image: np.ndarray = resize(image=image,
                                               output_shape=(RESOLUTION_P, RESOLUTION_OTHER),
                                               preserve_range=True, clip=True, anti_aliasing=True)
                image_dataset[i]: np.ndarray = new_image

            video_collection_dataset.append(image_dataset)
        
        else:
            return False
        
    if video_collection_dataset:
        return video_collection_dataset
    
    else:
        return False


if __name__ == "__main__":
    
    collection_out: list[np.ndarray] | bool = process_categories_dir(10)

    if collection_out:
        save_dataset_as_single_video(collection_out)
    
