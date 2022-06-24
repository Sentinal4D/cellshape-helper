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

___
Cellshape-helper is an easy-to-use tool to analyse the shapes of cells using deep learning and, 
in particular, 
3D convolutional neural networks. The tool provides the ability to convert masks to point clouds.


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

```

## Parameters




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
