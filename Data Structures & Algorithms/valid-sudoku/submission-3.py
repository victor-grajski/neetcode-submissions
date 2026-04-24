class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        boxSets = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in rowSets[i]:
                    rowSets[i].add(board[i][j])
                else:
                    return False
                if board[i][j] not in colSets[j]:
                    colSets[j].add(board[i][j])
                else:
                    return False
                if board[i][j] not in boxSets[i//3][j//3]:
                    boxSets[i//3][j//3].add(board[i][j])
                else:
                    return False

        return isValid
        