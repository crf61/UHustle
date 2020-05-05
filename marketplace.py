# marketplace.py

# This is a search engine. 
# This is to determine what products are available to purchase at a certain school location. 
# Right now there are three schools you can choose from; Georgetown University, George Washington University, or American University
# The user can select the school and category they are lookg

def to_usd(my_price):
    return f"${my_price:,.2f}"

if __name__ == "__main__":
    listings = [
        {"id":1, "name": "DJ Service", "school": "Georgetown University", "category": "Entertainment", "Product or Service": "Service", "price": 12.50},
        {"id":2, "name": "StrawberryCheesecake", "school": "George Washington University", "category": "Food/Drink", "Product or Service": "Product", "price": 9.99},
        {"id":3, "name": "Photoshoot Session", "school": "American University", "category": "Media", "Product or Service": "Service", "price": 15.00},

        
    ] # based on listing from UHustle's beta test in 2019

   
    #
    # Info capture / Input
    # 
    total_price = 0
    selected_schools = []
    selected_categories = []

    Name = input("Enter your name: ")
    School = input("Enter your school: ")

    while True:
            selected_category = input("Please enter a category: ") 
            if selected_category == "DONE":
                    break
            else: 
                    selected_categories.append(selected_category) 

    # print(selected_ids)


    import datetime
    x = datetime.datetime.now ()

    for selected_school in selected_schools:
                matching_listings = [p for p in listings if str(p["school"]) == str(selected_school)]
                matching_listing = matching_listings[0]
                total_price = total_price + matching_listing["price"]
                print("SELECTED LISTINGS: " + matching_listing["name"] + " " + str(matching_listing["price"]))  

    taxrate = 0.065
    tax = total_price * taxrate
    sum_total = tax + total_price

    def lookup_listing_by_school(selected_school):
        matching_listings = [p for p in listings if str(p["id"]) == str(selected_id)]
        return matching_products[0]

    price = 0

    print("----------------------------------------")
    print("WELCOME TO UHUSTLE,", Name, "!!")
    print("WE MAKE HUSTLING EASIER.")
    print("----------------------------------------")
    print("Website: TheUHustle.com")
    print ("Date:", x)
    print("----------------------------------------")
    print("Here are the search engine results at", School, ":")
    for selected_listing in selected_listings:
        listing = lookup_listing_by_school(selected_school)
        price += listing["price"]
        price_usd = ' (${0:.2f})'.format(product["price"])
        print(" + " + listing["name"] + price_usd)
    #Christy was unable to figure this out
    print("----------------------------------------")
    print (f"Amount of purchase: {to_usd(total_price)}")
    #calculate tax

    print (f"plus MA Sales Tax (6.25%): {to_usd(tax)}")

    print (f"The total price is:, {to_usd(sum_total)}")
    print("----------------------------------------")

    print(f"Thank you for shopping at Christy's Bodega. Have a wonderful day. I love you")

    #A grocery store name of your choice
    #A grocery store phone number and/or website URL and/or address of choice
    #The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
    #The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
    #The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
    #The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
    #The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
    #A friendly message thanking the customer and/or encouraging the customer to shop again