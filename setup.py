import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name = 'namari',
    packages = ["namari"],
    version = '1.0.1',
    license='MIT',
    description = 'Many-to-one keys-value pair relationship Python object manager.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Rodney Maniego Jr.',
    author_email = 'rod.maniego23@gmail.com',
    url = 'https://github.com/rmaniego/namari',
    download_url = 'https://github.com/rmaniego/namari/archive/v1.0.tar.gz',
    keywords = ['Dictionary', 'JSON', 'many-to-many', 'keys-value', 'multiple relationship'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6'
)