
value = [3, 4, 2, 4, 2 ]

# Solution 1
def find_non_repeating_number(num):
    dict = {}
    for i in num:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for k, v in dict.items():
        if v == 1:
            print(k)

# Solution2
def non_repeating_number(num):
    res = 0
    for i in num:
        res = res ^ i
    print(res)

find_non_repeating_number(value)
non_repeating_number(value)