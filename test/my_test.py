from app.my_script import listings_from

def test_listing_from():
    result = listings_from("Georgetown University")
    assert result == ['DJ Service', 'Strawberry Cheesecake', 'Party Planner', 'Fried Conch Dinner', 'Model Headshots', 'Tresure Hunt Set Up']
