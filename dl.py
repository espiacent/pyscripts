#!/opt/homebrew/bin/python3

import subprocess
import pyperclip
import os
import getpass

path = f'/Users/{getpass.getuser()}/Desktop/new_dl'
try:
    os.mkdir(path)
except Exception:
    pass

finally:
    inp = '"' + pyperclip.paste().replace('\n', '" "') + '"'

    run = subprocess.run(
        f'aria2c -x 16 -s 16 -Z {inp} --dir="{path}"',
        shell=True, check=True)

    print(run.returncode)
