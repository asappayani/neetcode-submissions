from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        REVISIT LATER B/C I HAD TO USE HINT

        idea: use hashmap, have key as the num and the values as all the positions (i, j) where that
        num can be found

        1: [(0,0), (4,7)]

        for each number in the hashmap
            if position list length <= 1 then continue
            else
                rowseen = set()
                colseen = set()
                boxseen = set()
                for each position with that number
                    if the positions row/col has been seen then false
                    *FROM HINT* if (row // 3, col // 3) in boxseen then false

                    otherwise 
                    add row to rowseen
                    add col to colseen
                    add current box to boxseen
        
        return true
        """
        hashmap = defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != ".":
                    hashmap[board[r][c]].append((r,c))

        for key in hashmap:
            if len(hashmap[key]) <= 1: 
                continue
            
            rowseen = set()
            colseen = set()
            boxseen = set()

            for pos in hashmap[key]:
                row, col = pos

                if row in rowseen or col in colseen:
                    return False
                
                if (row // 3, col // 3) in boxseen:
                    return False

                rowseen.add(row)
                colseen.add(col)
                boxseen.add((row // 3, col // 3))
            
        return True
        

        

