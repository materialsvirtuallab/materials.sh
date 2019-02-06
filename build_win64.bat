cd conda-skeletons
conda install conda-build anaconda-client
conda config --add channels matsci
conda config --set anaconda_upload yes
conda build --skip-existing --user matsci tabulate
conda build --skip-existing --user matsci monty
conda build --user matsci ruamel.yaml
conda build --user matsci pymatgen
FOR /D %%G in ("*") DO conda build  --skip-existing --user matsci %%G
cd ..
