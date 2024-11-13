from setuptools import setup, find_packages

setup(
    packages=find_packages(where=["uscodekit"]),
    options={"bdist_wheel": {"universal": False}},
)
