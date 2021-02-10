import os

def get_created_file_dir():
    basedir = os.path.abspath(os.path.dirname(__file__))
    return basedir