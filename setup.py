import setuptools

extras = {
    "dev": ["pytest==6.2.4"]
}

setuptools.setup(
    name="ernie",
    version="0.0.1",
    description="A flask app for serving BERT",
    packages=setuptools.find_packages(),
    extras_require=extras,
    python_requires='>=3.8',
    install_requires=[
        'Flask',
        'Flask-WTF',
        'transformers[torch]'
    ]
)
