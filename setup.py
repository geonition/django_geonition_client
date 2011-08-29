import os
from distutils.core import setup


def fullsplit(path, result=None):

    if result is None:
        result = []
    
    head, tail = os.path.split(path)
    
    if head == "":
        return [tail] + result
    
    if head == path:
        return result
    
    return fullsplit(head, [tail] + result)


package_dir = "geonition_client"


packages = []
for dirpath, dirnames, filenames in os.walk(package_dir):
    # ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith("."):
            del dirnames[i]
    if "__init__.py" in filenames:
        packages.append(".".join(fullsplit(dirpath)))

template_patterns = [
    'templates/*.txt',
    'templates/javascript/*.js',
    'templates/test/*.html'
]

package_data = dict(
    (package_name, template_patterns)
    for package_name in packages
)

setup(
    name='geonition_client',
    version='1.0.0',
    author='Kristoffer Snabb',
    url='https://github.com/geonition/django_geonition_client',
    packages=['geonition_client'],
    package_data=package_data,
    install_requires=['jsmin'],
)