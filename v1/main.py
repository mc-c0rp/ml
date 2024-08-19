import minecraft_launcher_lib as mll
import os
from tqdm import tqdm
import subprocess


# eto vsio banalnaya hueten, dumaiu ya raberus potom
minecraft_directory = os.path.expanduser("~/.minecraft")

available_versions = mll.utils.get_available_versions(minecraft_directory)

release_versions = [version['id'] for version in available_versions if version['type'] == 'release']

# hueta ebanaya poka nenado
'''
print("Доступные релизные версии Minecraft: ")
for version in release_versions:
    print(version)
    '''

version = input("Введите версию Minecraft для запуска: ")

# progressbar'i NE TROGAT SUKA!!!!

def set_status(stat):
    pbar.status_printer(str(stat))

def set_total(tot):
    pbar.total = tot

def download_callback(progress):
    pbar.update(progress - pbar.n)

# version check mnogo bukav nihuia ne ponyatno)))

if not os.path.exists(os.path.join(minecraft_directory, 'versions', version)):
    ch = input(f"Версия {version} не установлена. Загрузить? y/n\n")
    if ch.lower() == 'y' or ch.lower() == 'н':
        print("Загрузка...")
        with tqdm(total=100, desc="Загрузка Minecraft", unit="%") as pbar:
            mll.install.install_minecraft_version(version, minecraft_directory, callback={"setProgress": download_callback, 'setMax': set_total, 'setStatus': set_status})
    else:
        exit()

# testovaya hueta potom ydalit nada suka
options = mll.utils.generate_test_options()

# nik
username = input("Введи ник: ")

# eto karoche auth no yasen hui chto ni u kogo net license po etamu offline
# p.s. (u menya est hehehehehehehhehe)
login_data = {
    "access_token": "0",
    "client_token": "0",
    "uuid": "0",
    "name": username,
    "user_type": "mojang"
}

# eto karoche ocen vazhno po etamu ne trogat
launch_command = mll.command.get_minecraft_command(version, minecraft_directory, login_data)

# a eto uzhe launch minecrafta
try:
    subprocess.run(launch_command, check=True)
except subprocess.CalledProcessError as e:
    print(f"Ошибка при запуске Minecraft: {e}")