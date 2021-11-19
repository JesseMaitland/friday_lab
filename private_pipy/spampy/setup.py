from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name='spam',
    version=VERSION,
    author='spammer',
    discription='A cli tool to do some pretty rad stuff!',
    include_package_data=True,
    packages=find_packages(exclude=('tests*', 'venv')),
    entry_points={'console_scripts': ['spam = spam.__main__:main']},
    python_requires='>=3'
)
