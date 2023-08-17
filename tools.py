from os import listdir, getcwd
from os.path import isfile, join, abspath

def get_turns_files_list():
    path = join(getcwd(), 'static/images/turns/')
    turns_files = [f for f in listdir(path) if isfile(join(path, f))]
    return turns_files
    
def get_tables_files_list():
    path = join(getcwd(), 'static/images/tables/')
    tables_files = [f for f in listdir(path) if isfile(join(path, f))]
    return tables_files