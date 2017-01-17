cd conda-skeletons
conda install conda-build anaconda-client
conda config --add channels matsci
conda config --set anaconda_upload yes
conda build --skip-existing --user matsci tabulate
conda build --skip-existing --user matsci monty
FOR /D %%G in ("*") DO conda build  --skip-existing --user matsci %%G
cd ..
