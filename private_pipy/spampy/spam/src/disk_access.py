import os
from pathlib import Path
from typing import List


class FileManager:
    """
    Simple class that can do things with files and directories with the passed in path...
    """
    def __init__(self, path: Path) -> None:
        self.path = path

    def list_dir(self) -> List[str]:
        return os.listdir(self.path)
