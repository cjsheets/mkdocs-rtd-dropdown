from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name="rtd-dropdown",
    version=VERSION,
    url='https://github.com/cjsheets/mkdocs-rtd-dropdown',
    license='MIT',
    description='Clone of ReadTheDocs',
    author='Chad Sheets',
    author_email='chad@cjsheets.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'dropdown = rtd_dropdown',
        ]
    },
    zip_safe=False
)
