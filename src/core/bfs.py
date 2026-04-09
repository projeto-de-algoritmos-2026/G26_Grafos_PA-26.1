from collections import deque

def calcular_bfs(grid, inicio, fim):
    """
    Executa a Busca em Largura (BFS) no mapa.
    :param grid: Matriz MxN contendo objetos TypeTerrain
    :param inicio: Tupla (linha, coluna) de origem
    :param fim: Tupla (linha, coluna) de destino
    :return: Lista de tuplas com o caminho percorrido, ou lista vazia se não achar.
    """
    linhas = len(grid)
    colunas = len(grid[0])
    
    fila = deque([inicio])
    
    visitados = set()
    visitados.add(inicio)
    
    veio_de = {inicio: None}
    
    # movimentos
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while fila:
        atual = fila.popleft()
        
        if atual == fim:
            break
            
        linha_atual, coluna_atual = atual
        
        for dl, dc in direcoes:
            vizinho_linha = linha_atual + dl
            vizinho_coluna = coluna_atual + dc
            vizinho_pos = (vizinho_linha, vizinho_coluna)
            
            # verifica se o vizinho está dentro dos limites do mapa
            if 0 <= vizinho_linha < linhas and 0 <= vizinho_coluna < colunas:
                if vizinho_pos not in visitados:
                    # verifica se não é uma falha na matrix
                    terreno = grid[vizinho_linha][vizinho_coluna]
                    if terreno.name != "Falha na Matrix":
                        fila.append(vizinho_pos)
                        visitados.add(vizinho_pos)
                        veio_de[vizinho_pos] = atual

    caminho = []
    # se o 'fim' está no dicionário, achamos um caminho
    if fim in veio_de:
        passo_atual = fim
        while passo_atual is not None:
            caminho.append(passo_atual)
            passo_atual = veio_de[passo_atual]
        
        caminho.reverse()
        
    return caminho