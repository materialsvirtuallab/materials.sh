set -e
cd conda-skeletons
conda config --add channels matsci
conda build --skip-existing --user matsci tabulate
conda update --all --yes
for pkg in `ls -d *`
do
    conda build --skip-existing --user matsci $pkg
done
