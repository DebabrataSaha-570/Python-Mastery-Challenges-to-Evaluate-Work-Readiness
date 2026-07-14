total_items = int(input("how many Items of list you want? "))
items_per_page = int(input("How many Items per page you want? "))
page_number = int(input("Which page you want to go? "))

print(total_items)
print(items_per_page)
print(page_number)


list_items = []

for i in range (1, total_items+1):
    list_items.append(i)


pages = []

for i in range (0, len(list_items), items_per_page): 
    per_page = list_items[i:i+items_per_page]
 
    pages.append(per_page)

print("pages", pages)

print (f"page {page_number} items {pages[page_number-1]}")




