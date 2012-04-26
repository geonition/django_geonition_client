from setuptools import setup
from setuptools import find_packages

setup(
    name='geonition_client',
    version='4.0.0',
    author='Kristoffer Snabb',
    url='https://github.com/geonition/django_geonition_client',
    packages=find_packages(),
    include_package_data=True,
    package_data = {
        "geonition_client": [
            "templates/*.txt",
            "templates/javascript/*.js",
            "templates/test/*.html",
            "static/softgis_ui_dojo.js"
        ],
    },
    zip_safe=False,
    install_requires=['django', 'jsmin'],
)
