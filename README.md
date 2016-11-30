## materials.sh

materials.sh is an initiative to build the world's most comprehensive collection of software for materials science.

The intent is to improve the accessibility of these tools to all researchers by enabling one-line installations of highly useful software packages without the need for compilation, etc. All packages are hosted on the `matsci` channel on Anaconda Cloud.

## Getting started

The instructions are written for Python 3. For Windows, this is the only supported platform. For other OSes, the instructions below can be trivially modified for Python 2.7.

### Step 1: Preparing your system

#### Windows

1. Download Microsoft Visual Studio 2015 (the free Community Edition) is fine.
2. Install Visual Studio 2015, but *make sure that you select More Options -> Programming Languages -> Visual C++ during the installation process*. By default, Visual Studio does not install Visual C++, which is needed.

#### Mac OSX

1. Download and install Xcode. Afterwards, install the XCode command line tools by typing the following in a terminal:

        xcode-select --install

#### Linux

1. Usually no preparation is needed as most of the standard compilers should already be available.

### Step 2: Install conda

Download and install the version of conda for your operating system from http://conda.pydata.org/miniconda.html.

For Windows, **make sure it is the Miniconda3 installer**, and simply double-click the exe file.

For Mac, run:

    curl -o Miniconda3-latest-MacOSX-x86_64.sh https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
    bash Miniconda3-latest-MacOSX-x86_64.sh -b

For Linux, run:

    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda3-latest-Linux-x86_64.sh;
    bash Miniconda3-latest-Linux-x86_64.sh -b

Note that you may need to create a new terminal after this step in order for the environmental variables added by conda to be loaded.

### Step 2b: (Optional) Create a conda environment

If you are working with many python packages, it is generally recommended you create a separate environment for each of your packages. For example:

    conda create --name my_env python
    source activate my_env  # OSX or Linux
    activate my_env  # Windows

### Step 3: Add the matsci channel

You can now install materials science software packages in materials.sh via the following command:

    conda install --channel matsci <package>

where `--channel matsci` indicates to use the matsci channel.

If you believe you will be using the channel frequently, you can add it to the list of channels in your environment with the following command:

    conda config --add channels matsci

## Available packages

The packages available are constantly updated. You can check out the currently available packages on the [matsci channel on Anaconda Cloud](https://anaconda.org/matsci), or simply look at the conda-skeletons folder in this repo. This initiative arose from the desire to make [Python Materials Genomics](http://www.pymatgen.org) and its associated dependencies a lot easier to install for users on all platforms. Please note that not all packages are available for all OSes.

## Contributing

Contributions are always welcome. Feel free to fork this repo and add your proposed conda software recipes to the conda-skeletons folder. This repo is continuously integrated via TravisCI and Appveyor to build all Linux, OSX and Windows versions, where compatible.

## Authors

This initiative is started by the [Materials Virtual Lab](http://materialsvirtuallab.org).