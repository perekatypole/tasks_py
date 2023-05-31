import math

R = 10
H = 5
hits = 0
total = 0

for a, v0 in [(30, 100), (45, 150), (60, 200), (75, 250)]:
    t = 2 * v0 * math.sin(math.radians(a)) / 9.8
    R_hit = v0**2 * math.sin(2*math.radians(a)) / 9.8
    if R_hit <= R and H <= v0**2 * math.sin(math.radians(a)) / (2*9.8):
        hits += 1
    total += 1

print("Процент попадания снарядов в цель:", hits / total * 100)