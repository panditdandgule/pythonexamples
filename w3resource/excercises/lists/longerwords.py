def longer_words(items):
    n = 4
    li = []
    for x in items:
        if len(x) > n:
            li.append(x)

    return li


print("The all words are greater than given number: ", longer_words(['pandit', 'ravi', 'jay', 'bali', 'pratiksha']))
