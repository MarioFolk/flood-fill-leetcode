from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]:
            return image

        rows, cols = len(image), len(image[0])
        original = image[sr][sc]

        if original == color:
            return image

        q = deque([(sr, sc)])
        image[sr][sc] = color

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                    image[nr][nc] = color
                    q.append((nr, nc))
        return image


if __name__ == "__main__":
    sol = Solution()
    img1 = [[1,1,1],[1,1,0],[1,0,1]]
    print(sol.floodFill(img1, 1, 1, 2))

    img2 = [[0,0,0],[0,0,0]]
    print(sol.floodFill(img2, 0, 0, 0))
