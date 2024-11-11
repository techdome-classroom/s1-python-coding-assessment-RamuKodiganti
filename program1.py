class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def dfs(r, c):
            # Base case: return if out of bounds or on a water cell
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            # Mark the cell as visited by changing it to 'W'
            grid[r][c] = 'W'
            # Visit neighboring cells (up, down, left, right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        # Iterate through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':  # Found an unvisited landmass
                    island_count += 1
                    dfs(r, c)  # Start a DFS to mark the entire island

        return island_count

# Example usage:
solution = Solution()

grid1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"]
]
grid2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"]
]

print(solution.getTotalIsles(grid1))  # Output: 1
print(solution.getTotalIsles(grid2))  # Output: 3
