from setuptools import setup

setup(name='mwsu_curriculum',
      version='0.1',
      description='Curriculum definitions and utilities for MWSU Computer Science',
      url='https://github.com/mwsu-csmp/curriculum',
      author='MWSU Computer Science Department',
      author_email='csmp@missouriwestern.edu',
      license='GPL',
      packages=['mwsu_curriculum'],  
      package_dir={'mwsu_curriculum': 'mwsu_curriculum'}, 
      package_data={'mwsu_curriculum': ['syllabi/*.xml']},
      zip_safe=False)
