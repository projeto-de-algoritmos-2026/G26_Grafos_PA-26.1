import heapq
from src.core.constants import TypeTerrain

def get_cheapest_path(
        grid: list[list[TypeTerrain]],
        start_coords: tuple[int, int],
        end_coords: tuple[int, int]
    ) -> list[tuple[int, int]]:

    """
    Executa o algoritmo de Dijkstra usando a adjacência implícita da grid.
    Retorna uma lista de tuplas (linha, coluna) representando o caminho final.
    """

    pq = []
    m, n = len(grid), len(grid[0])

    parent = [-1] * (m * n)
    dist = [[float('inf') for _ in range(n)] for _ in range(m)]
    neighbor_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start_row, start_col = start_coords
    end_row, end_col = end_coords
    dist[start_row][start_col] = 0

    # 1º Ponto de start
    heapq.heappush(pq, (0, start_row, start_col))

    while pq:
        curr_weight, curr_row, curr_col = heapq.heappop(pq)

        # Se chegamos no destino, podemos parar de explorar a grid
        if (curr_row, curr_col) == end_coords:
            break

        # Evitando reprocessamento do mesmo nó
        if curr_weight > dist[curr_row][curr_col]:
            continue

        for offset in neighbor_offsets:
            neighbor_row = curr_row + offset[0]
            neighbor_col = curr_col + offset[1]

            if 0 <= neighbor_row and neighbor_row < m and \
                0 <= neighbor_col and neighbor_col < n:

                weight_terreno = grid[neighbor_row][neighbor_col].weight

                # Se for falha na matrix, pular
                if weight_terreno == float('inf'):
                    continue

                accumulated_weight = curr_weight + weight_terreno

                if accumulated_weight < dist[neighbor_row][neighbor_col]:

                    neighbor_idx = neighbor_row * n + neighbor_col
                    curr_idx = curr_row * n + curr_col

                    parent[neighbor_idx] = curr_idx
                    dist[neighbor_row][neighbor_col] = accumulated_weight

                    heapq.heappush(pq, (accumulated_weight, neighbor_row, neighbor_col))

    # Reconstrução do caminho
    path = []
    curr_idx = end_row * n + end_col

    # Se o parent do nó final continua sendo -1, é porque não achamos saída
    if parent[curr_idx] == -1:
        return []

    while curr_idx != -1:
        r = curr_idx // n
        c = curr_idx % n

        path.append((r, c))
        curr_idx = parent[curr_idx]

    # O caminho é montado do destino pro início, então precisamos inverter
    path.reverse()
    return path