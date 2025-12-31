
from dataclasses import dataclass, field
from pathlib import Path

from deepnotes.clustering.cluster_node import ClusterNode

@dataclass
class Cluster:
    nodes: dict[Path, ClusterNode] = field(default_factory=lambda: dict())


    

