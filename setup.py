from setuptools import setup, find_packages

setup(
    name='strong_password',
    version='0.1.0',
    url='https://github.com/estevaofon/strong-password-generator',
    author='Estevao',
    author_email='estevaopfon@gmail.com',
    description='Projeto para criar senhas fortes',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'strong_password = strong_password:main',
        ],
    },
)