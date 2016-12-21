# coding: utf-8
# Copyright (c) Materials Virtual Lab.

import hashlib
import os
import pkg_resources
import requests
from invoke import task

from monty.os import cd

__author__ = "Shyue Ping Ong"
__email__ = "ongsp@ucsd.edu"
__date__ = "Sep 1, 2014"


module_dir = os.path.dirname(os.path.abspath(__file__))


def load_template(fname):
    with open(fname) as f:
        contents = f.read()
        from jinja2 import Template
        return Template(contents)


def calc_md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


@task
def update_pypi(ctx, pkg, ver):
    meta = os.path.join(module_dir, "conda-skeletons", pkg, "meta.yaml")
    url = "https://pypi.io/packages/source/%s/%s/%s-%s.tar.gz" % (pkg[0], pkg, pkg, ver)
    response = requests.get(url, stream=True)

    with open("temp.tar.gz", "wb") as f:
        for data in response.iter_content():
            f.write(data)
    md5 = calc_md5("temp.tar.gz")

    lines = []
    with open(meta) as f:
        for l in f:
            if l.startswith('{% set version ='):
                lines.append('{%% set version = "%s" %%}' % ver)
            elif l.startswith('{% set md5 ='):
                lines.append('{%% set md5 = "%s" %%}' % md5)
            else:
                lines.append(l.rstrip("\n"))
    with open(meta, "wt") as f:
        f.write("\n".join(lines))
    os.remove("temp.tar.gz")


def get_env_version(pkg):
    try:
        return pkg_resources.get_distribution(pkg).version
    except (ImportError, pkg_resources.DistributionNotFound):
        return None
    return None


@task
def generate_description(ctx):
    desc = []
    with cd(os.path.join(module_dir, "conda-skeletons")):
        for pkg in os.listdir("."):
            with open(os.path.join(module_dir, "conda-skeletons", pkg, "meta.yaml")) as f:
                contents = f.read()
                from jinja2 import Template
                t = Template(contents)
                import yaml
                d = yaml.load(t.render())
                description = d["about"].get("description")
                if description is not None:
                    desc.append('<tr><th style="text-align: left;">%s</th><td style="text-align: left;">%s</td></tr>' % (t.module.name, description.strip()))
    with open("description.html", "wt") as f:
        f.write("<table>" + "\n".join(desc) + "</table>")


@task
def update_templates(ctx):
    with cd(os.path.join(module_dir, "conda-skeletons")):
        for pkg in os.listdir("."):
            with open(os.path.join(module_dir, "conda-skeletons", pkg, "meta.yaml")) as f:
                contents = f.read()
                from jinja2 import Template
                t = Template(contents)
                name = t.module.name
                version = t.module.version
                env_version = get_env_version(name)
                if version != env_version:
                    print("Update %s from v%s to v%s" % (name, version, env_version))



@task
def build_conda(ctx, pkg):
    with cd(os.path.join(module_dir, "conda-skeletons")):
        print("Building %s" % pkg)
        ctx.run("conda build --user matsci %s" % pkg)


@task
def build_all(ctx):
    pkgs = sorted(os.listdir(os.path.join(module_dir, "conda-skeletons")))
    pkgs = [p for p in pkgs if p not in ["pybtex"]]
    for pkg in pkgs:
        build_conda(ctx, pkg)
