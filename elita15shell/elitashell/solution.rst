================
Dummy Project v1
================

**TASK**

Write a shell script that would install Myshell Project. Few changes had to be made in setup.py file to install required dependencies.

**Code**

Code for setup.py file

::
   
    #!/usr/bin/env python2

    from setuptools import find_packages, setup


    setup(
       name='elitashell',
       version="0.3.4",
       description="elita's Shell",
       long_description="Dummy Project",
       platforms=["Linux"],
       author="Elita",
       author_email="loboelita@gmail.com",
       url="https://github.com/elitalobo/HomeTask1",
       license="MIT",
       install_requires=["requests", "cmd2"],
       packages=find_packages(),
       package_data = {
             '': [ 'elitashell/*.rst'],
       },
       entry_points={
           'console_scripts': [
               'eshell = elitashell:main',
             ]
          },
       )

**link**
`link <https://github.com/elitalobo/HomeTask1>`_

**link to package**

`link <https://testpypi.python.org/pypi/elitashell>`_
