from skimage import io
import pymesh
from skimage.measure import marching_cubes
from tqdm import tqdm
from util import create_dir_if_not_exist
from pathlib import Path


def mesh_conversion(image_directory, save_directory):
    p = Path(image_directory)
    files = list(p.glob("**/*.tif"))
    for file in tqdm(files):
        img = io.imread(file)
        vertices, faces, normals, values = marching_cubes(img)
        mesh_obj = pymesh.form_mesh(vertices, faces, values)
        save_to = save_directory + "/"
        create_dir_if_not_exist(save_to)
        pymesh.save_mesh(save_to + file[:-3] + 'off', mesh_obj)
