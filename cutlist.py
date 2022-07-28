#Cut List
#remove all words less than 4 letters long
words = []

with open("engwords.txt") as filein:
    for line in filein:
        line = line.strip()
        if(len(line) >= 4):
            words.append(line)

with open("validwords.txt", 'w') as fileout:
    for item in words:
        fileout.write(item + '\n')

print("Done")