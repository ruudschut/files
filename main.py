__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile

# opdracht 1, eerst kijken of de directory  bestaat, zo ja, verwijdere en lege directory aanmaken, zo nee, directory maken

def clean_cache():
    wd = os.getcwd()
    if os.path.exists(os.path.join(wd, "files", "cache")):
        shutil.rmtree(os.path.join(wd, "files", "cache"))
        os.mkdir(os.path.join(wd, "files", "cache"))
    else:
        os.mkdir(os.path.join(wd, "files", "cache"))

      
clean_cache()

# opdracht 2, pak het zip bestand uit in de cache directory

def cache_zip(file, dir):
    wd = os.getcwd()
    shutil.unpack_archive((os.path.join(wd, "files", file)), (os.path.join(wd, "files", dir)))

cache_zip("data.zip", "cache")

# opdracht 3, geef een lijst met alle files in de directory

directory = './files/cache'

def cached_files():
    my_path = os.path.abspath(directory)
    dir_cached_files = os.listdir(my_path)
    list_cached_files = []
    for file in dir_cached_files:
        list_cached_files.append(os.path.join(my_path, file))
    return list_cached_files

cached_files()


def find_password(files_list):
    for file in files_list:
        with open(file, 'r') as inhoud:
            tekst = inhoud.readlines()
            for file in tekst:
                if "password" in file:
                    pw = file[file.find(" ")+1:file.find("\\n")]
                    print(pw)
                    return pw
                    
        
find_password(cached_files())   

 