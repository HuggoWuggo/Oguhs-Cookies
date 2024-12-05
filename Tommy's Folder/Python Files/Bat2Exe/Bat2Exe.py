import os
from shutil import rmtree
from getpass import getuser
from PyColour import pycolour

def header() -> None:
    pycolour('blue', r"    ____        __     ______         ______         ".center(100, ' '), 'bold')
    pycolour('blue', r"   / __ )____ _/ /_   /_  __/___     / ____/  _____  ".center(100, ' '), 'bold')
    pycolour('blue', r"  / __  / __ `/ __/    / / / __ \   / __/ | |/_/ _ \ ".center(100, ' '), 'bold')
    pycolour('dark blue', r" / /_/ / /_/ / /_     / / / /_/ /  / /___ >  </  __/ ".center(100, ' '), 'bold')
    pycolour('dark blue', r"/_____/\__/_/\__/    /_/  \____/  /_____/_/|_|\___/  ".center(100, ' '), 'bold')
    print('')

def get_batch_code() -> None:
    with open(bat_file_path, 'r') as f:
        for line in f:
            batch_code.append(line)

def create_python_file() -> None:
    with open(py_file_path, 'a') as f:
        f.write("from os import system, remove\n")
        f.write("from getpass import getuser\n")
        f.write("create_bat_file: str = fr'C:\\Users\\{getuser()}\\AppData\\Local\\Temp\\Compiled.bat'\n")
        f.write(f"batch_code: list[str] = {batch_code}\n")
        f.write("with open(create_bat_file, 'a') as f:\n")
        f.write("    for line in batch_code:\n")
        f.write("        f.write(line)\n")
        f.write("""system(f'"{create_bat_file}"')\n""")
        f.write("remove(create_bat_file)")

def convert_to_exe() -> None:
    os.chdir(temp_path)
    if is_icon:
        os.system(f'python -m PyInstaller --onefile -i "{icon_path}" "{py_file_path}"')
    else:
        os.system(f'python -m PyInstaller --onefile "{py_file_path}"')
    os.remove(py_file_path)
    rmtree(fr'{temp_path}\build')
    os.remove(fr'{temp_path}\{bat_file_name}.spec')
    os.rename(fr'{temp_path}\dist\{bat_file_name}.exe', fr'{bat_file_directory}\{bat_file_name}.exe')
    os.rmdir(fr'{temp_path}\dist')

header()

bat_file_path: str = r'{}'.format(input('\033[36mBatch File Path: \033[32m').replace('"', ''))
if input('\033[36mInclude Icon (Y | N): \033[32m') in ['Yes', 'yes', 'Y', 'y']:
    is_icon: bool = True
    icon_path: str = r'{}'.format(input('\033[36mIcon Path: \033[32m').replace('"', ''))
else:
    is_icon: bool = False

temp_path: str = fr'C:\Users\{getuser()}\AppData\Local\Temp'
bat_file_directory: str = '\\'.join(bat_file_path.split('\\')[:-1])
bat_file_name: str = bat_file_path.split('\\')[-1].removesuffix('.bat')
py_file_path: str = fr'{temp_path}\{bat_file_name}.py'
batch_code: list[str] = []

os.system('cls')

header()

get_batch_code()
create_python_file()
convert_to_exe()