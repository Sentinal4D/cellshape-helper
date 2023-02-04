from .vendor.pytorch_geometric_files import read_off, sample_points
from pyntcloud import PyntCloud
import pandas as pd
from tifffile import imread
import trimesh
from skimage.measure import marching_cubes, regionprops
from skimage.segmentation import clear_border
from tqdm import tqdm
from .util import create_dir_if_not_exist
from pathlib import Path
import os
import numpy as np
import concurrent

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


def label_tif_to_pc_directory(path: str , save_dir: str, num_points: int):
    acceptable_formats = [".tif", ".TIFF", ".TIF", ".png"]
    mesh_save_dir = os.path.join(save_dir, 'mesh')
    point_cloud_save_dir = os.path.join(save_dir, 'point_cloud')
    Path(save_dir).mkdir(exist_ok = True)
    Path(mesh_save_dir).mkdir(exist_ok = True)
    Path(point_cloud_save_dir).mkdir(exist_ok = True)
    if os.path.isdir(path):
        for fpath in tqdm(os.listdir(path)):     
            if any(fpath.endswith(f) for f in acceptable_formats):
                read_path = os.path.join(path, fpath)
                lbl_img = imread(read_path)
                clear_lbl_img = clear_border(lbl_img)
                name = os.path.basename(os.path.splitext(read_path)[0])
                nthreads = os.cpu_count() - 1
                properties = regionprops(clear_lbl_img)
                bbox = [prop.bbox for prop in properties]
                with concurrent.futures.ThreadPoolExecutor(max_workers = nthreads) as executor:
                    futures = []
                    for i in range(len(bbox)):
                            current_box = bbox[i]    
                            futures.append(executor.submit(get_current_label_binary, clear_lbl_img, current_box, i))
                    for future in concurrent.futures.as_completed(futures):
                            binary_image, index = future.result()    
                            vertices, faces, normals, values = marching_cubes(binary_image)
                            mesh_obj = trimesh.Trimesh(
                                vertices=vertices, faces=faces, process=False
                            )
                            mesh_file = name + str(index) 
                            save_mesh_file = os.path.join(mesh_save_dir, mesh_file) + ".off"
                            save_point_cloud_file = os.path.join(point_cloud_save_dir, mesh_file) + ".ply"
                            mesh_obj.export(save_mesh_file) 
                            data = read_off(os.path.join(mesh_save_dir, save_mesh_file))
                            points = sample_points(data=data, num=num_points).numpy()
                            cloud = PyntCloud(pd.DataFrame(data=points, columns=["x", "y", "z"]))
                            cloud.to_file(save_point_cloud_file)
                    
def get_current_label_binary(clear_lbl_img, current_box, index):
       
       
                crop_z_min = current_box[0]
                crop_y_min = current_box[1]
                crop_x_min = current_box[2]
                crop_z_max = current_box[3]
                crop_y_max = current_box[4]
                crop_x_max = current_box[5]
                region = (
                    slice(int(crop_z_min), int(crop_z_max)),
                    slice(
                        int(crop_y_min) , int(crop_y_max) 
                    ),
                    slice(
                        int(crop_x_min) , int(crop_x_max)
                    ),
                )
                binary_image = clear_lbl_img[region] > 0

                return binary_image , index             