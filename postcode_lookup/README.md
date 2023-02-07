TITLE: postcode_lookup

DESCRIPTION: 
This script firstly tests that the postcode matches one of the acceptable formats.
If the postcode is of an acceptable format it will then split the string at the first number to give the area code (e.g. GU32 3DE = GU)
The area code is then run against the csv file to search the list for the area code.
If the area code is found the script will print the associated area name (e.g. GU32 3DE = GU = Guildford

PACKAGES USED:
re 
pandas

UNIT TESTS:
- test_postcode_lookup
- test_postcode_validation

------------------------------------------------

TITLE: test_postcode_lookup

DESCRIPTION:
This unit test tests the postcode_lookup function using the assertEqual method.

PACKAGES USED:
unittest

------------------------------------------------

TITLE: test_postcode_validation

DESCRIPTION:
This unit test tests the postcode_validation function using the assertTrue method.

PACKAGES USED:
unittest