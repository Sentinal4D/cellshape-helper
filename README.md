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
### Step 1: Install PyMesh:
This package relies on [PyMesh](https://pymesh.readthedocs.io/en/latest/index.html) which needs to be installed first. To install, check out the source code from [GitHub](https://github.com/PyMesh/PyMesh):
- Clone the PyMesh repo into a directory of your choice:
```bash
git clone https://github.com/PyMesh/PyMesh.git
cd PyMesh
git submodule update --init
export PYMESH_PATH=`pwd`
```
- On Linux, the system dependencies can be installed with apt-get:
 ```bash
 apt-get install \
    libeigen3-dev \
    libgmp-dev \
    libgmpxx4ldbl \
    libmpfr-dev \
    libboost-dev \
    libboost-thread-dev \
    libtbb-dev \
    python3-dev
```

 - On MacOS, the system dependencies can be installed with MacPorts:
```bash
port install
    python36 \
    eigen3 \
    gmp \
    mpfr \
    tbb \
    boost
```

- Python dependencies such as NumPy and SciPy can be installed using pip:
```bash
pip install -r $PYMESH_PATH/python/requirements.txt
```

- Build PyMesh with setuptools:
```bash
./setup.py build
```

- Install PyMesh:
```bash
./setup.py install  # May require root privilege
```

- Alternatively, one can install PyMesh locally:
```bash
./setup.py install --user
```
- Check if PyMesh was installed correctly:
```bash
python -c "import pymesh; pymesh.test()"
```

- Please refer to the PyMesh installation [guide](https://pymesh.readthedocs.io/en/latest/installation.html) if there are any issues.

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


## For developers
* Fork the repository
* Clone your fork
```bash
git clone https://github.com/USERNAME/cellshape-helper 
```
* Install an editable version (`-e`) with the development requirements (`dev`)
```bash
cd cellshape-voxel
pip install -e .[dev] 
```
* To install pre-commit hooks to ensure formatting is correct:
```bash
pre-commit install
```

* To release a new version:

Firstly, update the version with bump2version (`bump2version patch`, 
`bump2version minor` or `bump2version major`). This will increment the 
package version (to a release candidate - e.g. `0.0.1rc0`) and tag the 
commit. Push this tag to GitHub to run the deployment workflow:

```bash
git push --follow-tags
```

Once the release candidate has been tested, the release version can be created with:

```bash
bump2version release
```
