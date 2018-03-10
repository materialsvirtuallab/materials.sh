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
__date__ = "Aug 8, 2017"


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
def update_pypi(ctx, pkg):

    r = requests.get("http://pypi.org/project/%s/" % pkg)
    html_doc = r.text
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')
    header = soup.h1.text
    ver = header.strip().split()[-1]
    
    meta = os.path.join(module_dir, "conda-skeletons", pkg, "meta.yaml")
    url = "https://pypi.io/packages/source/%s/%s/%s-%s.tar.gz" % (pkg[0], pkg, pkg, ver)
    response = requests.get(url, stream=True)

    with open("temp.tar.gz", "wb") as f:
        for data in response.iter_content():
            f.write(data)
    md5 = calc_md5("temp.tar.gz")
    os.remove("temp.tar.gz")

    lines = []
    current_ver = None
    with open(meta) as f:
        for l in f:
            if l.startswith('{% set version ='):
                current_ver = l.strip().split("=")[-1]
                current_ver = current_ver.split("%")[0].strip().strip("\"")
                lines.append('{%% set version = "%s" %%}' % ver)
            elif l.startswith('{% set md5 =') and current_ver != ver and ver != "different":
                lines.append('{%% set md5 = "%s" %%}' % md5)
            else:
                lines.append(l.rstrip("\n"))

    if current_ver != ver and ver != "different":
        print("Updated %s from %s to %s!" % (pkg, current_ver, ver))
        with open(meta, "wt") as f:
            f.write("\n".join(lines))
    else:
        print("%s current version (%s) is up to date!" % (pkg, ver))


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
            update_pypi(ctx, pkg)


@task
def build_conda(ctx, pkg):
    with cd(os.path.join(module_dir, "conda-skeletons")):
        print("Building %s" % pkg)
        ctx.run("conda build --skip-existing --user matsci %s" % pkg)


@task
def build_all(ctx):
    pkgs = sorted(os.listdir(os.path.join(module_dir, "conda-skeletons")))
    pkgs = [p for p in pkgs if p.lower() not in ["pybtex", "bader", "boltztrap"]]
    for pkg in pkgs:
        build_conda(ctx, pkg)
