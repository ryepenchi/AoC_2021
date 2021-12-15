import numpy as np
from statistics import median, fmean, harmonic_mean, geometric_mean, mean

with open("input7.txt") as file:
    for line in file:
        crabs = line.strip().split(",")
        crabs = [int(x) for x in crabs]

# print("median",median(crabs))
# print("mean", mean(crabs))
# print("fmean", fmean(crabs))
# print("harmonic_mean", harmonic_mean(crabs))
# print(crabs)
# print("geo_mean", geometric_mean(crabs))
m = mean(crabs)
print(m)
m = 464
t = sum([abs(p - m) for p in crabs])
print(t)
# mean = sum(crabs)//len(crabs)
# print("mean: ", mean)
# lowest = 99999999999999999999999999
# finalpos = None
# for r in range(0, max(crabs)):
#     fuel = 0
#     for pos in crabs:
#         fuel += abs(pos - r)
#     if fuel < lowest:
#         lowest = fuel
#         finalpos = pos
# print(finalpos)
# print(lowest)