from setuptools import setup

setup(name='Fitbit.Food',
      version='0.1',
      description='Imports data from Kolonial to add to custom foods on Fitbit',
      author='Tomas Johnsen',
      packages=['fitbit', 'kolonial'],
      install_requires=[
            'requests',
      ],
      zip_safe=False)
