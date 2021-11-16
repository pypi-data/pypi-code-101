from setuptools import setup

setup(name='revcorml',
      version='0.2',
      description='tools to probe machine learning classifiers with noise, bubbles and reverse correlation',
      url = 'https://github.com/EtienneTho/revcorml',
      download_url = 'https://github.com/EtienneTho/revcorml/blob/main/dist/revcorml-0.2.tar.gz',
      author='Etienne Thoret, Thomas Andrillon, Damien Léger, Daniel Pressnitzer',
      author_email='etienne.thoret@univ-amu.fr',
      license='MIT',
      packages=['revcorml'],
      install_requires=['numpy','sklearn','scipy'],
      zip_safe=False)