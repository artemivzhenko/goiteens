from os import system
from os import listdir
from os import getcwd
import os

ui_files = [f for f in listdir(getcwd()) if f.endswith('.ui')]

for f in ui_files:
    py_file_name = f.replace(".ui", ".py")
    dir_name = f.replace(".ui", "")
    os.mkdir(dir_name)
    system(f"pyuic6 {f} -o {dir_name}/{py_file_name}")
    system(f"mv {f} {dir_name}/")
    
