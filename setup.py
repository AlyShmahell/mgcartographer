import os
from distutils.core import setup, Extension

setup(
    name="mgcartographer",
    packages=["mgcartographer"],
    install_requires=['pymongo[srv]'],
    version='0.1.0',
    description='Pushes a JSON file based database to MongoDB Atlas.',
    author='Aly Shmahell',
	author_email='aly.shmahell@gmail.com',
    license='Copyrights 2019 Aly Shmahell',
    entry_points={
    'console_scripts': ['mgcartographer=mgcartographer.executer:main']
        }
    )

