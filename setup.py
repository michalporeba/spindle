from setuptools import setup, find_packages 

VERSION = '0.0.1'
DESCRIPTION = 'A pythonic take on Historing Modelling concept'

setup(
    name='spindle',
    version=VERSION,
    author='Michał Poręba',
    author_email='michalporeba@gmail.com',
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    packages=find_packages(exclude=['tests*']),
    install_requires=[],
    keywords=['python', 'data', 'historical modelling'],
    classifiers=[
        'Programming Language :: Python :: 3'
    ]
)