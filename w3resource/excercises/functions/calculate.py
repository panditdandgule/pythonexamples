def calculate_string(s):
    upper = 0
    lower = 0
    for w in s:
        if w.isupper():
            upper += 1
        else:
            lower += 1
    print("No. of Upper case characters:", upper)
    print("No. of Lower case characters:", lower)


s = 'The quick Brow Fox'

calculate_string(s)
