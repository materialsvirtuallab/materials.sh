cd conda-skeletons
conda install conda-build anaconda-client
conda config --add channels matsci
conda config --set anaconda_upload yes
FOR %%A IN (latexcodec pybtex spglib pyhull pymatgen seekpath) DO conda build --user matsci %%A
cd ..
