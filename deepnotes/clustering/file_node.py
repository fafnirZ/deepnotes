
from dataclasses import dataclass
from pathlib import Path

from deepnotes.extracted_tags import CleanedTagList, TagList


@dataclass
class FileNode:
    file_path: Path
    tags: TagList | CleanedTagList

    def __post_init__(self):
        assert isinstance(self.file_path, Path)
        assert self.file_path.is_file()
        assert isinstance(self.tags, TagList)
    
    
