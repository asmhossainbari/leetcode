from functools import cmp_to_key

numbers = [5, -3, 4, -5, 3]

# Custom comparator function
# This comparator sorts numbers by their absolute value in ascending order.
# For numbers with the same absolute value, it places negatives before positives.

def custom_cmp(a, b):
    abs_a = abs(a)
    abs_b = abs(b)
    if abs_a < abs_b:
        return -1
    elif abs_a > abs_b:
        return 1
    else:
        if a < 0 and b > 0:
            return -1
        elif a > 0 and b < 0:
            return 1
        else:
            return 0
        
sorted_numbers = sorted(numbers, key=cmp_to_key(custom_cmp))
# sorted_numbers = sorted(numbers)
print(sorted_numbers)