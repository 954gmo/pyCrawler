# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import shutil

"""
I/O Stream (disk, network)

* read/write
* directory operations
* serialization/ deserialization ( the process of making variable conveyable or storing the variable to storage
    read()
    read(size)
    readline(limit)
    readlines(hint)
    

"""
import os


class FontColor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


filename = "IO.py"
mode = 'r' # rwab+
buffering = 1000 # 0 : no buffer, 1: buffer
try:
    f = open(file=filename, mode=mode, buffering=buffering)
    print(f"{FontColor.RED}reading all at once")
    print(f.read())
finally:
    if f:
        f.close()


size = 100
with open(file=filename, mode=mode, buffering=buffering) as file:
    print(f"{FontColor.BLUE}reading size every time with while")
    byte = file.read(size)
    while byte:
        print(byte)
        byte = file.read(size)

hint = 123
with open(file=filename, mode=mode) as file:
    print(f"{FontColor.MAGENTA}reading hint lines")
    cnt = 0
    for line in file.readlines(hint):
        print(line)
        cnt += len(line)

    print(cnt)

    print(f"{FontColor.YELLOW}read the rest ")
    for line in file.readlines():
        print(line)

limit = 4
with open(file=filename, mode=mode, buffering=buffering) as file:
    print(f"{FontColor.GREEN}read limit readline")
    for line in file.readline(limit):
        print(line)

    print(f"{FontColor.CYAN} read the rest")
    for line in file.readline():
        print(line)

with open(file='gmo001.txt', mode='wb') as file:
    file.write(b"what")

os.getcwd()
print(FontColor.RESET, os.listdir(os.path.expanduser('~')))
print(os.path.isfile(os.path.expanduser('~')))
print(os.path.isdir(os.path.expanduser('~')))
print(os.path.isabs(os.path.expanduser('~')))
print(os.path.exists('sdk'))
print(os.path.split(os.path.join(os.path.expanduser('~'), 'test.txt')))
print(os.path.splitext(os.path.join(os.path.expanduser('~'), 'test.txt.c')))
print(os.path.dirname(os.path.join(os.path.expanduser('~'), 'test.txt')))
print(os.path.basename(os.path.join(os.path.expanduser('~'), 'test.txt')))
# os.remove(filepath)
# os.removedirs(dir)
key = "PATH"
os.getenv(key)
# os.putenv(key, value)
os.linesep
os.name
# os.rename(old, new)
# os.makedirs(name=name, mode=mode, exist_ok=True)
# os.mkdir(path=path, mode=mode, dir_fd=dir_fd)
os.stat(filename)
# os.chmod(filename)
os.path.getsize(filename)
# shutil.copytree("old dir", "new dir")
# shutil.copyfile("old file", "new path")
# shutil.move("old path", "new path")
# os.rmdir("dir")
# shutil.rmtree("dir")


try:
    import cPickel as pickle
except ImportError:
    import pickle

d = dict(url='index.html', title='first page', content='content')
pickle.dumps(d)
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    print(pickle.load(f))

if __name__ == "__main__":
    pass
