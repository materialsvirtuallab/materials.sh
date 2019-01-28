cd conda-skeletons
conda install conda-build anaconda-client
conda install -n base conda==4.3.34 --yes
conda config --add channels matsci
conda config --set anaconda_upload yes
conda build --skip-existing --user matsci tabulate
conda build --skip-existing --user matsci monty
conda build --user matsci ruamel.yaml
FOR /D %%G in ("*") DO conda build  --skip-existing --user matsci %%G
cd ..
