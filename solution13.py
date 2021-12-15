points = []
folds = {"x":[], "y":[]}

with open("input13.txt") as file:
    for line in file:
        l = line.strip()
        if "," in l:
            x,y = l.split(",")
            points.append((int(x), int(y)))
        elif "=" in l:
            if "x" in l:
                folds["x"].append(int(l.split("=")[1]))
            elif "y" in l:
                folds["y"].append(int(l.split("=")[1]))

for xfold in folds["x"]:
    newpoints = []
    print("Folding at x ", xfold)
    for point in points:
        if point[0] > xfold:
            newpoint = (2 * xfold - point[0], point[1])
            newpoints.append(newpoint)
        else:
            newpoints.append(point)
    points = newpoints
for yfold in folds["y"]:
    newpoints = []
    print("Folding at y ", yfold)
    for point in points:
        if point[1] > yfold:
            newpoint = (point[0], 2 * yfold - point[1])
            newpoints.append(newpoint)
        else:
            newpoints.append(point)
    points = newpoints

unique_points = set(points)
plot = []
for y in range(10):
    line = []
    for x in range(40):
        if (x, y) in unique_points:
            line.append("#")
        else:
            line.append(".")
    plot.append(line)

for line in plot:
    print("".join(line))


# print(len(unique_points))
# print(points)
# print(folds)
