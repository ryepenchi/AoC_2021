# part 2 - answer 1618
tally = 0
previous = 999_999_999
singles = []
with open("input1.txt") as file:
    for line in file:
        singles.append(int(line.strip()))
triples = list(map(sum, zip(singles, singles[1:], singles[2:])))
for value in triples:
    if value > previous:
        tally += 1
    previous = value

print("increases: ", tally)

# part 1 - answer 1581
# tally = 0
# previous = 999_999_999
# with open("input1.txt") as file:
#     for line in file:
#         current = int(line.strip())
#         if current > previous:
#             tally += 1
#         previous = current
# print("increases: ", tally)
