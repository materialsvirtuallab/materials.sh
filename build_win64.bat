cd conda-skeletons
conda install conda-build anaconda-client
conda config --add channels matsci
conda config --set anaconda_upload yes
FOR %%A IN (ase latexcodec pybtex spglib pyhull pymatgen pymatgen-db seekpath) DO conda build --user matsci %%A
cd ..
