from setuptools import setup

setup(name='nixdeps',
      version='0.0.1',
      description='A setuptools entrypoint to store dependencies on Nix packages at build-time',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
      ],
      url='https://github.com/catern/rsyscall',
      author='catern',
      author_email='sbaugh@catern.com',
      license='MIT',
      packages=['nixdeps'],
      entry_points={
          'distutils.setup_keywords': [
              "nixdeps = nixdeps.setuptools:nixdeps",
          ],
      },
)
