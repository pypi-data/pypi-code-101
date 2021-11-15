from setuptools import setup, find_packages

setup(name="lisecky_messenger_prod",
      version="0.0.2",
      description="mess_server_proj",
      author="Ivan Ivanov",
      author_email="iv.iv@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
