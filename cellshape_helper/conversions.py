from ._vendor.pytorch_geometric_files import read_off, sample_points
from pyntcloud import PyntCloud
import pandas as pd
from tifffile import imread
import pymesh
from skimage.measure import marching_cubes
from tqdm import tqdm
from .util import create_dir_if_not_exist
from pathlib import Path


def tif_to_mesh(tif_directory):
    p = Path(tif_directory)
    files = list(p.glob("**/*.tif"))
    for tif_file in tqdm(files):
        tif_file_path = Path(tif_file)
        img = imread(tif_file)
        vertices, faces, normals, values = marching_cubes(img)
        mesh_obj = pymesh.form_mesh(vertices, faces, values)
        print(str(tif_directory))
        save_to_mesh_path = str(tif_directory) + "_mesh"
        create_dir_if_not_exist(save_to_mesh_path)
        split_string = tif_file_path.name.split(".")
        file_name = split_string[0]
        pymesh.save_mesh(save_to_mesh_path + file_name + ".off", mesh_obj)
        return save_to_mesh_path


def mesh_to_pc(mesh_directory, num_points):
    p = Path(mesh_directory)
    files = list(p.glob("**/*.off"))
    for mesh_file in tqdm(files):
        mesh_file_path = Path(mesh_file)
        data = read_off(mesh_file)
        points = sample_points(data=data, num=num_points)
        save_to_points_path = str(mesh_directory)[:-1] + "_points"
        create_dir_if_not_exist(save_to_points_path)
        split_string = mesh_file_path.name.split(".")
        file_name = split_string[0]
        cloud = PyntCloud(pd.DataFrame(data=points, columns=["x", "y", "z"]))
        cloud.to_file(save_to_points_path + file_name + ".ply")
        return points


def tif_to_pc_directory(tif_directory, num_points):
    mesh_directory = tif_to_mesh(tif_directory)
    mesh_to_pc(mesh_directory, num_points)


def tif_to_mesh_directory(image_directory, save_directory):
    p = Path(image_directory)
    files = list(p.glob("**/*.tif"))
    for file in tqdm(files):
        mesh_obj = tif_to_mesh(file)
        save_to = save_directory + "/"
        create_dir_if_not_exist(save_to)
        pymesh.save_mesh(save_to + file[:-3] + "off", mesh_obj)


def mesh_to_pc_directory(mesh_directory, save_directory, num_points):
    p = Path(mesh_directory)
    files = list(p.glob("**/*.obj"))
    for file in tqdm(files):
        points = mesh_to_pc(obj_file=file, num_points=num_points)
        save_to = save_directory + "/"
        create_dir_if_not_exist(save_to)
        cloud = PyntCloud(pd.DataFrame(data=points, columns=["x", "y", "z"]))
        cloud.to_file(save_to + file[:-3] + "ply")


def tif_to_pc(tif_file, num_points):
    mesh = tif_to_mesh(tif_file)
    pc = mesh_to_pc(mesh, num_points)
    return pc
