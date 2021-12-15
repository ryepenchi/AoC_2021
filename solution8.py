data = []
with open("input8.txt") as file:
    for line in file:
        ten_patterns, four_digits = line.strip().split(" | ")
        ten_patterns = [set(sorted(x)) for x in ten_patterns.split()]
        four_digits = [set(sorted(x)) for x in four_digits.split()]
        data.append([ten_patterns, four_digits])
# part 1
# easy_digits = 0
# for line in data:
#     for digit in line[1]:
#         if len(digit) in (2,3,4,7):
#             easy_digits += 1
# print(easy_digits)

# part 2 
output_sum = 0
def get_key(val, mydict):
    for key, value in mydict.items():
        if val == value:
            return key

for line in data:
    # deducing
    digits = {}
    segments = {}
    digits[1] = list(filter(lambda x: len(x) == 2, line[0]))[0]
    digits[7] = list(filter(lambda x: len(x) == 3, line[0]))[0]
    digits[4] = list(filter(lambda x: len(x) == 4, line[0]))[0]
    digits[8] = list(filter(lambda x: len(x) == 7, line[0]))[0]
    segments["a"] = digits[7] - digits[1]
    fiver1, fiver2, fiver3 = list(filter(lambda x: len(x) == 5, line[0]))
    segments["fivers"] = fiver1 & fiver2 & fiver3
    sixer1, sixer2, sixer3 = list(filter(lambda x: len(x) == 6, line[0]))
    segments["sixers"] = sixer1 & sixer2 & sixer3
    segments["d"] = segments["fivers"] - segments["sixers"]
    segments["g"] = segments["fivers"] - segments["a"] - segments["d"]
    digits[0] = digits[8] - segments["d"]
    segments["e"] = digits[8] - digits[4] - segments["fivers"]
    segments["b"] = digits[4] - digits[1] - segments["d"]
    digits[3] = digits[7] | segments["d"] | segments["g"]
    for sixer in [sixer1, sixer2, sixer3]:
        s = digits[1] & sixer
        if len(s) == 1:
            digits[6] = sixer
            segments["f"] = s
    # segments["c"] = digits[1] - segments["f"]
    digits[9] = digits[8] - segments["e"]
    digits[5] = digits[6] - segments["e"]
    digits[2] = digits[8] - segments["b"] - segments["f"]
    # output value
    for base, digit in zip([1000, 100, 10, 1], line[1]):
        output_sum += base * get_key(digit, digits)
print(output_sum)
