from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    "matplotlib >= 3.2.2",
    "numpy >= 1.18.5",
    "opencv-python>=4.1.1",
    "pandas>=1.1.4",
    "seaborn>=0.11.0"
    ]

setup(
    name="yolov5",
    version="0.0",
    author="",
    author_email="",
    description="",

    # Project website
    url="",

    # setuptools.find_packages can find all the packages in the directory
    packages=find_packages(),

    install_requires=INSTALL_REQUIRES
)
