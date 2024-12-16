from setuptools import setup, find_packages

setup(
    name="Orbital_Visualizator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["skyfield.api", "matplotlib.pyplot", "numpy", "mpl_toolkits.mplot3d"],
    entry_points={
        "console_scripts": [
            "Orbite_Visualizator=Orbite_Visualizator.Orbite_Visualizator_App:main",
        ]
    },
    author="Baptiste LEBON",
    description="Visualize in a 3D space an orbit from a TLE or direct Keplerian parameters given by user.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ArpaxSpaceSystems/Orbital_Visualizator.git",
    classifiers=[
        "Programming Language :: Python :: 3.x",
    ],
    python_requires='>=3.6',
)