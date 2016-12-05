set -e
cd conda-skeletons
for pkg in `ls -d *`
do
    conda build --skip-existing --user matsci $pkg
done
