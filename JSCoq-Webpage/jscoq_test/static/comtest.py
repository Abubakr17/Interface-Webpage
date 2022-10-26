import os
import subprocess

#print(subprocess.run('cd sml-to-coq && sml @SMLload test-img.amd64-darwin induction.sml pytest.v', shell=True, capture_output=True))
with open("sml-to-coq/pytest.v","r") as smlfile:
    print(smlfile.readlines())