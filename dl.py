#!/opt/homebrew/bin/python3

import subprocess
import pyperclip
import os


path = "/Users/chris/Desktop/new_dl"
try:
    os.mkdir(path)
except Exception:
    pass

finally:
    inp = '"' + pyperclip.paste().replace('\n', '" "') + '"'

    pyperclip.copy(
        f'aria2c -x 16 -s 16 -Z {inp} --dir="/Users/chris/Desktop/new_dl"')

    run = subprocess.run(
        f'aria2c -x 16 -s 16 -Z {inp} --dir="/Users/chris/Desktop/new_dl"',
        shell=True, check=True)

    print(run.returncode)
