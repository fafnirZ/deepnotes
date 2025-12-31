from abc import ABC, abstractmethod
from enum import Enum, auto
from pathlib import Path

from deepnotes.extracted_tags import TagList


class SemanticAgent(ABC):
    @classmethod
    @abstractmethod
    def extract_tags(cls, contents: str):
        raise NotImplementedError

    @classmethod
    def extract_file(cls, file_path: Path) -> TagList:
        assert isinstance(file_path, Path)
        with open(file_path, "r") as f:
            return cls.extract_tags(f.read())



    
