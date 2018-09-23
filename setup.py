import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-rclone",
    version="0.0.1",
    author="Dragos Dascalita Haut",
    author_email="ddragosd@gmail.com",
    description="Rclone wrapper for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ddragosd/python-rclone",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2 License",
        "Operating System :: OS Independent",
    ],
)