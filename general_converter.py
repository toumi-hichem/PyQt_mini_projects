# this dir is full of .ui files, this script traverses down the file tree and converts
# all ui files to py files to the same dir

import subprocess
import os

bat_file_path = r'C:\Users\toupa\Desktop\Projects\Python\Designer uis\ui_2_py.bat'

cwd = os.path.dirname(__file__)

for root, dirs, files in os.walk(cwd):
    for file in files:
        if '.ui' in file:
            INPUT_UI_FILE = os.path.join(root, file)
            OUTPUT_PY_FILE = os.path.join(root, file.replace(' ', '_')).replace('.ui', '.py')
            subprocess.run([bat_file_path, INPUT_UI_FILE, OUTPUT_PY_FILE], shell=True)
