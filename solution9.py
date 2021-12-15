heightmap = []
with open("input9.txt") as file:
    for line in file:
        heightmap.append(line.strip())
# print(heightmap)

risk_level_sum = 0
for y, line in enumerate(heightmap):
    for x, point in enumerate(line):
        p = int(point)
        l, r, u, d = [False]*4
        if 0 < x:
            l = p < int(heightmap[y][x-1])            
            # print(p, l, "kleiner als linker Nachbar", int(heightmap[y][x-1]))
        else:
            l = True
            # print("linker Rand")
        if x < len(line) - 1:
            r = p < int(heightmap[y][x+1])
            # print(p, r, "kleiner als rechter Nachbar", int(heightmap[y][x+1]))
        else:
            r = True
            # print("rechter Rand")
        if 0 < y:
            u = p < int(heightmap[y-1][x])
            # print(p, u, "kleiner als oberer Nachbar")
        else:
            u = True
            # print("oberer Rand")
        if y < len(heightmap) - 1:
            d = p < int(heightmap[y+1][x])
            # print(p, d, "kleiner als unterer Nachbar")
        else:
            d = True
            # print("unterer Rand")
        if all([l,r,u,d]):
            risk_level_sum += p+1
print(risk_level_sum)