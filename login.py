import os
import subprocess
import random

n = random.random()
username = os.environ['ANACONDA_USER']
password = os.environ['ANACONDA_PASSWORD']
subprocess.call(["anaconda", "login", "--hostname", "appveyor-mavrl-win64-py35-%s" % n, "--username", username, "--password", password])


