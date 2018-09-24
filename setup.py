"""
Package setup
"""
import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="python-rclone",
    version="0.0.2",
    author="Dragos Dascalita Haut",
    author_email="ddragosd@gmail.com",
    description="Rclone wrapper for python",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/ddragosd/python-rclone",
    py_modules=["rclone"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License"
    ],
)
