class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def count_parents(graph):
            counts = {node: 0 for node in graph}
            for parent in graph:
                for child in graph[parent]:
                    counts[child] += 1
            return counts
        def topo_sort(graph):
            queue = deque()
            res = []
            counts = count_parents(graph)
            for node in counts:
                if counts[node] == 0:
                    queue.append(node)
            while queue:
                node = queue.popleft()
                res.append(node)
                for child in graph[node]:
                    counts[child] -= 1
                    if counts[child] == 0:
                        queue.append(child)
            return len(res) == numCourses
        
        graph = {t: [] for t in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        return topo_sort(graph)
                
        