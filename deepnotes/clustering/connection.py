from dataclasses import dataclass

from deepnotes.clustering.cluster import NodeId


@dataclass
class Connection:
    src: NodeId
    dest: NodeId
    weight: float