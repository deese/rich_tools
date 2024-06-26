""" Setuptools configuration for the project. """

import os.path

from setuptools import find_packages, setup


def source_root_dir():
    """Return the path to the root of the source distribution."""
    return os.path.abspath(os.path.dirname(__file__))


def read_long_description():
    """Read from the README file in root of source directory."""
    readme = os.path.join(source_root_dir(), "README.md")
    with open(readme, encoding="utf-8") as fin:
        return fin.read()

setup(
    name="rich-tools",
    version = "0.6.0",
    description="A python package with helpful tools when working with the rich python library.",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/deese/rich_tools",
    author="Javier DeeSe",
    author_email="deese2k@gmail.com",
    classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Typing :: Typed",
    ], 
    packages=find_packages(),
    setup_requires=["setuptools_scm"],
    python_requires=">=3.8",
    install_requires=[
        'rich',
        "pandas"
    ]
)
