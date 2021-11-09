import setuptools
reqs = ['utils-s', 'pydub']
version = '2.4'

setuptools.setup(
    name='playerFramework',
    version=version,
    description="A Bridge between Swift based players and Python",
    packages=setuptools.find_packages(),
    install_requires=reqs
)