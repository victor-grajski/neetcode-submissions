class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True
        for i in range(len(board)):
            rowSet = set()
            for j in range(len(board[i])):
                if board[i][j] != "." and int(board[i][j]):
                    test = int(board[i][j])
                    if test not in rowSet:
                        rowSet.add(test)
                    else:
                        return False
                elif board[i][j] == ".":
                    continue
                else:
                    return False

        for j in range(len(board)):
            colSet = set()
            for i in range(len(board)):
                if board[i][j] != "." and int(board[i][j]):
                    test = int(board[i][j])
                    if test not in colSet:
                        colSet.add(test)
                    else:
                        return False
                elif board[i][j] == ".":
                    continue
                else:
                    return False

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                gridTest = set()
                test = [
                    board[i][j], board[i][j+1], board[i][j+2],
                    board[i+1][j], board[i+1][j+1], board[i+1][j+2],
                    board[i+2][j], board[i+2][j+1], board[i+2][j+2]
                ]
                for elem in test:
                    if elem == ".":
                        continue
                    elif elem not in gridTest:
                        gridTest.add(elem)
                    else:
                        return False


        return isValid
