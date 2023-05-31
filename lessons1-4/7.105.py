def check_all_equal_until_negative(lst):
    return len(set(lst)) == 1 or (lst and lst[-1] < 0)