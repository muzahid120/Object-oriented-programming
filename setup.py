from setuptools import setup,find_packages
from typing import List
hypen='-e .'
def get_requirements(file_path:str)->List:


    requirements=[]



    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','')for req in requirements ]
        if hypen in requirements:
            requirements.remove()

    return requirements






setup(author='Skmuzahid',
version='0.0.0',
author_email='muzahidsk771@gmail.com',
packages=find_packages(),
requires=get_requirements('requirements.txt')



)