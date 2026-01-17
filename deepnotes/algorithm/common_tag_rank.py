
from deepnotes.clustering.cluster import Cluster


def rank(cluster: Cluster):
    assert cluster.is_locked()
    assert len(cluster.connections) == 0

    for src_node_id, src_node in cluster.nodes.items():
        for dest_node_id, dest_node in cluster.nodes.items():
            if src_node_id == dest_node_id:
                continue

            # interset number of tags
            src_fnode = src_node.file_node
            dest_fnode = dest_node.file_node

            src_tags = src_fnode.tags
            dest_tags = dest_fnode.tags

            common_tags = src_tags.intersect(dest_tags)
            num_common_tags = len(common_tags.tags)

            # bidirectional
            cluster.add_connection(src=src_node_id, dest=dest_node_id, weight=num_common_tags)
            cluster.add_connection(src=dest_node_id, dest=src_node_id, weight=num_common_tags)
