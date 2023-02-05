# Imported packages
import re
import pandas


# Read from CSV file
data = pandas.read_csv("postcode_lookup/postcode_towns.csv")


# GLOBALS
POSTCODE_AREAS = data['Postcode_Area'].tolist() # list the postcode areas e.g. GU
POSTCODE_NAMES = data['Postcode_Name'].tolist() # list the postcode area names e.g. Guildford
POSTCODE_TOWNS = data['Postcode_Towns'].tolist() # list the town names 


# Functions
def is_valid(postcode: str) -> bool:
    """
    check if postcode entered matches any of the appropriate formats
    :param postcode: user input postcode
    :return: boolean, True if postcode matches one of the appropriate formats
    """
    postcode = postcode.upper()
    if (re.match("^[A-Z]{2}[0-9]{1}[A-Z]{1} [0-9]{1}[A-Z]{2}$", postcode) # e.g. AA9A 9AA
        or re.match("^[A-Z]{1}[0-9]{1}[A-Z]{1} [0-9]{1}[A-Z]{2}$", postcode) # e.g. A9A 9AA
        or re.match("^[A-Z]{1}[0-9]{1} [0-9]{1}[A-Z]{2}$", postcode) # e.g. A9 9AA
        or re.match("^[A-Z]{1}[0-9]{2} [0-9]{1}[A-Z]{2}$", postcode) # e.g. A99 9AA
        or re.match("^[A-Z]{2}[0-9]{1} [0-9]{1}[A-Z]{2}$", postcode) # e.g. AA9 9AA
        or re.match("^[A-Z]{2}[0-9]{2} [0-9]{1}[A-Z]{2}$", postcode)): # e.g. AA99 9AA
        return True
    else:
        return False


def get_area_name(postcode: str) -> str:
    """
    Gets the area name from the first letter(s) of the postcode e.g. AA,
    and then searches through the list of POSTCODE_AREAS to find a match
    :param: postcode user inputted postcode
    :return: if a match is found it will return the corresponding area name else will return 'Postcode not found'
     """
    postcode = postcode.upper()
    split_postcode = re.split(r'(\d+)', postcode)
    postcode_area = split_postcode[0]
    if postcode_area not in POSTCODE_AREAS:
       return "Postcode not found"
    else:
        postcode_area_index = POSTCODE_AREAS.index(postcode_area)
        return POSTCODE_NAMES[postcode_area_index]
 

# Variables
postcode = "gu32 3de"


# Main code
def main():
    if is_valid(postcode) == False:
        print("Invalid Postcode")
    else:
        postcode_area_name = get_area_name(postcode)
        print(postcode_area_name)


if __name__ == "__main__":
    main()