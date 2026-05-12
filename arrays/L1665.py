'''
Problem : Minimum Initial Energy to Finish Tasks
Platform: LeetCode (1665)
Difficulty: hard    
Approach: Greedy Sorting + Iteration
Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) for in-place sorting and constant extra space

'''
class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        total_energy = 0
        current_energy = 0
        
        for actual, minimum in tasks:
            if current_energy < minimum:
                total_energy += (minimum - current_energy)
                current_energy = minimum
            current_energy -= actual
            
        return total_energy
