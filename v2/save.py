import os
import exs
import json
# first setup launcher (suka sozdanie folder settings and sozdanie files users.json and settings.json blyat)
# ya ebu tut bukav i ifof
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
settings_dir = os.path.join(current_directory, 'settings')
user_file = os.path.join(settings_dir, 'user.json')
settings_file = os.path.join(settings_dir, 'settings.json')

def check():
    
    try:
        if os.path.isdir(settings_dir):
            print('settings OK')
            if os.path.isfile(user_file):
                print('user.json OK')
            else:
                print('user.json NOT FOUND')
                savef('user', exs.USERS_JSON)
                print('user.json CREATED')
                
            if os.path.isfile(settings_file):
                print('settings.json OK')
            else:
                print('settings.json NOT FOUND')
                savef('settings', exs.SETTINGS_JSON)
                print('settings.json CREATED')
        else:
            print('settings NOT FOUND')
            os.mkdir(settings_dir)
            print('settings CREATED')
            savef('settings', exs.SETTINGS_JSON)
            print('settings.json CREATED')
            savef('user', exs.USERS_JSON)
            print('user.json CREATED')

        print('checking done.')
        return 'ok'
    except Exception as ex:
        return f'ex: {ex}'

    
def savef(file, data:dict, indent=4):
    """
    Сохраняет данные в формате JSON в файл с указанным именем.

    :param file: Тип файла (settings, user)
    :param data: Переменная для сохранения
    :param indent: Количество пробелов для отступов в JSON (можно не трогать)
    """
    file = os.path.join(settings_dir, f'{file}.json') 
    try:
        with open(file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=indent)
        return 'ok'
    except (IOError, TypeError) as e:
        print(f"Ошибка при сохранении файла: {e}")
        return e

def loadj(file):
    """
    Загружает данные из JSON-файла.

    :param file: Тип файла (settings, user)
    :return: Данные, загруженные из JSON-файла
    """
    file = os.path.join(settings_dir, f'{file}.json') 
    try:
        with open(file, 'r') as file:
            data = json.load(file)
        return data
    except (IOError, json.JSONDecodeError) as e:
        print(f"Ошибка при открытии файла: {e}")
        return None