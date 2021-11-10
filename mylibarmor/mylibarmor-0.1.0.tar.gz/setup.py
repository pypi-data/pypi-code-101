from setuptools import setup, find_packages

setup(
    name='mylibarmor',
    version='0.1.0',
    packages=['mylibarmor'],
    package_dir={'mylibarmor': 'dist'},
    data_files=[('pytransform_vax_xxxxxx', 'dist/share/pytransform_vax_000593/*')]
)
