"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cherry',
    version='0.5.6',
    description='text classification without machine learning knowledge',
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://github.com/Windsooon/cherry',
    author='Windson Yang',
    author_email='wiwindson@outlook.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='data classify content filter',
    install_requires=[
        'numpy>=1.13.3',
        'scikit-learn>=0.21.3',
        'matplotlib>=2.2.2',
        ],
    packages=['cherry'],
    package_data={
        'cherry': [
            'data/harmful/trained.pkl', 'data/harmful/ve.pkl',
            'data/news/trained.pkl', 'data/news/ve.pkl']
    },
)
