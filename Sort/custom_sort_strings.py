from functools import cmp_to_key

words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

# Custom comparator function
# Sorts strings first by length (ascending), then lexicographically if lengths are equal.

def custom_cmp(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

sorted_words = sorted(words, key=cmp_to_key(custom_cmp))
print(sorted_words)