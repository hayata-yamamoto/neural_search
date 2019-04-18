from typing import IO

from setuptools import setup, find_packages

f: IO
with open("requirements.txt", 'r') as f:
    req = f.read().splitlines()


def main():
    setup(
        name='neural_search',
        version='0.0.1',
        author='hayata-yamamoto',
        install_requires=req,
        packages=find_packages(exclude=['neural_search/data'])
    )

if __name__ == '__main__':
    main()