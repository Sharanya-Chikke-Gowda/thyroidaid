from setuptools import setup, find_packages

setup(
    name='thyroidaid',
    version='0.1',
    description='A package for analyzing and predicting thyroid health risk',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'seaborn',
        'matplotlib',
        'scikit-learn'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
)
