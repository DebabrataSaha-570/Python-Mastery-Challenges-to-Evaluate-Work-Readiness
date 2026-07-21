list_items = ["Machine Learning & AI Agent for Voice Data Analysis" ,"Data Analytics With Machine Learning", "Machine Learning for natural language processing", "Theory of machine learning of (A-Z) pre-recorded", "Data analytics with machine learning (offline)", "Machine Learning to AI agent development for software engineers"]


search_item = input("Search in here ")

searched_result = []

for i in list_items: 
    if search_item.lower() in i.lower():
        searched_result.append(i)

if len(searched_result) == 0:
    print("No result found!!")
else: 
    print("Search results", searched_result)

