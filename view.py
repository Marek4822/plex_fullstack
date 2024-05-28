import os

def view_file_list(playlist):
    path = f'/home/marek/python/plex_fullstack/{playlist}'
    file_list = []
    count_file = 0
    for file in os.listdir(path):
        if file.endswith('m4a'):
            file_list.append(file)
            count_file += 1

    return file_list, count_file

def view_dir():
    path = '/home/marek/python/plex_fullstack'
    dir_list = []
    count_dir = 0
    dirs = os.listdir(path)
    for dir in dirs:
        if os.path.isdir(dir):
            dir_list.append(dir)
            count_dir += 1
    
    return dir_list, count_dir


