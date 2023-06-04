from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''

    This function would return the list of requirements to the get_requirements functions of the setup fuction.

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

        #upon executing the above line a \n would be added after each reading. so to remove that we would use.

        requirements = [req.replace('\n'," ") for req in requirements]

        #one issue with the requirements file is the presence of -e . this invokes the setup.py file so to remove this from the requirements.....
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements



setup(name = 'mlProject',
      version = '0.0.1',
      author = 'Adarsh',
      author_email = 'adarshkumar18122002@gmail.com',
      packages = find_packages(),
      install_requires = get_requirements('requirements.txt'))