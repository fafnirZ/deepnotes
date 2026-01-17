from __future__ import annotations
from dataclasses import dataclass
from typing import Any


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

    def __eq__(self, other: Any):
        if not isinstance(other, TagList):
            return False
        return sorted(self.tags) == sorted(other.tags)

    def intersect(self, other: TagList) -> TagList:
        self_tag_set = set(self.tags)
        other_tag_set = set(other.tags)
        intersected = self_tag_set.intersection(other_tag_set)
        return self.__class__(tags=list(intersected))
    

@dataclass
class CleanedTagList(TagList):
    pass

