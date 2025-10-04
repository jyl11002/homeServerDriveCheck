import subprocess

def set_to_bad():
    command = "openrgb -d 0 --mode breathing -c ff0000 -s 80"
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    return
def set_to_good():
    command = "openrgb -d 0 -c random"
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    return
def set_to_warning():
    command = "openrgb -d 0 -c ffff00 --mode breathing -s 80"
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    return
