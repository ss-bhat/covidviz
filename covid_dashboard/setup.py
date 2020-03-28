from setuptools import setup, find_packages
from os import path

# Path of the extension
here = path.abspath(path.dirname(__file__))


# Get description from Readme.md
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='covid19viz',  # Required
    version='1.0',
    description="""
                Dashboard for corono virus outbreak. Also contains some basic anasysis of the outbreak
                """,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Swaroop',
    author_email='',
    license="MIT",
    classifiers=[  # Optional
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    keywords='Data extractor covid19',
    packages=find_packages(
        exclude=['contrib', 'docs', 'tests']
    ),
    python_requires='>=3.6',

    # All install packages should go on requirements.txt file
    install_requires=[
    ],
    extras_require={
    },
    package_data={
    },
    data_files=[
    ],

    # Entry Points
    entry_points={
    }
)
