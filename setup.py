from setuptools import setup, find_packages

VERSION = '0.0.9'

with open("requirements.txt") as data:
    install_requires = [
        line for line in data.read().split("\n")
            if line and not line.startswith("#")
    ]

setup(
    name="mkdocs-rtd-dropdown",
    version=VERSION,
    url='https://github.com/cjsheets/mkdocs-rtd-dropdown',
    license='MIT',
    description='Clone of ReadTheDocs',
    author='Chad Sheets',
    author_email='chad@sheets.ch',
    packages=find_packages(),
    include_package_data=True,
    install_requires = install_requires,
    entry_points={
        'mkdocs.themes': [
            'rtd-dropdown = rtd_dropdown',
        ]
    },
    zip_safe=False
)
