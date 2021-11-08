from setuptools import setup

def readme():
  with open('README.md') as f:
    return f.read()

setup(name='verkefni',
    version='0.1.1',
    description='Efficient execution of trees of dependent tasks',
    long_description=readme(),
    keywords='',
    url='http://gitlab.com/OldIronHorse/verkefni',
    author='Simon Redding',
    author_email='s1m0n.r3dd1ng@gmail.com',
    license='GPL3',
    packages=[
        'verkefni',
        ],
    python_requires='>=3.10.0',
    install_requires=[
        'click',
        'redis',
        'pika'
        ],
    scripts=[
        'bin/worker-arithmetic',
        'bin/worker-lexical',
        'bin/tasker',
        'bin/monitor',
        'bin/configure',
        'bin/log',
        ],
    tests_require=[
        'pytest',
        'pytest-mock',
        'pytest-watch',
        ],
    include_package_data=True,
    zip_safe=False)
