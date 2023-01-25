#extraction of university name
def universiteiten(string):
  df_uni = pd.DataFrame()
  for unis in string:
      text=unis
      matchlist = ['Hospital','University','Universitäts','Universität','Università','Hogeschool','Labs', 'Laboratory', 'Zoo','Institute','Institut','School','Ecole','Academy', 'Universite','College','Universitaet,' '* University'] 
      # define all keywords that you need look up
      p = re.compile('^(.*?),\s+(.*?),(.*?)\.')   # regex pattern to match
      # We use a list comprehension using 'any' function to check if any of the item in the matchlist can be found in either group1 or group2 of the pattern match results
      text_match = [m.group(1) if any(x in m.group(1) for x in matchlist) else m.group(2) for m in re.finditer(p,text)]
      df_uni = df_uni.append(text_match, ignore_index=True)
# chatGPT's improvement
import re
import pandas as pd

def universiteiten(string):
    unis = []
    matchlist = ['Hospital','University','Universitäts','Universität','Università','Hogeschool','Labs', 'Laboratory', 'Zoo','Institute','Institut','School','Ecole','Academy', 'Universite','College','Universitaet,' '* University']
    for uni in string:
        match = re.search(', '.join(matchlist), uni)
        if match:
            unis.append(match.group(0))
    df_uni = pd.DataFrame(unis, columns=["University"])
    return df_uni
#This code uses the re.search() function to look for the university name within the input string.
#The search function returns a match object, which includes the matching string, the starting and ending position of the match, and any groups that are defined in the regular expression.
#In this case, if a match is found, it will append the match.group(0) to the unis list.

#Also, it's better to use Pandas Dataframe, to store the university names, rather than using the list and converting it to the dataframe at last.

#You can also add a try-except block to handle cases when no valid university names can be found in the input string.
import re
import pandas as pd

def universiteiten(string):
    try:
        unis = []
        matchlist = ['Hospital','University','Universitäts','Universität','Università','Hogeschool','Labs', 'Laboratory', 'Zoo','Institute','Institut','School','Ecole','Academy', 'Universite','College','Universitaet,' '* University']
        for uni in string:
            match = re.search(', '.join(matchlist), uni)
            if match:
                unis.append(match.group(0))
        df_uni = pd.DataFrame(unis, columns=["University"])
        return df_uni
    except ValueError:
        return None
