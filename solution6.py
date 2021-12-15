with open("input6.txt") as file:
    for line in file:
        timers = line.strip().split(",")
fish = {}
for i in range(9):
    fish[i] = timers.count(str(i))
# fish = [int(x) for x in timers]
# step = lambda x: 6 if x == 0 else x - 1 

for _ in range(256):
    offspring = fish[0]
    newfish = {}
    for i in range(8):
        newfish[i] = fish[i+1]
    newfish[6] += fish[0]
    newfish[8] = offspring
    fish = newfish

print(sum(fish.values()))