from os import listdir, getcwd  
from os.path import isfile, join, abspath

def get_turns_files_list():
    path = join(getcwd(), 'static/images/turns/')
    turns_files = [f for f in listdir(path) if isfile(join(path, f))]
    return turns_files
    
def get_tables_files_list():
    path = join(getcwd(), 'static/tables/tables.txt')
    tables_names = [line.split('=')[0] for line in open(path).readlines()]
    tables_images = [line.split('=')[1] for line in open(path).readlines()]
    return tables_names, tables_images
    
def get_maps_files_list():
    path = join(getcwd(), 'static/maps/maps.txt')
    maps_names = [line.split('=')[0] for line in open(path).readlines()]
    maps_images = [line.split('=')[1] for line in open(path).readlines()]
    return maps_names, maps_images
    
def get_players_list():
    path = join(getcwd(), 'static/players/')
    return open(join(path, 'players.txt'), 'r').readlines()  