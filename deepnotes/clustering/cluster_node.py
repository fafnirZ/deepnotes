from __future__ import annotations
from dataclasses import dataclass, field
from deepnotes.clustering.file_node import FileNode

@dataclass
class ClusterNode:
    """The intent of these classes are PURELY to persist info
    
    Some higher order being will assign connections to these classes.
    """
    file_node: FileNode

    connections: list[ClusterNode] = field(default_factory=lambda: [])

    def __eq__(self, other: ClusterNode):
        if not isinstance(other, ClusterNode):
            return False
        return self.file_node == other.file_node