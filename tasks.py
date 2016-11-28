# coding: utf-8
# Copyright (c) Materials Virtual Lab.

import glob
import os
import shutil

from invoke import task

from monty.os import cd
from monty.serialization import loadfn, dumpfn

__author__ = "Shyue Ping Ong"
__email__ = "ongsp@ucsd.edu"
__date__ = "Sep 1, 2014"


module_dir = os.path.dirname(os.path.abspath(__file__))

@task
def update_pypi(ctx, pkg):
    with cd(os.path.join(module_dir, "conda-skeletons")):
        meta = os.path.join(pkg, "meta.yaml")
        noarch = False
        if os.path.exists(meta):
            d = loadfn(meta)
            noarch = d.get("build", {}).get("noarch_python", False)
            shutil.rmtree(pkg)
        if not noarch:
            if pkg == "pymatgen":
                ctx.run("conda skeleton pypi --setup-options='--single-version-externally-managed --record=record.txt' %s" % pkg)
            else:
                ctx.run("conda skeleton pypi %s" % pkg)
        else:
            ctx.run("conda skeleton pypi --noarch-python %s" % pkg)
        if pkg == "pymatgen":
            d = loadfn(meta)
            d["requirements"]["build"].append("enum34")
            d["requirements"]["run"].append("enum34")
            dumpfn(d, meta, default_flow_style=False)
            ctx.run('sed -i "" "s/enum34/enum34 #[py27]/g" %s' % meta)


@task
def build_conda(ctx, pkg, nopy27=False):
    with cd(os.path.join(module_dir, "conda-skeletons")):
        d = loadfn(os.path.join(pkg, "meta.yaml"))
        noarch = d.get("build", {}).get("noarch_python", False)
        if noarch:
            ctx.run("conda build --user matsci %s" % pkg)
            # fnames = glob.glob(os.path.join(os.path.expanduser("~"),
            #                                 "miniconda3", "conda-bld", "noarch",
            #                                 "%s-*py*.tar.bz2" % pkg))
            # latest = sorted(fnames)[-1]
            # ctx.run("anaconda upload --force --user matsci %s" % latest)
        else:
            # Py35 versions
            ctx.run("conda build --user matsci %s" % pkg)
            # fnames = glob.glob(os.path.join(os.path.expanduser("~"),
            #                                 "miniconda3", "conda-bld", "*",
            #                                 "%s-*py35*.tar.bz2" % pkg))
            # latest = sorted(fnames)[-1]
            # ctx.run("anaconda upload --force --user matsci %s" % latest)

            if not nopy27:
                # Py27 versions
                ctx.run("conda build --user matsci --python 2.7 %s" % pkg)
                # fnames = glob.glob(os.path.join(os.path.expanduser("~"),
                #                                 "miniconda3", "conda-bld", "*",
                #                                 "%s-*py27*.tar.bz2" % pkg))

                # latest = sorted(fnames)[-1]
                # ctx.run("anaconda upload --force --user matsci %s" % latest)

@task
def build_all(ctx, nopy27=False):
    pkgs = sorted(os.listdir(os.path.join(module_dir, "conda-skeletons")))
    pkgs = [p for p in pkgs if p not in ["bader", "enumlib"]]
    for pkg in pkgs:
        build_conda(ctx, pkg, nopy27=nopy27)
