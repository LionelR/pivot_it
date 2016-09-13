from setuptools import setup, find_packages
from codecs import open as codecs_open

# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='pivot_it',
      version='0.1',
      url='https://github.com/LionelR/pivot_it',
      license='MIT',
      author='Lionel Roubeyrie',
      author_email='lionel dot roubeyrie at codinux dot fr',
      description='Command line utility to pivot CSV files',
      long_description=long_description,
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
      ],
      entry_points="""
          [console_scripts]
          pivot_it=pivot_it.pivot_it:run
          """
      )
