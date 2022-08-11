#To find particular symbol in a text

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
  
#Extracting hyperlinks from pdfs
#https://www.tutorialspoint.com/extract-hyperlinks-from-pdf-in-python
def find_url(string):
  #Find all the String that matches with the pattern
  regex = r"(https?://\S+)"
  url = re.findall(regex,string)
  for url in url:
     return url
    
#guessing date
def guess_date(string):
    for fmt in ["%Y/%m/%d", "%d/%m/%Y", "%d-%m-%Y", "%Y%m%d", "%d.%m.%Y","%Y/%m/%d"]:
        try:
            return datetime.datetime.strptime(string, fmt).date()
        except ValueError:
            continue
    #raise ValueError(string)
    
#Extraction e-mail adress
def emailadres(string):
  df_email = pd.DataFrame()
  email=[]
  for adressen in string:
      # \w matches any non-whitespace character
      # @ for as in the Email
      # + for Repeats a character one or more times
      FindEmail = re.findall("([\w.-]+@[\w.-]+)", adressen)
      # run for loop on the list variable
      for l in FindEmail:
      #set value in email variable
          emaill=l
      #declare local variables to store email addresses
      email.append(emaill)
  df_email['Email']=email

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
