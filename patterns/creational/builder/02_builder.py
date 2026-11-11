class NetworkNode:
    def __init__(self):
        self.node_id: str | None = None
        self.encryption_key: str | None = None
        self.connected_nodes: list[NetworkNode] = []

    def __repr__(self) -> str:
        return f'NetworkNode({self.node_id}, key=***, connections={len(self.connected_nodes)})'


class NodeBuilder:
    def __init__(self) -> None:
        self.network_node = NetworkNode()

    def set_id(self, node_id: str) -> 'NodeBuilder':
        self.network_node.node_id = node_id
        return self

    def set_key(self, key: str) -> 'NodeBuilder':
        self.network_node.encryption_key = key
        return self

    def connect_to(self, other_node: NetworkNode) -> 'NodeBuilder':
        self.network_node.connected_nodes.append(other_node)
        return self

    def build(self) -> NetworkNode:
        if self.network_node.node_id is None or self.network_node.encryption_key is None:
            raise ValueError('Идентификатор или ключ шифрования не заданы')
        return self.network_node

    def connect_to_builder(self, other_builder: 'NodeBuilder') -> None:
        node = other_builder.build()
        self.network_node.connected_nodes.append(node)
        return self


if __name__ == '__main__':
    node_id = input()
    encryption_key = input()

    builder = NodeBuilder()
    result_node = builder.set_id(node_id).set_key(encryption_key).build()
