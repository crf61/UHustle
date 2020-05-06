# marketplace.py

# This is a search engine. 
# This is to determine what products are available to purchase at a certain school location. 
# Right now there are three schools you can choose from; Georgetown University, George Washington University, or American University

def to_usd(my_price):
    return f"${my_price:,.2f}"

if __name__ == "__main__":
    listings = [
        {"id":1, "name": "DJ Service", "school": "Georgetown University", "category": "Entertainment", "Product or Service": "Service", "price": 12.50},
        {"id":2, "name": "Strawberry Cheesecake", "school": "Georgetown University", "category": "Food and Drink", "Product or Service": "Product", "price": 9.99},
        {"id":3, "name": "Peach Candy", "school": "George Washington University", "category": "Food and Drink", "Product or Service": "Product", "price": 9.99},
        {"id":4, "name": "Photoshoot Session", "school": "American University", "category": "Media", "Product or Service": "Service", "price": 15.00},
        {"id":5, "name": "Party Planner", "school": "Georgetown University", "category": "Entertainment", "Product or Service": "Service", "price": 7.50},
        {"id":6, "name": "Eyebrow Waxing", "school": "George Washington University", "category": "Beauty", "Product or Service": "Service", "price": 11.99},
        {"id":7, "name": "Books", "school": "American University", "category": "Entertainment", "Product or Service": "Product", "price": 12.10},
        {"id":8, "name": "Fried Conch Dinner", "school": "Georgetown University", "category": "Food and Drink", "Product or Service": "Product", "price": 4.99},
        {"id":9, "name": "Graphic Design: Logo", "school": "American University", "category": "Media", "Product or Service": "Service", "price": 3.00},
        {"id":10, "name": "Videography Session", "school": "George Washington University", "category": "Media", "Product or Service": "Service", "price": 12.00},
        {"id":11, "name": "Wash and Set", "school": "American University", "category": "Beauty", "Product or Service": "Service", "price": 30.00},
        {"id":12, "name": "Dance Performance", "school": "George Washington University", "category": "Entertainment", "Product or Service": "Service", "price": 23.99},
        {"id":13, "name": "Trail Mix", "school": "American University", "category": "Food and Drink", "Product or Service": "Product", "price": 10.45},
        {"id":14, "name": "Private Chef/Caterer", "school": "George Washington University", "category": "Food and Drink", "Product or Service": "Service", "price": 17.89},
        {"id":15, "name": "Model Headshots", "school": "Georgetown University", "category": "Media", "Product or Service": "Service", "price": 5.00},
        {"id":16, "name": "Band Performance", "school": "George Washington University", "category": "Entertainment", "Product or Service": "Service", "price": 9.49},
        {"id":17, "name": "Cotton Candy", "school": "American University", "category": "Food and Drink", "Product or Service": "Product", "price": 5.30},
        {"id":18, "name": "Tresure Hunt Set Up", "school": "Georgetown University", "category": "Entertainment", "Product or Service": "Service", "price": 2.99},
        
    ] 
    total_price = 0
    selected_schools = []
    selected_categories = []
    selected_names = []
   

    First_Name = input("Enter your name: ")
    selected_school = input("Choose from the available schools: Georgetown University, George Washington University, and American University: ")
    
    def listings_from(school):
        return [listings["name"] for listings in listings if listings["school"] == school]
        
    if selected_school == "Georgetown University":
        print("The Available Listings Are: ", listings_from("Georgetown University"))

    if selected_school == "George Washington University":
        print("The Available Listings Are: ", listings_from("George Washington University"))

    if selected_school == "American University":
        print("The Available Listings Are: ", listings_from("American University"))
            
    while True:
            selected_name = input("Choose which listings you would like to purchase from the products listed above. Write DONE when complete. ") 
            if selected_name == "DONE":
                    break
            else: 
                    selected_names.append(selected_name) 

    import datetime
    x = datetime.datetime.now ()

    for selected_name in selected_names:
                matching_listings = [p for p in listings if str(p["name"]) == str(selected_name)]
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

    print("__________________________________________________")
    print("WELCOME TO UHUSTLE,", First_Name, "!!")
    print("WE MAKE HUSTLING EASIER.")
    print("Website: TheUHustle.com")
    print ("Date:", x)
    print("__________________________________________________")
    print("Here are the search engine results at", selected_school, ":")
    for selected_category in selected_categories:
        listing = lookup_listing_by_category(selected_category)
        price += listing["price"]
        price_usd = ' (${0:.2f})'.format(listing["price"])
        print(" + " + listing["name"] + price_usd)
    print("SELECTED LISTINGS: " + matching_listing["name"] + " " + str(matching_listing["price"]))
    print("*************************************************")
    print (f"Amount of purchase: {to_usd(total_price)}")

    print (f"plus MA Sales Tax (6.25%): {to_usd(tax)}")

    print (f"The total price is:, {to_usd(sum_total)}")
    print("__________________________________________________")
    print(f"Thank you for your purchase. Have a nice say and Hustle Hard!")

