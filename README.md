# pattern-matching-functions

This code is designed to find specific symbols, extract URLs, guess dates, extract email addresses, and extract university names from a given string of text.

The symbol to be searched for is defined as the variable 'symbol' at the beginning of the code. The function 'find_all' searches for occurrences of this symbol in the given string and appends them to a list called 'acc'. 

The function 'find_url' uses a regular expression to search for and extract URLs from the given string. 

The function 'guess_date' attempts to parse a date from the given string using a variety of different formats. 

The function 'emailadres' uses a regular expression to extract email addresses from the given string and stores them in a dataframe. 

Finally, the function 'universiteiten' searches for keywords related to universities in the given string and stores any matches in a dataframe.

# chat GPT reply on pattern matching symbol on original code snippet
The code you provided appears to be an implementation of a recursive function that finds all occurrences of a given symbol in a string. The function takes four arguments: the symbol to search for, the string to search in, an optional starting index, and an optional accumulator for the found occurrences.

Here are a few suggestions to improve the code:

The acc parameter should be renamed to something more descriptive, such as occurrences. This will make the purpose of the parameter more clear.

Instead of appending the result of string[string.find(symbol, start)+len(symbol):].split()[0:10] to a global list, you can include it as a part of the tuple that is appended to the occurrences list.

You can use the enumerate() function to find the index of the symbol in the string, which eliminates the need for the start parameter.

You can use the return statement to return the final list of occurrences, rather than relying on the global variable test_list. 
