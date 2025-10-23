# =============== Cafe Management System===============

menu = {
    "Zinger Roll": 300,
    "Chicken Roll": 200,
    "Chicken Burger": 450,
    "Chicken Sandwich": 350,
    "Chicken Nuggets": 250, 
    "Chicken Wings": 400,
    "Chicken Shawarma": 500,
    "Chicken Biryani": 600,
    "Chicken Karahi": 700,
    "Chicken Tikka": 550,
    "Beef Burger": 500,
    "Beef Shawarma": 600,
    "Beef Roll": 400,
    "Beef Biryani": 650,
    "Beef Karahi": 750,
    "Beef Tikka": 600,
    "Vegetable Roll": 150, 
    "French Fries": 200,
    "Pizza Fries": 500,
    "Masala Fries": 250,
    "Soft Drink": 100,
    "Mineral Water": 50,
    "Tea": 30,
    "Coffee": 80,
    "Juice": 120,
    "Ice Cream": 150,
}

# Greeting the user
print("Welcome to the Cafe Management System!")
# Displaying the menu
print("\nHere is the menu:")
print("Zinger Roll - $300\n Chicken Roll - $200\n Chicken Burger - $450\n Chicken Sandwich - $350\n Chicken Nuggets - $250\n Chicken Wings - $400\n Chicken Shawarma - $500\n Chicken Biryani - $600\n Chicken Karahi - $700\n Chicken Tikka - $550\n Beef Burger - $500\n Beef Shawarma - $600\n Beef Roll - $400\n Beef Biryani - $650\n Beef Karahi - $750\n Beef Tikka - $600\n Vegetable Roll - $150\n French Fries - $200\n Pizza Fries - $500\n Masala Fries - $250\n Soft Drink - $100\n Mineral Water - $50\n Tea - $30\n Coffee - $80\n Juice - $120\n Ice Cream - $150")
Order_total = 0

# Function to take order in a loop
while True:
    item = input("\nPlease enter the item you want to order: ")
    if item in menu:
        Order_total += menu[item]
        print(f"{item} has been added to your order. Current total: ${Order_total}")
    else:
        print(f"Order item {item} is not available in the menu.")    
        another_order = input("Do you want to order another item? (yes/no): ").strip().lower()
        if another_order != 'yes':
            break
        print(f"Your final amount is ${Order_total}. Thank you for your order!")