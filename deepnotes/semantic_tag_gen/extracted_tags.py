from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TagList:
    tags: list[str]

    def clean(self) -> CleanedTagList:
        _tags = self.tags[:] # clone
        # remove whitespace
        _tags = list(map(lambda x: x.strip(), _tags))
        # to lower all tags
        _tags = list(map(lambda x: x.lower(), _tags))
        return CleanedTagList(_tags)

    def __eq__(self, other: TagList):
        if not isinstance(other, TagList):
            return False
        return sorted(self.tags) == sorted(other.tags)

@dataclass
class CleanedTagList(TagList):
    pass

