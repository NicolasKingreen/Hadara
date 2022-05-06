import os


def get_files_inside(path):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        files.extend(filenames)
    return files


def shift(seq, n):
    """Shifts list to the left by n"""
    n = n % len(seq)
    return seq[n:] + seq[:n]


def get_key_from_value(d, val):
    for key, value in d.items():
        if value == val:
            return key
    return None
