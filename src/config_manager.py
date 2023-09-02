import json
from dataclasses import dataclass
import os

@dataclass
class ConfigSettings:
    gh_repository: str
    
class ConfigManager:
    FOLDER_NAME = 'snipsync'
    CONFIG_FILE_NAME = 'config.json'
    
    def __init__(self):
        self.load_config()
        self.config = None
    
    def load_config(self):
        self.create_folder_if_dont_exist()
        config_file_exists = os.path.isfile(self.get_config_file_path())
        if config_file_exists:
            self.config = self.load_config_file()
        else:
            self.config = self.create_config_file()
            
    def create_config_file(self):
        config_file_path = self.get_config_file_path()
        with open(config_file_path, 'w', encoding="utf-8") as config_file:
            config = ConfigSettings(gh_repository='')
            config_json = json.dumps(config.__dict__, indent=4)
            config_file.write(config_json)
            return config
    
    def load_config_file(self):
        config_file_path = self.get_config_file_path()
        with open(config_file_path, encoding="utf-8") as config_file:
            config_json = json.load(config_file)
            return ConfigSettings(**config_json)
        
    def get_config_file_path(self):
        user_home = os.path.expanduser('~')
        config_path = os.path.join(user_home, '.config')
        return os.path.join(config_path, ConfigManager.FOLDER_NAME, ConfigManager.CONFIG_FILE_NAME)
    
    def create_folder_if_dont_exist(self):
        snipsync_path = self.get_snipsync_path()
        directory_exists = os.path.isdir(snipsync_path)
        if not directory_exists:
            self.create_config_folder()

    def get_snipsync_path(self):
        config_path = self.get_config_path()
        snipsync_path = os.path.join(config_path, ConfigManager.FOLDER_NAME)
        return snipsync_path
        
    def create_config_folder(self):
        config_path = self.get_config_path()
        os.mkdir(os.path.join(config_path, ConfigManager.FOLDER_NAME))

    def get_config_path(self):
        user_home = os.path.expanduser('~')
        config_path = os.path.join(user_home, '.config')
        return config_path
            
    def has_config_folder(self, dirnames):
        for dirname in dirnames:
            if dirname == ConfigManager.FOLDER_NAME:
                return True
        return False