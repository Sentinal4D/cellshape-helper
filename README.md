[![Project Status: Active – The project has reached a stable, usable
state and is being actively
developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![Python Version](https://img.shields.io/pypi/pyversions/cellshape-helper.svg)](https://pypi.org/project/cellshape-helper)
[![PyPI](https://img.shields.io/pypi/v/cellshape-helper.svg)](https://pypi.org/project/cellshape-helper)
[![Downloads](https://pepy.tech/badge/cellshape-helper)](https://pepy.tech/project/cellshape-helper)
[![Wheel](https://img.shields.io/pypi/wheel/cellshape-helper.svg)](https://pypi.org/project/cellshape-helper)
[![Development Status](https://img.shields.io/pypi/status/cellshape-helper.svg)](https://github.com/Sentinal4D/cellshape-helper)
[![Tests](https://img.shields.io/github/workflow/status/Sentinal4D/cellshape-helper/tests)](
    https://github.com/Sentinal4D/cellshape-helper/actions)
[![Coverage Status](https://coveralls.io/repos/github/Sentinal4D/cellshape-helper/badge.svg?branch=master)](https://coveralls.io/github/Sentinal4D/cellshape-helper?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


<img src="https://github.com/Sentinal4D/cellshape-helper/blob/main/img/cellshape_helper_logo.png" 
     alt="Cellshape logo by Matt De Vries">
___
Cellshape-helper provides the ability to convert 3D masks to point clouds.


## To install

### Step 2: Install cellshape-helper
```bash
pip install cellshape-helper
```

## Usage
```python
import cellshape_helper as helper


PATH_TO_TIF_FILES = "path/to/tif/files/"
PATH_TO_SAVE_MESH = "path/to/save/mesh/files/"
PATH_TO_SAVE_PC = "path/to/save/pointcloud/files/"
NUM_POINTS = 2048

helper.tif_to_pc_directory(PATH_TO_TIF_FILES, 
                           PATH_TO_SAVE_MESH, 
                           PATH_TO_SAVE_PC, 
                           NUM_POINTS)
```

## Parameters
- `PATH_TO_TIF_FILES`: str.  
The path to you binary masks of cells or nuclei.
- `PATH_TO_SAVE_MESH`: str.  
The path where you want to save the mesh objects to.
- `PATH_TO_SAVE_PC`: str.  
The path where you want to save your point clouds to.
- `NUM_POINTS`: str.  
The number of points to sample from the mesh object when creating a point cloud.

