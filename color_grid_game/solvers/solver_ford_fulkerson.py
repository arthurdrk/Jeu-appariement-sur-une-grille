import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from color_grid_game import *


class Solver_Ford_Fulkerson(Solver):
    """
    A subclass of Solver that implements a bipartite matching algorithm to find pairs.
    """

    def run(self) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        """
        Runs the bipartite matching algorithm to find pairs of cells.

        Returns
        -------
        list of tuple
            A list of pairs of cells, each represented as a tuple of tuples.
        """
        graph = defaultdict(list)
        even_cells = set()
        odd_cells = set()

        # Add edges between cells (direction: from even to odd)
        for cell1, cell2 in self.grid.all_pairs(self.rules):
            even, odd = (cell1, cell2) if sum(cell1) % 2 == 0 else (cell2, cell1)
            even_cells.add(even)
            odd_cells.add(odd)
            graph[even].append(odd)

        # Add edges from source "s" to even cells
        for even in even_cells:
            graph["s"].append(even)

        # Add edges from odd cells to sink "t"
        for odd in odd_cells:
            graph[odd].append("t")

        # Sets of cells for later extraction of the matching
        self.even_cells = even_cells
        self.odd_cells = odd_cells
        # Get optimal pairs
        self.pairs = self.edmonds_karp(graph, even_cells, odd_cells)
        return self.pairs

    @staticmethod
    def bfs(graph: dict, s: str, t: str) -> dict:
        """
        Performs a BFS to find a path from source 's' to sink 't' in the graph.

        Parameters
        ----------
        graph : dict
            The graph represented as an adjacency list.
        s : str
            The source node.
        t : str
            The sink node.

        Returns
        -------
        dict
            A dictionary of parents for reconstructing the path.
        """
        queue = deque([s])
        parents = {s: None}

        while queue:
            u = queue.popleft()
            for v in graph.get(u, []):
                if v not in parents:
                    parents[v] = u
                    if v == t:
                        return parents
                    queue.append(v)

        return {}

    @classmethod
    def edmonds_karp(cls, graph: dict, even_cells: set, odd_cells: set) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        """
        Computes the maximum flow (maximum matching) in the bipartite graph using the Edmonds-Karp method.

        Parameters
        ----------
        graph : dict
            The graph represented as an adjacency list.

        Returns
        -------
        list of tuple
            The maximum matching as a list of pairs of cells.
        """
        # Validate the input
        if not graph or not even_cells or not odd_cells:
            raise ValueError("Invalid graph or cell sets")

        residual_graph = defaultdict(list)
        for u in graph:
            residual_graph[u] = graph[u][:]

        while True:
            parents = cls.bfs(residual_graph, "s", "t")
            if not parents:
                break

            # Augment the flow along the path found
            path_flow = float('Inf')
            s = "t"
            while s != "s":
                path_flow = min(path_flow, 1)  # Unit capacity
                s = parents[s]

            v = "t"
            while v != "s":
                u = parents[v]
                if u in residual_graph and v in residual_graph[u]:
                    residual_graph[u].remove(v)
                if v not in residual_graph or u not in residual_graph[v]:
                    residual_graph[v].append(u)
                v = u

        return [(u, odd) for odd in odd_cells for u in residual_graph[odd] if u in even_cells]
