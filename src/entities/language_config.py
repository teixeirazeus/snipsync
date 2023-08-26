from dataclasses import dataclass

@dataclass
class LanguageConfig:
    """
    LanguageConfig is a dataclass that represents a programming language configuration.
    name: str - The name of the programming language.
    extensions: list[str] - The file extensions of the programming language.
    name_file_snippet: str - The name of the file that contains the snippet.
    """
    name: str
    extensions: list[str]
    name_file_snippet: str
    
    def has_any_extension(self, extensions: set[str]) -> bool:
        """
        Returns True if the language has any extension in the extensions set.
        """
        for extension in self.extensions:
            if extension in extensions:
                return True
        return False
    