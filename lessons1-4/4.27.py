x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())

x_min = min(x1, x2)
y_min = min(y1, y2)
x_max = max(x1 + w1, x2 + w2)
y_max = max(y1 + h1, y2 + h2)

print(x_min, y_min, x_max - x_min, y_max - y_min)