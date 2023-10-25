from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    """
    This function will return a list of requirements
    """
    # requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.read().strip()

    return [
        line.strip()
        for line in requirements.split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ] 


setup(
    name='data-pipeline',
    version='0.0.1',
    author='Sumeet',
    author_email='sachdevsumeet1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)