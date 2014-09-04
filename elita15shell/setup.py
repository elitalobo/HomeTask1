#!/usr/bin/env python2

from setuptools import find_packages, setup


setup(
    name='elitashell',
    version="0.3.2",
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


