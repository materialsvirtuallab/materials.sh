cd conda-skeletons
conda build --skip-existing --user matsci tabulate
conda build --skip-existing --user matsci monty
conda build --skip-existing --user matsci ruamel.yaml
conda build --skip-existing --user matsci --python 2.7 tabulate
conda build --skip-existing --user matsci --python 2.7 monty
conda build --skip-existing --user matsci --python 2.7 ruamel.yaml
# conda update --all --yes
for pkg in `ls -d *`
do
    conda build --skip-existing --user matsci $pkg
done
for pkg in `ls -d *`
do
    conda build --skip-existing --user matsci --python 2.7 $pkg
done
