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


# ui

def print_centered(text, filler='', end='\n'):
    print(f'{text:{filler}^80}', end=end)


def print_choices_incol(seq, spaces=20):
    for i, item in enumerate(seq):
        line = f'{i+1}. {item}'
        print(" " * spaces, line)


def print_choices_inline(seq, spaces=20):
    output = ""
    for i, item in enumerate(seq):
        output += f'{i+1}. {item}\t'
    output = output.center(80)
    print(output)
