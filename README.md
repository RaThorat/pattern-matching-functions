# pattern-matching-functions

This code is designed to find specific symbols, extract URLs, guess dates, extract email addresses, and extract university names from a given string of text.

The symbol to be searched for is defined as the variable 'symbol' at the beginning of the code. The function 'find_all' searches for occurrences of this symbol in the given string and appends them to a list called 'acc'. 

The function 'find_url' uses a regular expression to search for and extract URLs from the given string. 

The function 'guess_date' attempts to parse a date from the given string using a variety of different formats. 

The function 'emailadres' uses a regular expression to extract email addresses from the given string and stores them in a dataframe. 

Finally, the function 'universiteiten' searches for keywords related to universities in the given string and stores any matches in a dataframe.
