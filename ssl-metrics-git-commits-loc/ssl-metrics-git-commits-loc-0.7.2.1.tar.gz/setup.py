from setuptools import setup

from ssl_metrics_git_commits_loc import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ssl-metrics-git-commits-loc",
    packages=["ssl_metrics_git_commits_loc"],
    version=version.version(),
    description="SSL Metrics - Git History (LOC/KLOC) Analysis",
    author="Software and Systems Laboratory - Loyola University Chicago",
    author_email="ssl-metrics@ssl.luc.edu",
    license="Apache License 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ssl.cs.luc.edu/projects/metricsDashboard",
    project_urls={
        "Bug Tracker": "https://github.com/SoftwareSystemsLaboratory/ssl-metrics-git-commits-loc/issues",
        "GitHub Repository": "https://github.com/SoftwareSystemsLaboratory/ssl-metrics-git-commits-loc",
    },
    keywords=[
        "git",
        "github",
        "software engineering",
        "metrics",
        "software systems laboratory",
        "ssl",
        "loyola",
        "loyola university chicago",
        "luc",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.9",
    install_requires=[
        "matplotlib>=3.4.3",
        "numpy>=1.21.2",
        "pandas>=1.3.3",
        "progress>=1.6",
        "python-dateutil>=2.8.2",
        "scikit-learn>=1.0.1",
    ],
    entry_points={
        "console_scripts": [
            "ssl-metrics-git-commits-loc-extract = ssl_metrics_git_commits_loc.main:main",
            "ssl-metrics-git-commits-loc-graph = ssl_metrics_git_commits_loc.create_graph:main",
        ]
    },
)
