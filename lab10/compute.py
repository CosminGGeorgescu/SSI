p = 14086963408384851001
q = 16670813262138239653
phi = 234841136411758272970005817684311852000
e = 65537

v = 1
while v % e != 0:
    v = v + phi

d = int(v / e)
print(d)
