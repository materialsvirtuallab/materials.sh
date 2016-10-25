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
    with cd(os.path.join("conda-skeletons", "noarch")):
        for pkg in os.listdir():
            ctx.run("conda build %s" % pkg)
            fnames = glob.glob(os.path.join(os.path.expanduser("~"),
                "miniconda3", "conda-bld", "noarch", "%s-*py*.tar.bz2" % pkg))

            latest = sorted(fnames)[-1]
            ctx.run("anaconda upload --force --user matsci %s" % latest)


@task
def build_conda_platform(ctx, nopy27=False):
    with cd(os.path.join("conda-skeletons", "platform")):
        for pkg in ["latexcodec", "pybtex", "spglib", "pymatgen"]:
            # Py35 versions
            ctx.run("conda build %s" % pkg)
            fnames = glob.glob(os.path.join(os.path.expanduser("~"),
                "miniconda3", "conda-bld", "*", "%s-*py35*.tar.bz2" % pkg))
            latest = sorted(fnames)[-1]
            ctx.run("anaconda upload --force --user matsci %s" % latest)

            if not nopy27:
                # Py27 versions
                ctx.run("conda build --python 2.7 %s" % pkg)
                fnames = glob.glob(os.path.join(os.path.expanduser("~"),
                                                "miniconda3", "conda-bld", "*",
                                                "%s-*py27*.tar.bz2" % pkg))

                latest = sorted(fnames)[-1]
                ctx.run("anaconda upload --force --user matsci %s" % latest)


@task
def build_conda(ctx, nopy27=False):
    build_conda_noarch(ctx)
    build_conda_platform(ctx, nopy27=nopy27)
