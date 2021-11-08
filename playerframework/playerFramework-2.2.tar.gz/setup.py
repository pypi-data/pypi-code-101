import setuptools
reqs = ['utils-s']
version = '2.2'

setuptools.setup(
    name='playerFramework',
    version=version,
    description="A Bridge between Swift based players and Python",
    packages=setuptools.find_packages(),
    install_requires=reqs
)