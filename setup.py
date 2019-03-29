from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='python-fastrand',
    version='1.1',
    packages=find_packages(),
    author='Mukundan Senthil',
    author_email='mukundan314@gmail.com',
    description='Pure Python clone of fastrand',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='random pcg',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
    ],
    url='https://github.com/mukundan314/python-fastrand.git')
