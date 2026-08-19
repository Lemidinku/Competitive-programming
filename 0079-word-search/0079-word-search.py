class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m , n = len(board), len(board[0])
        dir = [[0,1], [0,-1], [1, 0], [-1,0]]

        def is_inbound(r,c):
            return 0<= r < m and 0<= c < n

        def search(word, r, c, visited):
            if board[r][c] != word[0]:
                return False
            if len(word)==1:
                return True

            visited.add((r,c))
            found = False

            for x,y in dir:
                new_r, new_c = r+x, c+y
                if is_inbound(new_r, new_c) and (new_r, new_c) not in visited:
                    found |= search(word[1:], new_r, new_c, visited)
            visited.remove((r,c))


            return found

        
        for r in range(m):
            for c in range(n):
                if search(word, r,c, set()):
                    return True
        return False