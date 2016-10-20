#!/bin/bash

for pkg in latexcodec  monty  palettable  pybtex  pydispatcher tabulate
do
        conda build "$pkg"
        anaconda upload --force --user matsci $HOME/miniconda3/conda-bld/noarch/$pkg*.tar.bz2
done
