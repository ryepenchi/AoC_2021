from itertools import chain, count
from collections import defaultdict
rules = {}
with open("input14.txt") as file:
    # template = [x for x in file.readline().strip()]
    template = file.readline().strip()
    _ = file.readline()
    for line in file:
        k, v = line.strip().split(" -> ")
        rules[k] = v

print(template)
# part 2
paircount = defaultdict(lambda: 0)
for i in range(len(template)-1):
    paircount[template[i:i+2]] += 1

def step(paircountdict, steps):
    for i in range(steps):
        pairs = list(paircountdict.keys())
        loopcountdict = paircountdict.copy()
        for pair in pairs:
            paircountdict[pair] -= loopcountdict[pair]
            firstnew = pair[0] + rules[pair]
            secondnew = rules[pair] + pair[1]
            paircountdict[firstnew] += loopcountdict[pair]
            paircountdict[secondnew] += loopcountdict[pair]
    return paircountdict
            
result = step(paircount, 40)
# print(result)
elements = set(chain(*[x for x in rules]))
elementcount = defaultdict(lambda: 0)
for e in elements:
    for pair in result:
        if pair.count(e) == 1:
            elementcount[e] += result[pair] /2
        elif pair.count(e) == 2:
            elementcount[e] += result[pair]
    if e == template[0] or e == template[-1]: # die fälschlicherweise geteilten Randpunkte wieder dazurechnen
        elementcount[e] += 0.5

print(elementcount)
print(max(elementcount.values())-min(elementcount.values()))
for k, v in sorted(elementcount.items(), key=lambda x: x[1], reverse=True):
    print(k, str(v).rjust(15))
# not 2914365137497
# answer 2914365137499 (#2 from calculated answer, why?)


# part 1 slow
# def step(polymer):
#     new_polymer = []
#     for i in range(len(polymer) - 1):
#         new_polymer.append(polymer[i])
#         new_polymer.append(rules["".join(polymer[i:i+2])])
#     new_polymer.append(polymer[-1])
#     return new_polymer

# elements = set(chain(*[x for x in rules]))

# for i in range(10):
#     new_template = step(template)
    
#     template = new_template
#     # print(template)

# counts = {template.count(e):e for e in elements}
# # most_common = counts[max(counts)]
# # least_common = counts[min(counts)]
# # print(most_common, least_common)
# print("diff: ", max(counts) - min(counts) )
# print(counts)
# # print(len(template))
# # print(template)