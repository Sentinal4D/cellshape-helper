from .vendor.pytorch_geometric_files import read_off, sample_points
from pyntcloud import PyntCloud
import pandas as pd
from tifffile import imread
import trimesh
from skimage.measure import marching_cubes, regionprops
from tqdm import tqdm
from .util import create_dir_if_not_exist
from pathlib import Path
import os
import numpy as np

def tif_to_mesh(tif_directory, save_directory):
    p = Path(tif_directory)
    files = list(p.glob("*.tif"))
    for tif_file in tqdm(files):
        tif_file_path = Path(tif_file)
        img = imread(tif_file)
        vertices, faces, normals, values = marching_cubes(img)
        mesh_obj = trimesh.Trimesh(
            vertices=vertices, faces=faces, process=False
        )
        save_to_mesh_path = save_directory
        create_dir_if_not_exist(save_to_mesh_path)
        # split_string = tif_file_path.name.split(".")
        # file_name = split_string[0]
        file_name = tif_file_path.name[:-4]
        mesh_obj.export(save_to_mesh_path + file_name + ".off")


def mesh_to_pc(mesh_directory, num_points, save_dir):
    p = Path(mesh_directory)
    files = list(p.glob("*.off"))
    for mesh_file in tqdm(files):
        mesh_file_path = Path(mesh_file)
        data = read_off(mesh_file)
        # changed to .numpy() to avoid issue with pyntcloud
        points = sample_points(data=data, num=num_points).numpy()
        save_to_points_path = save_dir
        create_dir_if_not_exist(save_to_points_path)
        # split_string = mesh_file_path.name.split(".")
        # file_name = split_string[0]
        file_name = mesh_file_path.name[:-4]
        cloud = PyntCloud(pd.DataFrame(data=points, columns=["x", "y", "z"]))
        cloud.to_file(save_to_points_path + file_name + ".ply")


def tif_to_pc_directory(tif_directory, save_mesh, save_points, num_points):
    tif_to_mesh(tif_directory, save_mesh)
    mesh_to_pc(save_mesh, num_points, save_points)


def label_tif_to_pc_directory(path: str , save_dir: str, save_name: str, num_points: int):
    acceptable_formats = [".tif", ".TIFF", ".TIF", ".png"]
    Path(save_dir).mkdir(exist_ok = True)
    if os.path.isdir(path):
        mesh_data = []
        points_data = []
        for fpath in tqdm(os.listdir(path)):     
            if any(fpath.endswith(f) for f in acceptable_formats):
                lbl_img = imread(os.path.join(path, fpath))
                for l in (set(np.unique(lbl_img)) - set([0])):
                    binary_image = lbl_img==l
                    print(binary_image.shape)
                    vertices, faces, normals, values = marching_cubes(binary_image)
                    mesh_obj = trimesh.Trimesh(
                        vertices=vertices, faces=faces, process=False
                    )
                    points = sample_points(data=mesh_obj, num=num_points).numpy()
                    mesh_data.append(mesh_obj) 
                    points_data.append(points)
        
        mesh_data = np.asarray(mesh_data)
        points_data = np.asarray(points_data)
        np.savez(os.path.join(save_dir, save_name), mesh=mesh_data, points=points_data)