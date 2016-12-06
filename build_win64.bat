cd conda-skeletons
conda install conda-build anaconda-client
conda config --add channels matsci
conda config --set anaconda_upload yes
FOR %%A IN (ase latexcodec pybtex spglib pymatgen pymatgen-db seekpath) DO conda build  --skip-existing --user matsci %%A
FOR %%A IN (ase latexcodec pybtex spglib pymatgen pymatgen-db seekpath) DO conda build  --skip-existing --user matsci --python 2.7 %%A
cd ..
