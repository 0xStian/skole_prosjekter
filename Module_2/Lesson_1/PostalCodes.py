"""
Create a script called PostalCodes.py. Create a data structure able to store 10 postal codes with their associated residential areas.
Prompt the user to enter a postal code. If the postal code exists, output the residential area linked to the postal code.
"""

postal_codes = {"0001":"oslo",
                "0002":"stavanger",
                "0003":"Kristiansand",
                "0004":"Bergen"}

selected_postal_code = input("Postal Code: ")

if selected_postal_code in postal_codes:
    print(postal_codes[selected_postal_code])
else:
    print("Invalid Postal Code")