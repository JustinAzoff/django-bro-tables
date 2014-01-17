import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bro-tables',
    version='0.4',
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to manage bro tables',
    long_description=README,
    author='Justin Azoff`',
    author_email='jazoff@illinois.edu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires = [
        "djangorestframework",
        "djangorestframework-csv",
        "pytz",
    ],
)
