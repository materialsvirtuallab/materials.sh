set -e
cd conda-skeletons
conda config --add channels matsci
conda install tabulate --yes
conda update --all --yes
for pkg in `ls -d *`
do
    conda build --skip-existing --user matsci $pkg
done
