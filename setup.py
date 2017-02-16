import os
from setuptools import find_packages, setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-uwsgi',
    version='1.0.0',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    license='',
    description='',
    long_description='',
    url='',
    author_email='pkucmus@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.12',
    ],
)
