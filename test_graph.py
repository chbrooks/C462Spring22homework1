import  graph2

def test_graph():
    test_add_node()
    test_add_edge()
    test_get_edges()


def test_add_node():
    g = graph2.Graph()
    g.add_node(1)
    assert 1 in g


def test_add_edge():
    g  = graph2.Graph()
    g.add_edge(1,2,1)
    assert 1 in g and 2 in g and len(g.edgeMap[1]) > 0


def test_get_edges():
    g = graph2.Graph()
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 1)
    result = g.get_edges(1)
    print(result)
    assert len(result) == 2
