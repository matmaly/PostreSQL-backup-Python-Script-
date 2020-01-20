from setuptools import find_packages, setup

with open('README.md','r') as f:
	long_description = f.read()

setup(
	name='pgbackup'
	version='0.1.0'
	author='Mateusz Maly'
	author_email='mateuszfmaly@gmail.com'
	description='Utulity for backing up PostreSQL dbs'
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/matmaly/PostreSQL-backup-Python-Script-.git'
	packages=find_packages('src')
)
