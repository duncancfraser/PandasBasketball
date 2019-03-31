from setuptools import setup, find_packages


setup(
    name='PandasBasketball',

    version='0.1',

    description='PandasBasketball is a small module intended to scrape data from basketball reference.',

    url='https://github.com/alfremedpal/PandasBasketball',

    author='Alfredo Medina',
    author_email='info@amedpal.com',

    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.7.1',
        'pandas==0.24.2',
        'requests==2.21.0'
    ]
)
