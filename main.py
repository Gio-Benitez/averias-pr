import subprocess
import os
import sys

# Context manager for changing the current working directory
class cd:
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

# Define Database Setup working directory
database_setup_DIR = os.getcwd() + "/db_setup/"

with cd(database_setup_DIR):
   process = subprocess.Popen(['bash build.sh'],shell=True,stdout=sys.stdout,stderr=subprocess.STDOUT)
   process.wait()
   returncode = process.returncode
