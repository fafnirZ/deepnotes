from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from deepnotes.extracted_tags import CleanedTagList, TagList

type NodeId = Path

@dataclass
class FileNode:
    file_path: Path
    tags: TagList | CleanedTagList

    def __post_init__(self):
        assert isinstance(self.file_path, Path)
        assert self.file_path.is_file()
        assert isinstance(self.tags, TagList)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, FileNode):
            return False
        
        return (
            self.file_path == other.file_path
            and self.tags == other.tags
        )
    
    @property
    def id(self) -> NodeId:
        return self.file_path