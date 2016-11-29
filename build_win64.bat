cd conda-skeletons
conda install conda-build anaconda-client
conda config --add channels matsci
conda config --set anaconda_upload yes
anaconda login --hostname travis-mavrl-win64-py35 --username %ANACONDA_USER% --password %ANACONDA_PASSWORD%
FOR %%A IN (latexcodec tabulate monty pybtex palettable spglib pydispatcher pymatgen) DO conda build %%A
cd ..
