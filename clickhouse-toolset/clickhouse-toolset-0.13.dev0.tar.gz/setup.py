from setuptools import setup, Extension

NAME = 'clickhouse-toolset'
VERSION = '0.13.dev0'

try:
    from conf import *
    chquery = Extension(
        'chtoolset._query',
        sources=['src/query.cpp'] + musl_sources,
        depends=['src/ClickHouseQuery.h'],
        include_dirs=include_dirs,
        extra_compile_args=['-std=gnu++2a'],
        library_dirs=library_dirs,
        libraries=libraries
    )
    setup(
        name=NAME,
        version=VERSION,
        url='https://gitlab.com/tinybird/clickhouse-toolset',
        author='Tinybird.co',
        author_email='support@tinybird.co',
        packages=['chtoolset'],
        package_dir={'': 'src'},
        python_requires='>=3.6, <3.11',
        install_requires=[],
        extras_require={
            'test': requirements_from_file('requirements-test.txt')
        },
        cmdclass={
            'clickhouse_parsers': ClickHouseBuildExt,
            'libc_libs': LibcBuildExt,
            'build_ext': CustomBuildWithClang,
        },
        ext_modules=[chquery]
    )

except:
    setup(
        name=NAME,
        version=VERSION,
        url='https://gitlab.com/tinybird/clickhouse-toolset',
        author='Tinybird.co',
        author_email='support@tinybird.co',
        packages=['chtoolset'],
        package_dir={'': 'src'},
        python_requires='>=3.6, <3.11',
        install_requires=[],
    )
