#original code for guessing date
def guess_date(string):
    for fmt in ["%Y/%m/%d", "%d/%m/%Y", "%d-%m-%Y", "%Y%m%d", "%d.%m.%Y","%Y/%m/%d"]:
        try:
            return datetime.datetime.strptime(string, fmt).date()
        except ValueError:
            continue
    #raise ValueError(string)
    
# chatGPT improving on original function
import dateutil.parser

def guess_date(string):
    date = dateutil.parser.parse(string, fuzzy=True)
    return date.date()

#This code uses the dateutil library's parse function, which is more robust and can handle a wider variety of date formats. 
#The fuzzy=True option allows for more lenient parsing of the input string, which makes it more likely to find a valid date.

#You can also add a try-except block to handle cases when no valid date can be found in the input string.
import dateutil.parser

def guess_date(string):
    try:
        date = dateutil.parser.parse(string, fuzzy=True)
        return date.date()
    except ValueError:
        return None
#This way, you can check if the returned value is None or not, if yes then you can raise ValueError(string) or handle it in any other way you want.
