#I will write category in the input and show products based on that category

products = [
    {
        "id": 1,
        "name": "MacBook Air M3",
        "category": "Laptop",
        "price": 1450
    },
    {
        "id": 2,
        "name": "Dell XPS 15",
        "category": "Laptop",
        "price": 1800
    },
    {
        "id": 3,
        "name": "iPhone 16",
        "category": "Mobile",
        "price": 1200
    },
    {
        "id": 4,
        "name": "Samsung Galaxy S25",
        "category": "Mobile",
        "price": 1100
    },
    {
        "id": 5,
        "name": "Sony WH-1000XM6",
        "category": "Headphone",
        "price": 400
    },
    {
        "id": 6,
        "name": "AirPods Pro 3",
        "category": "Headphone",
        "price": 280
    },
    {
        "id": 7,
        "name": "Logitech MX Master 3S",
        "category": "Mouse",
        "price": 120
    },
    {
        "id": 8,
        "name": "Razer DeathAdder V3",
        "category": "Mouse",
        "price": 90
    },
    {
        "id": 9,
        "name": "Keychron K8",
        "category": "Keyboard",
        "price": 110
    },
    {
        "id": 10,
        "name": "Royal Kludge RK84",
        "category": "Keyboard",
        "price": 75
    }
] 

input_category = input("Please write the category name: ")
searched_items = []

for i in products: 
    if i["category"] == input_category:
        searched_items.append(i)

if len(searched_items) == 0:
    print("No result found!!")
else:
    print("Searched result", searched_items)
