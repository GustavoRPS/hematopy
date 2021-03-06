
# -*- encoding: utf-8 -*-
import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='hematopy',
    description='Python and Blood',
    version='0.0.2.dev1',
    author='Gustavo RPS @ ArgoCrew/ArgoPy',
    author_email='gustavorps+hematopy@argocrew.io',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    setup_requires=['pytest-runner'],
    install_requires=[
        'CairoSVG==2.1.3',
        'click==6.7',
        'sanic==0.7.0',
        'lxml==4.2.1',
        'python-magic==0.4.15'
    ],
    tests_require = [
        'pytest-console-scripts==0.1.5',
    ],
    # package_dir={'':'hematopy'},
    entry_points = {
        'console_scripts': [
            'hematopy=hematopy.cli:main'
        ],
    },
    license='BSD-3',
    keywords='blood banner utility',
    project_urls={
        'Issues': 'https://github.com/ArgoCrew/hematopy/issues',
        'Source Code': 'https://github.com/ArgoCrew/hematopy',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Intended Audience :: Healthcare Industry',
    ],
)
