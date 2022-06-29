from os import path

from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

requirements = [
    "torch",
    "torchvision",
    "pyntcloud",
    "numpy",
    "matplotlib",
    "scikit-image",
    "pandas",
    "tqdm",
    "tifffile",
]


setup(
    name="cellshape-helper",
    version="0.0.14-rc0",
    description="3D shape analysis using deep learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    extras_require={
        "dev": [
            "black",
            "pytest-cov",
            "pytest",
            "gitpython",
            "coverage>=5.0.3",
            "bump2version",
            "pre-commit",
            "flake8",
        ]
    },
    python_requires=">=3.7",
    packages=find_packages(),
    package_dir={"cellshape_helper": "cellshape_helper"},
    include_package_data=True,
    project_urls={
        "Source Code": "https://github.com/Sentinal4D/cellshape-helper",
        "Bug Tracker": "https://github.com/Sentinal4D/cellshape-helper/issues",
    },
    author="Matt De Vries, Lucas Dent, Adam Tyson",
    author_email="mattdevries.ai@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    zip_safe=False,
)
