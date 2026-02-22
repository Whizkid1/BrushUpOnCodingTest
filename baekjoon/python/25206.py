grade_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
tg = 0
tc = 0
for i in range(20):
    s, c, g = input().split()
    if str(g) == "P":
        continue
    tg += float(c) * grade_dict[str(g)]
    tc += float(c)
print(tg/tc)