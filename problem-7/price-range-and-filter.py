# image moton kore logic banao. price range dibo, tahole oi price range er product gulo dekhabe. multiple filter choose korbo tahole oi filter gulor product dekhabe.

products = [
    {
        "id": 1,
        "name": "MacBook Air M3",
        "category": "Laptop",
        "brand": "Apple",
        "price": 1450,
        "availability": "In Stock",
        "rating": 4.9
    },
    {
        "id": 2,
        "name": "Dell XPS 15",
        "category": "Laptop",
        "brand": "Dell",
        "price": 1800,
        "availability": "Pre Order",
        "rating": 4.8
    },
    {
        "id": 3,
        "name": "Lenovo Legion 5",
        "category": "Laptop",
        "brand": "Lenovo",
        "price": 1650,
        "availability": "In Stock",
        "rating": 4.7
    },
    {
        "id": 4,
        "name": "iPhone 16",
        "category": "Mobile",
        "brand": "Apple",
        "price": 1200,
        "availability": "In Stock",
        "rating": 4.9
    },
    {
        "id": 5,
        "name": "Samsung Galaxy S25",
        "category": "Mobile",
        "brand": "Samsung",
        "price": 1100,
        "availability": "Pre Order",
        "rating": 4.8
    },
    {
        "id": 6,
        "name": "Google Pixel 10",
        "category": "Mobile",
        "brand": "Google",
        "price": 950,
        "availability": "Up Coming",
        "rating": 4.7
    },
    {
        "id": 7,
        "name": "Sony WH-1000XM6",
        "category": "Headphone",
        "brand": "Sony",
        "price": 400,
        "availability": "In Stock",
        "rating": 4.8
    },
    {
        "id": 8,
        "name": "AirPods Pro 3",
        "category": "Headphone",
        "brand": "Apple",
        "price": 280,
        "availability": "In Stock",
        "rating": 4.7
    },
    {
        "id": 9,
        "name": "Logitech MX Master 3S",
        "category": "Mouse",
        "brand": "Logitech",
        "price": 120,
        "availability": "Pre Order",
        "rating": 4.9
    },
    {
        "id": 10,
        "name": "Razer DeathAdder V3",
        "category": "Mouse",
        "brand": "Razer",
        "price": 90,
        "availability": "In Stock",
        "rating": 4.6
    } 
]

minimum_price = int(input("Please give Min Price "))
maximum_price = int(input("Please give Max price "))

availability = input ("Please type availability such as In Stock, Pre Order, Up Coming ")

print(minimum_price)
print(maximum_price)
print(availability)

availability_list = availability.split(",")
print(availability_list)

search_result = []

for product in products:
    if minimum_price <= product["price"] <= maximum_price and product["availability"] in availability_list:
            search_result.append(product)

if len(search_result) == 0: 
      
       print("No result found!!")
else: 
     print("Search Result", search_result)