from setuptools import setup, find_packages

setup(name="pyqt_server",
      version="0.0.1",
      description="server",
      author="ALeksei Barannikov",
      author_email="alekseibarannikov@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
