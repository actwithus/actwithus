from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='awucontacts',
    version=version,
    description="ActWithUs: Contacts app",
    long_description="""\
    What does this app do?
    ======================

    - Provides model and views for contact information.
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='ElevenCraft Inc.',
    author_email='actwithus@11craft.com',
    url='http://actwithus.com/',
    license='Apache 2.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django >= 1.2.3, < 1.3',
    ],
    entry_points="""
    """,
)
