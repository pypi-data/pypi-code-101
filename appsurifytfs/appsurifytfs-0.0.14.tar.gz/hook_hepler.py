# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
import os
import json
import string

def execute(commandLine):
    process = Popen(commandLine, shell=True, stdout=PIPE, stderr=PIPE)
    out = process.stdout.read().decode('utf-8', errors='ignore').strip()
    out = str.join("", list([x for x in out if x in string.printable]))
    error = process.stderr.read().decode('utf-8', errors='ignore').strip()
    error = str.join("", list([x for x in error if x in string.printable]))
    if error and not out:
        process.kill()
        raise Exception(error)
    return out


commandLine = "git for-each-ref"

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), u'.testbrain.db')
class SimpleDB(object):
    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dumpdb()

    def load(self, location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        self.db = json.load(open(self.location, "r"))

    def dumpdb(self):
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except Exception as e:
            logging.error("Error saving database file. '{}'".format(e), exc_info=DEBUG)
            return False

    def set(self, key, value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
        except Exception as e:
            logging.error("Error saving values to database. '{}'".format(e), exc_info=DEBUG)
            return False

    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            logging.debug("No Value Can Be Found for {}".format(key))
            return False

    def delete(self, key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True

    def resetdb(self):
        self.db = {}
        self.dumpdb()
        return True


database = SimpleDB(location=DB_FILE)


output = execute(commandLine)

# database.set(key, val)

for line in output.splitlines():
    sha, ref_type, ref = line.split()

    if ref_type != "commit":
        continue

    if not ref.startswith("refs/remotes/origin/"):
        continue

    ref = ref[len("refs/remotes/origin/"):]

    print(ref + "\t" + sha)
    database.set(ref, sha)
