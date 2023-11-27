from .common import *
import networkx as nx


class EfficiencyMeasures(Benchmark):
    params = [(backends), (num_nodes), (edge_prob)]
    param_names = ["backend", "num_nodes", "edge_prob"]

    def time_local_efficiency(self, backend, num_nodes, edge_prob):
        G = cached_gnp_random_graph(num_nodes, edge_prob)
        _ = nx.local_efficiency(G, backend=backend)
