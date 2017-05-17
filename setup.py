from setuptools import find_packages, setup

setup(
    name='djangostar',
    version='0.0.0-1rc',
    url='https://github.com/linuxlewis/djangostar',
    author='Sam Bolgert',
    author_email='sbolgert@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.8',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)