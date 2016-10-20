# coding: utf-8
# Copyright (c) Materials Virtual Lab.

import glob
import os
import shutil

from invoke import task

from monty.os import cd

__author__ = "Shyue Ping Ong"
__email__ = "ongsp@ucsd.edu"
__date__ = "Sep 1, 2014"


@task
def build_conda_noarch(ctx):
    with cd("conda-skeletons/noarch"):
        for pkg in os.listdir():
            ctx.run("conda build %s" % pkg)
            fnames = glob.glob(os.path.expanduser("~/miniconda3/conda-bld/noarch/%s-*py*.tar.bz2" % pkg))

            latest = sorted(fnames)[-1]
            ctx.run("anaconda upload --force --user matsci %s" % latest)


@task
def build_conda_platform(ctx):
    with cd("conda-skeletons/platform"):
        for pkg in ["spglib", "pymatgen"]:
            # Py35 versions
            ctx.run("conda build %s" % pkg)
            fnames = glob.glob(os.path.expanduser(
                "~/miniconda3/conda-bld/*/%s-*py35*.tar.bz2" % pkg))
            latest = sorted(fnames)[-1]
            ctx.run("anaconda upload --force --user matsci %s" % latest)

            # # Py27 versions
            # if pkg == "pymatgen":
            #     shutil.copy("pymatgen/meta.yaml", "pymatgen/meta.yaml.bak")
            #     with open("pymatgen/meta.yaml", "rt") as f:
            #         lines = []
            #         for l in f:
            #             l = l.rstrip()
            #             lines.append(l)
            #             if l.startswith("    - palettable"):
            #                 lines.append("    - enum34")
            #     with open("pymatgen/meta.yaml", "wt") as f:
            #         f.write("\n".join(lines))
            # ctx.run("conda build --python 2.7 %s" % pkg)
            # fnames = glob.glob(os.path.expanduser(
            #     "~/miniconda3/conda-bld/*/%s-*py27*.tar.bz2" % pkg))
            # latest = sorted(fnames)[-1]
            # ctx.run("anaconda upload --force --user matsci %s" % latest)
            # if pkg == "pymatgen":
            #     shutil.move("pymatgen/meta.yaml.bak", "pymatgen/meta.yaml")


@task
def build_conda(ctx):
    build_conda_noarch(ctx)
    build_conda_platform(ctx)