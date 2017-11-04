import sys
from collections import defaultdict


class Graph:
    def __init__(self, filename=None, delimiter=None):
        self._adj = defaultdict(set)
        self._nb_edges = 0
        with open(filename) as graph_file:
            for line in graph_file:
                vertices = line.strip().split(delimiter)
                me = vertices[0]
                for neigh in vertices[1:]:
                    self += (me, neigh)

    @property
    def nb_vertex(self):
        return len(self._adj)

    @property
    def nb_edges(self):
        return self._nb_edges

    def neighbours_of(self, v):
        yield from self._adj[v]

    def has_vertex(self, v):
        return v in self._adj

    def has_edge(self, v, w):
        return w in self._adj[v]

    def add_edge(self, v, w):
        # if not self.has_edge(v, w):
        if (v, w) not in self:
            self._adj[v].add(w)
            self._adj[w].add(v)

    def vertices(self):
        yield from self._adj

    def degree(self, v):
        return len(self._adj[v])

    def __iadd__(self, tup):
        v, w = tup
        self.add_edge(v, w)
        return self

    def __iter__(self):
        seen = set()
        for v in self.vertices():
            for neigh in self.neighbours_of(v):
                seen.add((v, neigh))
                if (neigh, v) in seen:
                    continue
                yield v, neigh

    def __str__(self):
        return str(tuple(self))

    def __contains__(self, x):
        if isinstance(x, tuple):
            return self.has_edge(*x)
        return self.has_vertex(x)

    def gen_graphviz(self):
        res = "graph G{\n"
        for tup in self:
            res += '\t'
            u, v = tup
            res += '"%s" -- "%s"' % (u, v)
        return res + '}'


def main():
    filename = sys.argv[1]
    graph = Graph(filename)
    print(graph)
    with open('graphviz.txt', 'w') as out:
        out.write(graph.gen_graphviz())
    print('A' in graph, 'Z' in graph)
    print(('A', 'B') in graph, ('G', 'H') in graph)
    for w in graph.neighbours_of('A'):
        print(w)


if __name__ == "__main__":
    main()
