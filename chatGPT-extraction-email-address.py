#Extraction e-mail adress
## original code
import re
import pandas as pd
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

## chatGPT improvement
import re
import pandas as pd

def emailadres(string):
    email = []
    for adressen in string:
        # Use the re.findall() function to find all email addresses in the string
        # The regular expression looks for any characters before and after the @ symbol,
        # and any characters after the . in the domain name
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", adressen)
        email.extend(emails)
    # Create a dataframe to store the email addresses
    df_email = pd.DataFrame(email, columns=["Email"])
    return df_email
#This code uses the re.findall() function to extract all email addresses from the input string, rather than just one. 
#The regular expression used in the function is more specific, and will only match email addresses that are formatted correctly.
#Instead of iterating through the list of emails, I used the extend function to add all the emails found to the email list.

#Also, it's better to use Pandas Dataframe, to store the email addresses, rather than using the list and converting it to the dataframe at last.

#You can also add a try-except block to handle cases when no valid email addresses can be found in the input string.
import re
import pandas as pd

def emailadres(string):
    try:
        email = []
        for adressen in string:
            # Use the re.findall() function to find all email addresses in the string
            # The regular expression looks for any characters before and after the @ symbol,
            # and any characters after the . in the domain name
            emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", adressen)
            email.extend(emails)
        # Create a dataframe to store the email addresses
        df_email = pd.DataFrame(email, columns=["Email"])
        return df_email
    except ValueError:
        return None
#This way, you can check if the returned value is None or not, if yes then you can raise ValueError(string) or handle it in any other way you want.
