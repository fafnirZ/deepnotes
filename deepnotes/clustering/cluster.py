from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Self

from deepnotes.clustering.cluster_node import ClusterNode
from deepnotes.clustering.connection import Connection
from deepnotes.clustering.file_node import FileNode, NodeId



# TODO implement connection

@dataclass
class Cluster:
    nodes: dict[NodeId, ClusterNode] = field(default_factory=lambda: dict())
    connections: dict[NodeId, Connection] = field(default_factory=lambda: dict())

    # aux
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
        )
        return self


    # once locked it will be immutable
    # and you must generate a new cluster.
    def lock(self):
        self._lock = True

    def deep_clone(self) -> Cluster:
        inst = Cluster()
        for id, node in self.nodes.items():
            inst.add_node(node.file_node)
        return inst
    
    def calculate(self):
        if self._lock:
            raise RuntimeError("Cannot recalculate on a locked cluster.")

        


