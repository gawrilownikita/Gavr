
f = open("Telnum.txt", "r")

lines = f.read().splitlines()
f.close()
answer = []
for i in lines:
    lc = 2
    if len(i) > 12:
        lc = len(i) - 10
    rc = lc + 3
    answer.append("+1 (" + i[lc:rc] + ") " + i[rc:])



fw = open ("Answer.txt", "w")
for i in answer:
    fw.write(str(i) + "\n")
fw.close()