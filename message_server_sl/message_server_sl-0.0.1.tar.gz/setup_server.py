from setuptools import setup, find_packages

setup(name="message_server_sl",
      version="0.0.1",
      description="message_server_sl",
      author="Sergey Lomakin",
      author_email="sergeylomakin-it@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
