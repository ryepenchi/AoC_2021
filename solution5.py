from collections import defaultdict
points = defaultdict(lambda: 0)
vent_lines = []
with open("input5.txt") as file:
    for line in file:
        start, end = line.strip().split(" -> ")
        start_x, start_y = start.split(",")
        end_x, end_y = end.split(",")
        vent_lines.append(((int(start_x), int(start_y)), (int(end_x), int(end_y))))

# part 1 - answer 7318
f = lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1]
only_hor_ver = list(filter(f, vent_lines))

for vent_line in only_hor_ver:
    xes = sorted([vent_line[0][0], vent_line[1][0]])
    for x in range(xes[0], xes[1] + 1):
        yes = sorted([vent_line[0][1], vent_line[1][1]])
        for y in range(yes[0], yes[1] + 1):
            points[(x,y)] += 1

# part 2 - answer 19939
f = lambda x: not (x[0][0] == x[1][0] or x[0][1] == x[1][1])
only_diag = list(filter(f, vent_lines))
for vent_line in only_diag:
    if vent_line[0][0] < vent_line[1][0]:
        x_range = range(vent_line[0][0], vent_line[1][0] + 1)
    else:
        x_range = range(vent_line[0][0], vent_line[1][0] - 1, - 1)
    if vent_line[0][1] < vent_line[1][1]:
        y_range = range(vent_line[0][1], vent_line[1][1] + 1)
    else:
        y_range = range(vent_line[0][1], vent_line[1][1] - 1, - 1)
    for x,y in zip(x_range, y_range):
        points[(x,y)] += 1




at_least_two = {k:v for (k,v) in points.items() if v > 1}
print("len: ", len(at_least_two))
