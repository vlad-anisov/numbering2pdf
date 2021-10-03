from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='numbering2pdf',
    version='1.0.0',
    packages=['numbering2pdf'],
    url='https://github.com/vlad-anisov/numbering2pdf',
    license='Apache 2.0',
    author='Vlad Anisov',
    author_email='anisoffgo@gmail.com',
    description='Adds numbering to pdf file',
    install_requires=[
        "reportlab == 3.5.2",
        "PyPDF4 == 1.27.0",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
