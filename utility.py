import os


def get_files_inside(path):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        files.extend(filenames)
    return files
