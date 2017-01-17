set -e
cd conda-skeletons
conda build --skip-existing --user matsci tabulate
for pkg in `ls -d *`
do
    conda build --skip-existing --user matsci $pkg
done
