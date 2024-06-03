import os


def refresh():
    command = 'sudo ./static/refresh.sh'
    os.system(command)