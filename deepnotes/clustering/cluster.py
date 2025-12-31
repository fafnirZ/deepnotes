
from dataclasses import dataclass, field
from pathlib import Path
from typing import Self

from deepnotes.clustering.cluster_node import ClusterNode
from deepnotes.clustering.file_node import FileNode

@dataclass
class Cluster:
    nodes: dict[Path, ClusterNode] = field(default_factory=lambda: dict())

    def add_node(self, node: FileNode) -> Self:
        assert isinstance(node, FileNode)
        file_path = node.file_path
        self.nodes[file_path] = ClusterNode(
            file_node=node,
            connections=[],
        )
        return self
    


