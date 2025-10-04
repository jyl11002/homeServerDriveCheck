#!/usr/bin/python3

import os
import subprocess
import json
import logging
import sys
from logging.handlers import RotatingFileHandler

file_directory = os.path.abspath('/root/Maintenance')
sys.path.insert(0, file_directory)

import fan_leds

# Set up logger
logger = logging.getLogger("driveTest_logger")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(
        "drivecheck.log",
        maxBytes=1024*2048,
        backupCount=5
        )
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def get_list_of_drives:
    ls_output = subprocess.run(['ls', '/dev'], capture_output=True, text=True, check=True)
    ls_lines = ls_output.stdout.splitlines()
    return ls_lines

def smartctlCheck:
    for line in ls_lines:
        if line[0:2] == 'sd' and not line[-1].isdigit():
     
def main():
    logger.info('Weekly Test being run')

    fan_leds.set_to_bad()
    logger.info('LEDS set')
