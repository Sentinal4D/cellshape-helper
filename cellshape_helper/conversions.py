from ._vendor.pytorch_geometric_files import read_off, sample_points
from pyntcloud import PyntCloud
import pandas as pd
from skimage import io
import pymesh
from skimage.measure import marching_cubes
from tqdm import tqdm
from .util import create_dir_if_not_exist
from pathlib import Path


def tif_to_mesh(tif_file):
    img = io.imread(tif_file)
    vertices, faces, normals, values = marching_cubes(img)
    mesh_obj = pymesh.form_mesh(vertices, faces, values)
    return mesh_obj


def tif_to_mesh_directory(image_directory, save_directory):
    p = Path(image_directory)
    files = list(p.glob("**/*.tif"))
    for file in tqdm(files):
        mesh_obj = tif_to_mesh(file)
        save_to = save_directory + "/"
        create_dir_if_not_exist(save_to)
        pymesh.save_mesh(save_to + file[:-3] + "off", mesh_obj)


def mesh_to_pc(obj_file, num_points):
    data = read_off(obj_file)
    points = sample_points(data=data, num=num_points)
    return points


def mesh_to_pc_directory(mesh_directory, save_directory, num_points):
    p = Path(mesh_directory)
    files = list(p.glob("**/*.obj"))
    for file in tqdm(files):
        points = mesh_to_pc(obj_file=file, num_points=num_points)
        save_to = save_directory + "/"
        create_dir_if_not_exist(save_to)
        cloud = PyntCloud(pd.DataFrame(data=points, columns=["x", "y", "z"]))
        cloud.to_file(save_to + file[:-3] + "ply")


def tif_to_pc(tiffile, num_points):
    mesh = tif_to_mesh(tiffile)
    pc = mesh_to_pc(mesh, num_points)
    return pc


def tif_to_pc_directory(tif_directory, save_directory, num_points):
    p = Path(tif_directory)
    files = list(p.glob("**/*.tif"))
    for file in tqdm(files):
        tif_to_pc(file, num_points)
        pc = create_dir_if_not_exist(save_directory)
        cloud = PyntCloud(pd.DataFrame(data=pc, columns=["x", "y", "z"]))
        cloud.to_file(save_directory + file[:-3] + "ply")
