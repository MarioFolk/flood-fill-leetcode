# Flood Fill (LeetCode 733)

Jednoduchá implementácia flood fillu (BFS) v Pythone.

## Vlastnosti
- O(E + V) časová zložitosť
- Paint-on-discovery (žiadny extra visited set)
- Early return keď `color == original`

## Použitie
```python
from flood_fill import Solution
sol = Solution()
result = sol.floodFill(image, sr, sc, color)
