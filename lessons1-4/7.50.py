num_children = []
for i in range(1, 12):
    num_children.append(int(input(f"How many children in grade {i}? ")))
total_children = sum([num_children[i] for i in range(0, 11, 2)])
print(f"Total number of children in odd-numbered grades: {total_children}")