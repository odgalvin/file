#!/usr/bin/python3

from os import rename, getcwd
from os.path import basename, exists, isdir, join
from sys import argv, exit
from subprocess import run

if len(argv) != 3:
    raise ValueError(f"Usage: {argv[0]} FILE_CMD MAGIC_DIR")

file_cmd = argv[1]
in_dir = argv[2]
if not isdir(in_dir):
    print(f"No directory '{in_dir}' found.")
    exit(1)
magic_ext = ".mgc"
run([file_cmd, "-C", "-m", in_dir])
output = basename(in_dir) + magic_ext
if not exists(output):
    print(f"Could not compile magic from {in_dir}.")
    exit(1)
final_output = join(getcwd(), "magic" + magic_ext)
rename(output, final_output)
print(f"Magic data in {in_dir} was compiled and saved to {final_output}.")
exit(0)
