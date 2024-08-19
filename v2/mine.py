import minecraft_launcher_lib as mll
import os
import subprocess

current_directory = os.path.dirname(os.path.abspath(__file__))
mine_dir = os.path.join(current_directory, '.minecraft')
if not os.path.isdir(mine_dir):
    os.mkdir(mine_dir)

minecraft_directory = mine_dir

def get_ver():
    available_versions = mll.utils.get_available_versions(mine_dir)
    release_versions = [version['id'] for version in available_versions if version['type'] == 'release']
    return release_versions

def install(ver):
    print('downloading ver ' + ver)
    mll.install.install_minecraft_version(ver, mine_dir)
    print('downloaded')

def launch(username, ver):
    if not os.path.exists(os.path.join(mine_dir, 'versions', ver)):
        install(ver)
    login_data = {
    "access_token": "0",
    "client_token": "0",
    "uuid": "0",
    "name": username,
    "user_type": "mojang"
    }
    options = mll.utils.generate_test_options()
    # eto karoche ocen vazhno po etamu ne trogat
    launch_command = mll.command.get_minecraft_command(ver, minecraft_directory, login_data)
    try:
        subprocess.run(launch_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске Minecraft: {e}")