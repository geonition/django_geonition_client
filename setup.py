from setuptools import setup
from setuptools import find_packages

setup(
    name='geonition_client',
    version='1.0.0',
    author='Kristoffer Snabb',
    url='https://github.com/geonition/django_geonition_client',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['jsmin'],
)