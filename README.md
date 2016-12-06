## materials.sh

[materials.sh](http://materials.sh) is a community initiative to build the world's most comprehensive collection of software for materials science.

The intent is to improve the accessibility of these tools to all researchers by enabling one-line installations of highly useful software packages without the need for compilation, etc. All packages are hosted on the [matsci channel on Anaconda Cloud](https://anaconda.org/matsci).

## Available packages

The packages available are constantly updated. You can check out the currently available packages on the [matsci channel on Anaconda Cloud](https://anaconda.org/matsci), or simply look at the conda-skeletons folder in this repo. This effort initially arose from the desire to make [Python Materials Genomics](http://www.pymatgen.org) and its associated dependencies a lot easier to install for users on all platforms. So these will always be available. Please note that not all packages are available for all OSes.

## Getting started

Details instructions are available on [materials.sh](http://materials.sh). After installing conda or Anaconda, you can install materials science software packages in materials.sh via the following command:

```bash
conda install --channel matsci <package>
```

where `--channel matsci` indicates to use the matsci channel.

If you believe you will be using the channel frequently, you can add it to the list of channels in your environment with the following command:

```bash
conda config --add channels matsci
```

## Contributing

Contributions are always welcome. Feel free to fork this repo and add your proposed conda software recipes to the conda-skeletons folder. This repo is continuously integrated via [TravisCI](https://travis-ci.org/materialsvirtuallab/materials.sh) and [Appveyor](https://ci.appveyor.com/project/shyuep/materials-sh) to build all Linux, OSX and Windows versions, where compatible.

## Authors

This initiative is started by the [Materials Virtual Lab](http://materialsvirtuallab.org).