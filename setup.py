from setuptools import setup, find_packages

setup(
    name='cryptofusepy',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Silenttttttt',
    author_email='cryptofuse.net@gmail.com',
    description='Python library for interacting with the CryptoFuse API',
    keywords='cryptofuse cryptocurrency cryptoswap swap crypto',
    entry_points={
        'console_scripts': [
            'cryptofusepy = cryptofusepy.client:CryptoFuseClient',
        ],
    }
)
