cd conda-skeletons
conda install conda-build anaconda-client
conda config --add channels matsci
conda config --set anaconda_upload yes
FOR %%A IN (latexcodec tabulate monty pybtex palettable spglib pydispatcher pymatgen) DO conda build --user matsci %%A
cd ..
