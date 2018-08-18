from os import path

from setuptools import setup

# Version
with open(path.join(path.dirname(__file__), 'ar_cmudict', 'VERSION')) as version_file:
    VERSION = version_file.read().strip()
# Long Description
with open(path.join(path.dirname(__file__), 'README.md')) as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name='ar_cmudict',
    version=VERSION,
    description='A python wrapper package for Arabic CMU Pronouncing Dictionary data files.',
    long_description=LONG_DESCRIPTION,
    author='Youssef Sherif',
    author_email='sharief@aucegypt.edu',
    url='https://github.com/youssefsharief/arabic-python-cmudict.git',
    include_package_data=True,
    zip_safe=False,
    license='GPL-3.0',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6'
    )
)
