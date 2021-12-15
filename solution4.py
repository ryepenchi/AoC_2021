import itertools

draws = []
boards = []
board = []

with open("input4.txt") as file:
    firstline = False
    for line in file:
        if not firstline:
            draws = [int(x) for x in line.strip().split(",")]
            firstline = True
        else:
            if line == "\n":
                if board:
                    boards.append(board)
                board = []
            else:
                board.append([int(x) for x in line.strip().split()])
# part 1 - answer 8136
# finished = False
# for number in draws:
#     for b in boards:
#         try:
#             i = list(itertools.chain(*b)).index(number)
#             row = i//5
#             col = i%5
#             b[row][col] = -1
#             # print(b)
#             if sum(b[row]) == -5 or sum([r[col] for r in b]) == -5:
#                 boardset = set(list(itertools.chain(*b)))
#                 boardset.remove(-1)
#                 for row in b:
#                     print(row)
#                 print("final score: ",sum(boardset) * number)
#                 finished = True
#                 break
#         except ValueError:
#             pass
#     if finished:
#         break

# part 2 - answer 12738
finishedboards = set()
for number in draws:
    for n, b in enumerate(boards):
        if n not in finishedboards:
            try:
                i = list(itertools.chain(*b)).index(number)
                row = i//5
                col = i%5
                b[row][col] = -1
                if sum(b[row]) == -5 or sum([r[col] for r in b]) == -5:
                    boardset = set(list(itertools.chain(*b)))
                    boardset.remove(-1)
                    finishedboards.add(n)
                    if len(boards) - len(finishedboards) == 0:
                        print("final score: ",sum(boardset) * number)
            except ValueError:
                pass
