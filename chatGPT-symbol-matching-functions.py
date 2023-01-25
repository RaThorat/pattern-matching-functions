#finding symbol in text
def find_all(symbol, string):
    occurrences = []
    for i, char in enumerate(string):
        if char == symbol:
            next_10 = string[i+len(symbol):].split()[:10]
            occurrences.append((symbol, i, next_10))
    return occurrences
#Note: This implementation will not handle the case where the input is a symbol that could be part of an emojis,
#you will have to use some library to handle this case like "emoji" library.
