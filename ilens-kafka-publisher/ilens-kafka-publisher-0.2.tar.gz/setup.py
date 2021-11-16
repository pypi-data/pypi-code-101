from setuptools import setup

setup(
    name='ilens-kafka-publisher',
    version='0.2',
    packages=['ilens_kafka_publisher'],
    url='https://unifytwin.com',
    license='Restricted',
    author='Charan',
    author_email='charankumar@knowledgelens.com',
    description='Utility for Publishing messages to Kafka in iLens',
    install_requires=[
          "redis~=3.5.3",
          "kafka-python~=2.0.2"
      ],
)
