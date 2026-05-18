from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
        queue = deque([0])  
        visited = {0}     
        steps = 0

        while queue:
            for _ in range(len(queue)):
                curr_idx = queue.popleft()
                if curr_idx == n - 1:
                    return steps
                
                val = arr[curr_idx]
                for neighbors in graph[val]:
                    if neighbors not in visited:
                        visited.add(neighbors)
                        queue.append(neighbors)
                
                graph[val].clear()
                
                if curr_idx - 1 >= 0 and (curr_idx - 1) not in visited:
                    visited.add(curr_idx - 1)
                    queue.append(curr_idx - 1)

                if curr_idx + 1 < n and (curr_idx + 1) not in visited:
                    visited.add(curr_idx + 1)
                    queue.append(curr_idx + 1)
            
            steps += 1
            
        return -1
