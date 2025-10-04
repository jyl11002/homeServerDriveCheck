#!/usr/bin/python3

import os
import subprocess
import json
import sys

file_directory = os.path.abspath('/root/Maintenance')
sys.path.insert(0, file_directory)

import fan_leds

ls_output = subprocess.run(['ls', '/dev'], capture_output=True, text=True, check=True)
ls_lines = ls_output.stdout.splitlines()

for line in ls_lines:
    if line[0:2] == 'sd' and not line[-1].isdigit():
            print(line)
fan_leds.set_to_bad()

