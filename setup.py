# import package
from setuptools import setup, find_packages 
from typing import List

HYPER_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    
    if HYPER_E_DOT in requirements:
        requirements.remove(HYPER_E_DOT)
    
    return requirements

setup(
    name='ML_Projects',
    version='0.0.1',
    author='PhanAnhTri180803',
    author_email='triphan180803@gmail.com',
    description='Machine Learning Projects',
    packages= find_packages(),
    insatall_requires = get_requirements('requirements.txt'),
    
)