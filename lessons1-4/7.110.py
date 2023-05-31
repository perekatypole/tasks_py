masses = [65, 120, 85, 95, 110]
full_masses = []
other_masses = []

for mass in masses:
    if mass > 100:
        full_masses.append(mass)
    else:
        other_masses.append(mass)

avg_full_mass = sum(full_masses)/len(full_masses)
avg_other_mass = sum(other_masses)/len(other_masses)

print("Average mass of full people:", avg_full_mass)
print("Average mass of other people:", avg_other_mass)