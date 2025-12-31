from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Self

from deepnotes.clustering.cluster_node import ClusterNode
from deepnotes.clustering.file_node import FileNode

@dataclass
class Cluster:
    nodes: dict[Path, ClusterNode] = field(default_factory=lambda: dict())
    lock_: bool = field(default=False)

    def add_node(self, node: FileNode) -> Self:
        if self.lock_:
            raise RuntimeError("Cannot add node to a locked cluster")

        assert isinstance(node, FileNode)
        file_path = node.file_path

        if file_path in self.nodes:
            raise RuntimeError("Duplicative FileNode provided.")

        self.nodes[file_path] = ClusterNode(
            file_node=node,
            connections=[],
        )
        return self


    # once locked it will be immutable
    # and you must generate a new cluster.
    def lock(self):
        self._lock = True

    def deep_clone(self) -> Cluster:
        inst = Cluster()
        for node in self.nodes:
            inst.add_node(node)
        return inst
    
    def calculate(self):
        if self._lock:
            raise RuntimeError("Cannot recalculate on a locked cluster.")

        


