from src.config_manager import ConfigManager
from src.project_detection import get_languages_in_this_project, has_vscode_folder

print(get_languages_in_this_project("./src"))
print(has_vscode_folder("."))

print(ConfigManager())

