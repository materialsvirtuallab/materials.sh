set -e
cd conda-skeletons
conda build --skip-existing --user matsci tabulate
conda build --skip-existing --user matsci monty
conda update --all --yes
for pkg in `ls -d *`
do
    if [ "$pkg" != "atomate" ]; then
        conda build --skip-existing --user matsci $pkg
    fi
done
do
    if [ "$pkg" != "atomate" ]; then
        conda build --skip-existing --user matsci --python 2.7 $pkg
    fi
done
