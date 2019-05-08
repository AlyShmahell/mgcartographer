import os
import sys
from setuptools import setup, Extension

with open('LICENSE', 'r') as legal:
	license = " ".join(line.strip() for line in legal)

setup(
        name             = "mgcartographer",
        packages         = ["mgcartographer"],
        install_requires = ['pymongo[srv]'],
        version          = '0.1.0',
        description      = 'Pushes a JSON file based database to MongoDB Atlas.',
        author           = 'Aly Shmahell',
        author_email     = 'aly.shmahell@gmail.com',
        license          = license,
        entry_points     = {
                                'console_scripts': ['mgcartographer=mgcartographer.executer:main']
                           }
    )

