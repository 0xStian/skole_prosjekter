"""
1. Define a dictionary consisting of 5 business names and their associated phone numbers.  The business name should be used as the key. 
2. Request the name and number of another business from the user and add it to the dictionary. 
3. Ask the user to type in the name of a business.  If the business exists, display its phone number; otherwise display the message “The business is not in the phonebook.”. 
4. Display the entire dictionary (names and phone numbers). 
5. Display only the business names (no phone numbers). 
"""

businesses = {
    "Apple": "89382736",
    "Samsung": "43829174",
    "Ikea": "49382740",
    "Rema1000": "10548394",
    "Kiwi": "19374859"
}

businesses.update({input("Business name: "):input("Phone number: ")})
search_for_business = input("search for business: ")

if search_for_business in businesses:
    print(f"The phone number of {search_for_business} is {businesses[search_for_business]}")
    print (f"Keys & Values: {businesses}")
    ### Alternative ###
    #for key, value in businesses.items():
    #    print(f"{key}:{value},", end=' ')
    #print("\n")
    print (f"only Keys: {businesses.keys()}")
    ### Alternative ###
    #for key in businesses:
    #    print(f"{key},", end=' ')
else:
    print("The business is not in the phonebook.")
