#!/bin/bash

if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
    if [[ "$TOXENV" == "py27" ]]; then
        curl -o miniconda.sh https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh;
    else
        curl -o miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh;
    fi
else
    if [[ "$TRAVIS_PYTHON_VERSION" == "2.7" ]]; then
        wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O miniconda.sh;
    else
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh;
    fi
fi

bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
hash -r
conda config --set always_yes yes --set changeps1 no
conda update -q conda
# Useful for debugging any issues with conda
conda info -a
conda install conda-build anaconda-client
conda config --add channels matsci
conda config --add channels conda-forge
if [[ "$TOXENV" == "py36" ]]; then
    conda install python==3.6 --yes
fi

if [ "$TRAVIS_BRANCH" == "master" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    conda config --set anaconda_upload yes;
    python login.py;
else
    conda config --set anaconda_upload no;
fi
