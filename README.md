## materials.sh

[materials.sh](http://materials.sh) is a community initiative to build the world's most comprehensive collection of software for materials science.

The intent is to improve the accessibility of these tools to all researchers by enabling one-line installations of highly useful software packages without the need for compilation, etc. All packages are hosted on the [matsci channel on Anaconda Cloud](https://anaconda.org/matsci).

## Available packages

The packages available are constantly updated. You can check out the currently available packages on the [matsci channel on Anaconda Cloud](https://anaconda.org/matsci), or simply look at the conda-skeletons folder in this repo. As of writing, the packages available are:

* bader
* boltztrap
* custodian
* enumlib
* latexcodec
* monty
* palettable
* pybtex
* pydispatcher
* pymatgen
* pymatgen-diffusion
* seekpath
* spglib
* tabulate

This effort initially arose from the desire to make [Python Materials Genomics](http://www.pymatgen.org) and its associated dependencies a lot easier to install for users on all platforms. So these will always be available. Please note that not all packages are available for all OSes.

## Getting started

The instructions are written for Python 3. For Windows, this is the only supported platform. For other OSes, the instructions below can be trivially modified for Python 2.7.

### Step 1: Install conda

Download and install the version of conda for your operating system from http://conda.pydata.org/miniconda.html.

For Windows, **make sure it is the Miniconda3 installer**, and simply double-click the exe file.

For Mac, run:

```bash
curl -o Miniconda3-latest-MacOSX-x86_64.sh https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh -b
```

For Linux, run:

```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda3-latest-Linux-x86_64.sh;
bash Miniconda3-latest-Linux-x86_64.sh -b
```

Note that you may need to create a new terminal after this step in order for the environmental variables added by conda to be loaded.

### Step 1b: (Optional) Create a conda environment

If you are working with many python packages, it is generally recommended you create a separate environment for each of your packages. For example:

```bash
conda create --name my_env python
source activate my_env  # OSX or Linux
activate my_env  # Windows
```

### Step 2: Add the matsci channel

You can now install materials science software packages in materials.sh via the following command:

```bash
conda install --channel matsci <package>
```

where `--channel matsci` indicates to use the matsci channel.

If you believe you will be using the channel frequently, you can add it to the list of channels in your environment with the following command:

```bash
conda config --add channels matsci
```

## Contributing

Contributions are always welcome. Feel free to fork this repo and add your proposed conda software recipes to the conda-skeletons folder. This repo is continuously integrated via TravisCI and Appveyor to build all Linux, OSX and Windows versions, where compatible.

## Authors

This initiative is started by the [Materials Virtual Lab](http://materialsvirtuallab.org).