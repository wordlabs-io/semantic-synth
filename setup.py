from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = '0.0.1' 
DESCRIPTION = 'Synthetic dataset generator for testing semantic search quality'
LONG_DESCRIPTION = long_description

# Setting up
setup(
        name="semantic_synth", 
        version=VERSION,
        author="Tanishk Kithannae",
        author_email="tanishk.kithannae@wordlabs.io",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type = 'text/markdown',
        url = "https://github.com/wordlabs-io/context_aware_chunker",
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        install_requires=[
            'transformers',
            'pysbd',
            'yake',
            'pandas'
        ], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'rag'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)