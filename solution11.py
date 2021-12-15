from itertools import chain

def step(octopi):
    octopi = [[x+1 for x in line] for line in octopi]
    boom = any(chain(*[[x>9 for x in line] for line in octopi]))
    if not boom:
        return octopi, 0
    return boom_chain(octopi, 0)

def boom_chain(octopi, flashes):
    boom = any(chain(*[[x>9 for x in line] for line in octopi]))
    if not boom:
        reset_octopi = octopi.copy()
        for y, line in enumerate(octopi):
            for x, octopus in enumerate(line):
                if octopus == -1:
                    reset_octopi[y][x] = 0
        return reset_octopi, flashes
    
    next_octo_step = octopi.copy()
    for y, line in enumerate(octopi):
        for x, octopus in enumerate(line):
            if octopus > 9:
                flashes += 1
                for yy in (y-1, y, y+1):
                    if yy < 0 or yy > len(octopi) - 1:
                        continue
                    for xx in (x-1, x, x+1):
                        if xx < 0 or xx > len(line) - 1:
                            continue
                        # self-reset and increment
                        if yy == y and xx == x:
                            next_octo_step[yy][xx] = -1
                        elif next_octo_step[yy][xx] == -1:
                            continue
                        else:
                            next_octo_step[yy][xx] += 1

    return boom_chain(next_octo_step, flashes)


octopi = []
with open("input11.txt") as file:
    for line in file:
        octopi.append([int(x) for x in line.strip()])

# part 1
# flashes = 0
# [print(line) for line in octopi]
# print()
# for i in range(195):
#     octopi, f = step(octopi)
#     flashes += f
# print("flashes: ", flashes)

# part 2
stepnr = 0
while True:
    octopi, f = step(octopi)
    stepnr += 1
    if f == 100:
        print(stepnr)
        break