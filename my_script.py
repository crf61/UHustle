from my_script import listings_from(school)

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

def test_listing_from(school):
    result = listings_from("Georgetown University")
    assert result == ['DJ Service', 'Strawberry Cheesecake', 'Party Planner', 'Fried Conch Dinner', 'Model Headshots', 'Tresure Hunt Set Up']
