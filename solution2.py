# part 2 - answer 1857958050
hor = 0
depth = 0
aim = 0
with open("input2.txt") as file:
    for line in file:
        what, how_much = line.split()
        how_much = int(how_much)
        if what == "forward":
            hor += how_much
            depth += aim * how_much
        elif what == "up":
            aim -= how_much
        elif what == "down":
            aim += how_much
        
print("hor", hor)
print("depth", depth)
print("result", hor*depth)

# part 1 - answer 1693300
# hor = 0
# depth = 0
# with open("input2.txt") as file:
#     for line in file:
#         what, how_much = line.split()
#         how_much = int(how_much)
#         if what == "forward":
#             hor += how_much
#         elif what == "up":
#             depth -= how_much
#         elif what == "down":
#             depth += how_much
        
# print("hor", hor)
# print("depth", depth)
# print("result", hor*depth)