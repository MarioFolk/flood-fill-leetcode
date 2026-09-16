# Flood Fill – Zadanie (LeetCode 733)

**Popis**  
Máte mriežku `image` veľkosti `m × n`. Dostanete štartovaciu pozíciu `(sr, sc)` a novú farbu `color`.

**Úloha:**  
Prefarbiť celú **spojitú oblasť** začínajúc od `(sr, sc)` 4-smerne a majúcej rovnakú pôvodnú farbu.

**Príklady**  
1. `image = [[1,1,1],[1,1,0],[1,0,1]]`, `sr=1`, `sc=1`, `color=2` → `[[2,2,2],[2,2,0],[2,0,1]]`  
2. `image = [[0,0,0],[0,0,0]]`, `sr=0`, `sc=0`, `color=0` → `[[0,0,0],[0,0,0]]`

**Obmedzenia**  
- `1 ≤ m, n ≤ 50`
