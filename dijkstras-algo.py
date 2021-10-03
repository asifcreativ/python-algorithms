# time: O(v^2 + e) | time: O(v)
def dijkstrasAlgorithm(start, edges):
    numberOfNodes = len(edges)

    minDistances = [float("inf") for _ in range(numberOfNodes)]
    minDistances[start] = 0

    visited = set()
    while len(visited) < numberOfNodes:
        vertex, weight = getNotVisitedVertexWithSmallestWeight(
            minDistances, visited)

        if weight == float("inf"):
            break

        visited.add(vertex)

        for negVertex, negWeight in edges[vertex]:
            currentWeight = weight + negWeight
            minDistances[negVertex] = min(
                minDistances[negVertex], currentWeight)

    return [-1 if val == float("inf") else val for val in minDistances]


def getNotVisitedVertexWithSmallestWeight(minDistances, visited):
    vertex = None
    weight = float("inf")

    for vertexIdx in range(len(minDistances)):
        vertexWeight = minDistances[vertexIdx]

        if vertexIdx in visited:
            continue

        if vertexWeight < weight:
            weight = vertexWeight
            vertex = vertexIdx
    return vertex, weight


start = 0
edges = [
    [[1, 7]],
    [[2, 6], [3, 20], [4, 3]], [[3, 14]],
    [[4, 2]],
    [],
    []
]

print(dijkstrasAlgorithm(start, edges))
