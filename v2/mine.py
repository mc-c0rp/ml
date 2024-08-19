import minecraft_launcher_lib as mll
import os
import subprocess
from tqdm import tqdm

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
    print(f'Скачивание версии {ver}...')
    mll.install.install_minecraft_version(ver, mine_dir)
    print('Скачано')

def launch(username, ver):
    if not os.path.exists(os.path.join(mine_dir, 'versions', ver)):
        global pbar
        pbar = tqdm(total=100, desc="Загрузка Minecraft", unit="%")

        def set_status(stat):
            pbar.set_description(str(stat))

        def set_total(tot):
            pbar.total = tot

        def download_callback(progress):
            pbar.update(progress - pbar.n)

        mll.install.install_minecraft_version(ver, minecraft_directory, callback={"setProgress": download_callback, 'setMax': set_total, 'setStatus': set_status})
        pbar.close()

    login_data = {
        "access_token": "0",
        "client_token": "0",
        "uuid": "0",
        "name": username,
        "user_type": "mojang"
    }
    options = mll.utils.generate_test_options()
    launch_command = mll.command.get_minecraft_command(ver, minecraft_directory, login_data)
    try:
        subprocess.run(launch_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске Minecraft: {e}")

# Пример использования
# versions = get_ver()
# install('1.19.2')  # Замените на нужную версию
# launch('username', '1.19.2')  # Замените на нужную версию
