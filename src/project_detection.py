import os
from typing import List
from src.entities.language_config import LanguageConfig
from src.languages import languages

def has_vscode_folder(directory: str) -> bool:
    return ".vscode" in os.listdir(directory)

def get_languages_in_this_project(directory: str) -> List[LanguageConfig]:
    file_extensions = get_file_extensions(directory)
    languages_in_this_project = []
    
    for language in languages:
        if language.has_any_extension(file_extensions):
            languages_in_this_project.append(language)
    
    return languages_in_this_project
    
def get_file_extensions(directory: str) -> set[str]:
    extensions = set()
    for _, _, filenames in os.walk(directory):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext:
                extensions.add(ext.lower())

    return extensions
    