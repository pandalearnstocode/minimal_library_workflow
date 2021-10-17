from setuptools import find_packages, setup

from minipackage import __version__

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    author="Aritra Biswas",
    author_email="pandalearnstocode@gmail.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    description="Python Library template for Data Science project.",
    entry_points={"console_scripts": ["source=minipackage.cli:main",],},
    install_requires=requirements,
    include_package_data=True,
    keywords="minipackage",
    name="minipackage",
    packages=find_packages(include=["minipackage", "minipackage.*"]),
    test_suite="tests",
    tests_require=requirements,
    version=__version__,
    zip_safe=False,
)
