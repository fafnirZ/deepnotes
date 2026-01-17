

from pathlib import Path
from deepnotes.algorithm.common_tag_rank import rank
from deepnotes.clustering.cluster import Cluster
from deepnotes.clustering.file_node import FileNode
from deepnotes.semantic_tag_gen.extracted_tags import TagList

def test_simple(mocker):

    def noop(self):
        pass
    mocker.patch("deepnotes.clustering.file_node.FileNode.__post_init__", noop)

    file_nodes = [
        ("some/path/a.md", ["tag1", "tag2", "tag3"]),
        ("some/path/b.md", ["tag1"]),
        ("some/path/c.md", ["tag3", "tag2"]),
        ("some/path/d.md", ["tag4", "tag5"]),
        ("some/path/e.md", ["tag4", "tag5"]),
        ("some/path/f.md", ["tag6", "tag6"]),
        ("some/path/g.md", ["tag1", "tag2", "tag3", "tag4"]),
    ]

    fnodes = [
        FileNode(file_path=Path(node[0]), tags=TagList(node[1]))
        for node in file_nodes
    ]

    # add nodes to cluster
    cluster = Cluster()
    for fnode in fnodes:
        cluster.add_node(fnode)
    cluster.lock()
    
    # run algo
    rank(cluster)

    # print cluster
    print(cluster)

    assert False
    