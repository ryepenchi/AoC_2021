from statistics import median

topf_und_deckel = {")":"(", "]":"[", "}":"{", ">":"<"}
error_scores = {")":3, "]":57, "}":1197, ">":25137}
autocomplete_scores = {"(":1, "[":2, "{":3, "<":4}
score = 0
bscores = []
with open("input10.txt") as file:
    for line in file:
        opened_chunks = {"(":0, 
                    "[":0,
                    "{":0,
                    "<":0}
        closed_chunks = opened_chunks.copy()
        line = line.strip()
        # print(line)
        currupted = False
        blinescore = 0
        last_opened = ""
        for char in line:
            if char in "([{<":
                last_opened += char
                # print(last_opened)
                opened_chunks[char] += 1
            elif topf_und_deckel[char] != last_opened[-1]:
                score += error_scores[char]
                corrupted = True
                # print("error", error_scores[char])
                break
            else:
                last_opened = last_opened[:-1]
                # print(last_opened)
        if not currupted:
            for opened in last_opened[::-1]:
                blinescore *= 5
                blinescore += autocomplete_scores[opened]
                bscores.append(blinescore)
    print(score)
    print(median(bscores))
