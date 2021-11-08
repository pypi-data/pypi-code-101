from setuptools import setup


INSTALL_REQUIRES = [
    "pytest==6.0.1",
    "allure-pytest==2.8.18",
    "requests==2.23.0",
    "PyYAML>=5.3.1",
    "xlwt==1.3.0",
    "xlrd==1.2.0",
    "mysql-connector-python>=8.0.20",
    "jmespath==0.10.0",
    "selenium",
    "Faker",
    "Pillow",
    "pypng==0.0.20",
    "pytest-xdist==2.1.0",
    "Flask",
    "Jinja2",
    "flask_migrate",
    "flask_cors",
    "Flask-SQLAlchemy",
    "flask_migrate",
    "flask_restful",
    "fnv",
    "colorama",
    "importlib_metadata>=4.5.0"
]


def main():
    setup(
        use_scm_version={"write_to": "src/_pyland/_version.py"},
        setup_requires=["setuptools-scm", "setuptools>=40.0"],
        package_dir={"": "src"},
        # fmt: on
        install_requires=INSTALL_REQUIRES,
    )


if __name__ == "__main__":
    main()

