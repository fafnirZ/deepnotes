from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from deepnotes.clustering.cluster import NodeId

@dataclass
class Connection:
    src: NodeId
    dest: NodeId
    weight: float