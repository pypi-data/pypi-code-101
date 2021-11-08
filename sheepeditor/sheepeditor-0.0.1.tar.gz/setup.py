import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='sheepeditor',
	author='sleepntsheep',
	author_email='contact@papangkorn.com',
	description='Sheep Own text Editor',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/sleepntsheep/soe',
	package_dir={'': 'src'},
	packages=setuptools.find_packages(where='src'),
	python_requires='>=3.6',
	# extra_requires={
	entry_points={
		'console_scripts': [
			'soe=soe:main'
		],
	}
)
