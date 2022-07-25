# Install PyMesh:
This package used to rely on [PyMesh](https://pymesh.readthedocs.io/en/latest/index.html) which needs to be installed prior to installing cellshape-helper. To install, check out the source code from [GitHub](https://github.com/PyMesh/PyMesh):
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
