#!/usr/bin/python3

import os
import sys
import shutil
import tarfile
import tempfile


output = tempfile.mkdtemp()
print("Extracting to: %s" % output)
original = os.getcwd()
dist = os.path.join(original, 'dist')
print("Looking in %s" % dist)
if not os.path.isdir(dist):
    print("No 'dist' directory found in %s" % original)
tarballs = os.listdir(dist)
if len(tarballs) != 1:
    print("Only one tarball in dist is supported.")
    os.chdir(original)
    shutil.rmtree(output)
    sys.exit(2)
tarball = os.path.join(original, 'dist', tarballs[0])
fixup = os.path.join(original, 'dist', tarballs[0].lower())
os.chdir(output)
tar = tarfile.open(tarball)
tar.extractall()
tar.close()
contents = os.listdir(output)
if not contents[0].startswith('pyOCD'):
    print("Cannot find bad directory %s." % bad)
    os.chdir(original)
    shutil.rmtree(output)
    sys.exit(2)
bad = os.path.join(output, contents[0])
print("Renaming %s to %s" % (bad, bad.lower()))
os.rename(bad, bad.lower())
contents = os.listdir(output)
os.remove(tarball)
with tarfile.open(fixup, 'w:gz') as fixed:
    fixed.add(contents[0].lower())

os.chdir(original)
shutil.rmtree(output)

