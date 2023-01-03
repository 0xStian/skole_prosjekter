import requests, os

choice = 0

def dog(dog_name):
    os.system("cls")
    dog_response = requests.get(f"https://api.thedogapi.com/v1/breeds/search?q={dog_name}")
    dog_data = dog_response.json()
    if dog_data != []:
        info = dog_data[0]
        id = dog_data[0]["id"]
        name = info["name"]
        weight = info["weight"]["metric"]
        height = info["height"]["metric"]
        bred_for = info["bred_for"]
        life_span = info["life_span"]
        temperament = info["temperament"]
        try:
            image_url = requests.get(f"https://api.thedogapi.com/v1/images/search?breed_ids={id}")
            image = image_url.json()[0]["url"]
            os.popen(f"start {image}")
        except:
            print("No image found.")
        return f"\nName: {name}\nWeight: {weight}\nHeight: {height}\nBred for: {bred_for}\nLife span: {life_span}\nTemperament: {temperament}\n"
    else:
        return "No dog found."


def cat(cat_name):
    os.system("cls")
    cat_response = requests.get(f"https://api.thecatapi.com/v1/breeds/search?q={cat_name}")
    cat_data = cat_response.json()
    if cat_data != []:
        id = cat_data[0]["id"]
        info = cat_data[0]
        name = info["name"]
        weight = info["weight"]["metric"]
        temperament = info["temperament"]
        origin = info["origin"]
        description = info["description"]
        indoor = info["indoor"]
        wikipedia_url = info["wikipedia_url"]
        try:
            image_url = requests.get(f"https://api.thecatapi.com/v1/images/search?breed_ids={id}")
            image = image_url.json()[0]["url"]
            os.popen(f"start {image}")
        except:
            print("No image found.")
        return f"\nName: {name}\nWeight: {weight}\nTemperament: {temperament}\nOrigin: {origin}\nDescription: {description}\nIndoor: {indoor}\nWiki: {wikipedia_url}\n"
    else:
        return "No cat found."
        
        
def menu():
    os.system("cls")
    print("\n1. Dog information.")
    print("2. Cat information.")
    print("3. Exit.")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            print(dog(input("Enter dog name: ")))
            input("\nPress enter to continue...")
            menu()
        case "2":
            print(cat(input("Enter cat name: ")))
            input("\nPress enter to continue...")
            menu()
        case "3":
            print("Goodbye!\n")
            exit()
        case _:
            print("Invalid choice.")
            input("\nPress enter to continue...")
            menu()
       
       
menu()