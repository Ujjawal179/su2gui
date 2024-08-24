from setuptools import setup, find_packages

setup(
    name='su2gui',
    version='1.0.0',
    packages=find_packages(),
    description = 'SU2GUI is a Python-based graphical user interface designed to simplify the setup, execution, and analysis of simulations using the SU2 software suite.',
    package_data={
        'su2gui': [
            'user/*.json',
            'user/*.su2',
            'user/*.csv',
            'img/*',
            'icons/*',
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
            'SU2_GUI=su2gui.su2gui:main',
        ],
    },
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license='GPL-3.0',
)
