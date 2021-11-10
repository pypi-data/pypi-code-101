from pathlib import Path
import json

class ConfigValidationError(Exception):
    """Raised when there is an error in the config file."""

    def __init__(self, message):
        self.message = message
        super().__init__()

    def __str__(self):
        return f"{self.message}"

class Config:
    """
    Parses a config file and into a dictionary.

    Loads from provided path, otherwise loads default configuration file.
    """

    def __init__(self, config_path=None):
        self.path = Path(config_path) if config_path else Path("./config.json")
        self.data = self.load()
            
    def load(self) -> dict:
        """Loads the config file into a dictionary."""
        try:
            with self.path.open() as f:
                config = json.load(f)
            return config
        except json.decoder.JSONDecodeError as e:
            raise ConfigValidationError(
                "Could not load configuration file") from e
    
    def validation(self):
        # got error for ksize of (100, 100) and (22, 22)
        # ksize.width > 0 && ksize.width % 2 == 1 && ksize.height > 0 && ksize.height % 2 == 1
        # ksize width and height must be over 0 and odd
        pass