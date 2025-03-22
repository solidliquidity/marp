from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="marp",
    version="0.1",
    description="A Python package to generate presentations with Marp",
    author="Luke Harding",
    url="https://github.com/solidliquidity/marp",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires = requirements
)