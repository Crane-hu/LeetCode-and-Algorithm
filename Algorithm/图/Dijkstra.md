在图相关的问题中，有一种问题是寻找最短路径，即从一个节点出发，判断多久能到达所有路径，除了广度优先搜索以外，最高效的莫过于**Dijkstra**算法

## 核心思想

```
算法的核心思想是贪心+广度优先搜索，可以理解为是对广度优先搜索的优化。
每次更新一个离初始点源最近的节点作为新的点源并将此点进行标记，再以这个点源为中心搜索离其最近的节点，依次更新遍历，直到图中的节点被全部标记
```

## 代码

```python
import heapq
from typing import Dict


def init_distance(graph: Dict, s: str) -> Dict:
    distance = {s: 0}
    for v in graph:
        if v != s:
            distance[v] = float('inf')
    return distance

def dijkstra(graph: Dict, s: str) -> (Dict, Dict):
    pq = []
    heapq.heappush(pq, (0, s))
    visited = set()
    visited.add(s)
    parent = {s: None}
    distance = init_distance(graph, s)

    while (len(pq) > 0):
        pair = heapq.heappop(pq)
        dist, vertex = pair[0], pair[1]
        visited.add(vertex)
        nodes = graph[vertex]
        for w in nodes:
            if w not in visited:
                if dist + nodes[w] < distance[w]:
                    heapq.heappush(pq, (dist + nodes[w], w))
                    distance[w] = dist + nodes[w]
                    parent[w] = vertex
    return parent, distance


if __name__ == '__main__':
    graph = {
        "A": {"B": 5, "C": 1},
        "B": {"A": 5, "C": 2, "D": 1},
        "C": {"A": 1, "B": 2, "D": 4, "E": 8},
        "D": {"B": 1, "C": 4, "E": 3, "F": 6},
        "E": {"C": 8, "D": 3},
        "F": {"D": 6},
    }
    print(dijkstra(graph, "A"))
```
