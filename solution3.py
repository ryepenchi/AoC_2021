""" # part 1 - answer 
ones = [0,0,0,0,0,0,0,0,0,0,0,0]
# zeros = [0,0,0,0,0,0,0,0,0,0,0,0]
with open("input3.txt") as file:
    for line in file:
        for i, bit in enumerate(line.strip()):
            if int(bit):
                ones[i] += 1
            # else:
            #     zeros[i] += 1

gamma = ["1" if x > 500 else "0" for x in ones]
gamma = int("".join(gamma),2)
epsilon = gamma ^ 4095
# print(gamma, epsilon)
print("power consumption: ", gamma * epsilon) """

# part 2
o2 = []
co2 = []
values = []
with open("input3.txt") as file:
    for line in file:
        values.append(line.strip())
        
o2 = values.copy()
print(len(list(o2)))
i = 0
while len(o2) > 1:
    ratio = [x[i] for x in o2].count("1") / len(o2)
    if ratio >= 0.5:
        o2 = list(filter(lambda x: bool(int(x[i])), o2))
        print("bit nr", i+1, " .most commcon: 1")
    elif ratio < 0.5:
        o2 = list(filter(lambda x: not bool(int(x[i])), o2))
        print("bit nr", i+1, " .most commcon: 0")
    # else:
    #     o2 = list(filter(lambda x: bool(int(x[i])), o2))
    i += 1
    print("ratio: ", ratio)
    print(o2)
print(int(o2[0],2))
co2 = values.copy()
i = 0
while len(co2) > 1:
    ratio = [x[i] for x in co2].count("1") / len(co2)
    if ratio >= 0.5:
        co2 = list(filter(lambda x: not bool(int(x[i])), co2))
    elif ratio < 0.5:
        co2 = list(filter(lambda x: bool(int(x[i])), co2))
    # else:
    #     co2 = list(filter(lambda x: not bool(int(x[i])), co2))
    i += 1
    print("ratio: ", ratio)
    print(co2)
print(int(co2[0],2))
print("life support rating: ", int(o2[0],2)*int(co2[0],2))