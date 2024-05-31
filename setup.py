from setuptools import setup, find_packages

setup(
    name='su2guitest',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        'su2gui': [
            'user/*.json',
            'user/*.cfg',
            'user/*.su2',
            'user/*.csv',
            'user/*.dat',
            'user/**/*.vtu',
            'user/**/*.vtm',
            'img/*',
            'icons/*',
            # Add other patterns as needed
        ],
    },

    include_package_data=True,
    install_requires=[
        "jsonschema>=4.19.1",
        "pandas>=2.1.0",
        "trame>=3.2.0",
        "trame-client>=2.12.0",
        "trame-components>=2.2.0",
        "trame-markdown>=3.0.0",
        "trame-matplotlib>=2.0.0",
        "trame-server>=2.12.0",
        "trame-vtk>=2.5.0",
        "trame-vuetify>=2.3.0",
        "vtk>=9.2.0",
    ],
    entry_points={
        'console_scripts': [
            'su2gui=su2gui.su2gui:main',
        ],
    },
)
