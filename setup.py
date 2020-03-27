"""Setup for carmd package."""

import setuptools


with open('README.rst') as f:
    README = f.read()

setuptools.setup(
    author="Ira Horecka",
    author_email="ira89@icloud.com",
    name='python-carmd',
    license="MIT",
    description='A simple CarMD API wrapper',
    version='v0.2.0',
    long_description=README,
    long_description_content_type="text/x-rst",
    url='https://github.com/irahorecka/python-carmd',
    packages=['carmd'],
    python_requires=">=3.5",
    install_requires=['requests'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
