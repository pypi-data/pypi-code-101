from setuptools import setup, find_packages

setup(name="serverapp",
      version="0.1",
      description="serverapp",
      author="Korepanov A",
      author_email="al1working@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
