#original code to find particular symbol in a text

symbol='☒'    
test_list=[]
def find_all(symbol, # string pattern
             string, # string to be searched
             start=0, # ignore everything before start
             acc=[]# All occurrences of string pattern in string
            ): #all patterns
    # Find next occurrence of pattern in string
    

    i = string.find(symbol, start)
    test_str = string[string.find(symbol, start)+len(symbol):].split()[0:10]
    #print(test_str)
    test_list.append(test_str)

    if i == -1:
        # Pattern not found in remaining string
        return acc
        # Appending String to list
    # using + operator + list conversion
    #test_list += [test_str]
    n=len(test_list)

    return find_all(symbol, string, start = i+1,
                    acc = acc + [(symbol, i)]) # Pass new list with found pattern

# chatGPT's improvement on finding symbol in text
def find_all(symbol, string):
    occurrences = []
    for i, char in enumerate(string):
        if char == symbol:
            next_10 = string[i+len(symbol):].split()[:10]
            occurrences.append((symbol, i, next_10))
    return occurrences
#Note: This implementation will not handle the case where the input is a symbol that could be part of an emojis,
#you will have to use some library to handle this case like "emoji" library.
