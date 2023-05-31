birth_years = [1985, 1999, 2002, 1978, 2004, 1960, 1992, 1995, 2001, 1975, 1998]
before_1990 = len([y for y in birth_years if y < 1990])
after_2000 = len([y for y in birth_years if y > 2000])
print("Number of people born before 1990:", before_1990)
print("Number of people born after 2000:", after_2000)