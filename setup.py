import setuptools

setuptools.setup(
    name='ai-sdk-sbarbosa115',
    version='1.0.3',
    packages=setuptools.find_packages(),
    url='https://github.com/sbarbosa115/ai-sdk.git',
    license='',
    author='Sergio Barbosa ',
    author_email='sbarbosa115@gmail.com',
    description='IA package.',
    package_dir={'ia_sdk': 'src'},
    install_requires=[
        'cerberus', 'pycountry', 'boto3', 'python-dotenv'
    ],
    python_requires='>=3.8',
)
