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
# chat GPT reply on pattern matching symbol on original code snippet
#The code you provided appears to be an implementation of a recursive function that finds all occurrences of a given symbol in a string. 
#The function takes four arguments: the symbol to search for, the string to search in, an optional starting index, and an optional accumulator for the found occurrences.

#Here are a few suggestions to improve the code:

#The acc parameter should be renamed to something more descriptive, such as occurrences. This will make the purpose of the parameter more clear.
#Instead of appending the result of string[string.find(symbol, start)+len(symbol):].split()[0:10] to a global list, you can include it as a part of the tuple that is appended to the occurrences list.
#You can use the enumerate() function to find the index of the symbol in the string, which eliminates the need for the start parameter.
#You can use the return statement to return the final list of occurrences, rather than relying on the global variable test_list. 

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
