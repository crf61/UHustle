# marketplace.py

# This is a search engine. 
# This is to determine what products are available to purchase at a certain school location. 
# Right now there are three schools you can choose from; Georgetown University, George Washington University, or American University

def to_usd(my_price):
    return f"${my_price:,.2f}"

if __name__ == "__main__":
    listings = [
        {"id":1, "name": "DJ Service", "school": "Georgetown University", "category": "Entertainment", "Product or Service": "Service", "price": 12.50},
        {"id":2, "name": "StrawberryCheesecake", "school": "George Washington University", "category": "Food/Drink", "Product or Service": "Product", "price": 9.99},
        {"id":2, "name": "Strawberry Cheesecake", "school": "George Washington University", "category": "Food and Drink", "Product or Service": "Product", "price": 9.99},
        {"id":3, "name": "Photoshoot Session", "school": "American University", "category": "Media", "Product or Service": "Service", "price": 15.00},
        {"id":4, "name": "Party Planner", "school": "Georgetown University", "category": "Entertainment", "Product or Service": "Service", "price": 7.50},
        {"id":5, "name": "Eyebrow Waxing", "school": "George Washington University", "category": "Beauty", "Product or Service": "Service", "price": 11.99},
        {"id":6, "name": "Books", "school": "American University", "category": "Entertainment", "Product or Service": "Product", "price": 12.10},
        {"id":7, "name": "Fried Conch Dinner", "school": "Georgetown University", "category": "Food/Drink", "Product or Service": "Product", "price": 4.99},
        {"id":8, "name": "Graphic Design: Logo", "school": "American University", "category": "Media", "Product or Service": "Service", "price": 3.00},
        {"id":9, "name": "Videography Session", "school": "George Washington University", "category": "Media", "Product or Service": "Service", "price": 12.00},
        {"id":10, "name": "Wash and Set", "school": "American University", "category": "Beauty", "Product or Service": "Service", "price": 30.00},
        {"id":11, "name": "Dance Performance", "school": "George Washington University", "category": "Entertainment", "Product or Service": "Service", "price": 23.99},
        {"id":12, "name": "Trail Mix", "school": "American University", "category": "Food and Drink", "Product or Service": "Product", "price": 10.45},
        {"id":13, "name": "Private Chef/Caterer", "school": "George Washington University", "category": "Food and Drink", "Product or Service": "Service", "price": 17.89},
        {"id":14, "name": "Model Headshots", "school": "Georgetown University", "category": "Media", "Product or Service": "Service", "price": 5.00},
        {"id":15, "name": "Band Performance", "school": "George Washington University", "category": "Entertainment", "Product or Service": "Service", "price": 9.49},
        {"id":16, "name": "Cotton Candy", "school": "American University", "category": "Food and Drink", "Product or Service": "Product", "price": 5.30},
        {"id":17, "name": "Tresure Hunt Set Up", "school": "Georgetown University", "category": "Entertainment", "Product or Service": "Service", "price": 2.99},
        {"id":18, "name": "Facial", "school": "Georgetown University", "category": "Beauty", "Product or Service": "Service", "price": 74.99},

        ] # based on listing from UHustle's beta test in 2019

   
    #
    # Info capture / Input
    # 
    total_price = 0
    selected_schools = []
    selected_categories = []

    Name = input("Enter your name: ")
  
    while True:
            selected_school = input("Choose from the available schools: Georgetown University, George Washington University, and American University: ") 
            if selected_school == "DONE":
                    break
            else: 
                    selected_schools.append(selected_school) 

    for selected_school in selected_schools:
                matching_selections = [p for p in listings if str(p["school"]) == str(selected_school)]
                matching_selection = matching_selections[0]
                print("SELECTED LISTINGS: " + matching_selection["name"] + " " + str(matching_selection["id"]))  
   
    while True:
            selected_category = input("Choose from the available listings from the ids listed above: ") 
            if selected_category == "DONE":
                    break
            else: 
                    selected_categories.append(selected_category) 


    import datetime
    x = datetime.datetime.now ()

    for selected_category in selected_categories:
                matching_listings = [p for p in listings if str(p["category"]) == str(selected_category)]
                matching_listing = matching_listings[0]
                total_price = total_price + matching_listing["price"]
                print("SELECTED LISTINGS: " + matching_listing["name"] + " " + str(matching_listing["price"]))  

    taxrate = 0.065
    tax = total_price * taxrate
    sum_total = tax + total_price

    def lookup_listing_by_category(selected_category):
        matching_listings = [p for p in listings if str(p["category"]) == str(selected_category)]
        return matching_listings[0]

    price = 0

    print("----------------------------------------")
    print("WELCOME TO UHUSTLE,", Name, "!!")
    print("WE MAKE HUSTLING EASIER.")
    print("----------------------------------------")
    print("Website: TheUHustle.com")
    print ("Date:", x)
    print("----------------------------------------")
    print("Here are the search engine results at", selected_school, ":")
    for selected_category in selected_categories:
        listing = lookup_listing_by_category(selected_category)
        price += listing["price"]
        price_usd = ' (${0:.2f})'.format(listing["price"])
        print(" + " + listing["name"] + price_usd)
    #Christy was unable to figure this out
    print("----------------------------------------")
    print (f"Amount of purchase: {to_usd(total_price)}")
    #calculate tax

    print (f"plus MA Sales Tax (6.25%): {to_usd(tax)}")

    print (f"The total price is:, {to_usd(sum_total)}")
    print("----------------------------------------")

    print(f"Thank you for your purchase. Hustle Hard!")

    #A grocery store name of your choice
    #A grocery store phone number and/or website URL and/or address of choice
    #The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
    #The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
    #The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
    #The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
    #The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
    #A friendly message thanking the customer and/or encouraging the customer to shop again