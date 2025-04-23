import requests
import json
import sys

#random chuch norris jokes
random_url = "https://api.chucknorris.io/jokes/random"


#list of categories
category_url = "https://api.chucknorris.io/jokes/categories"


#random joke from a specific category
random_cat_url = "https://api.chucknorris.io/jokes/random?category={category}"


#text search
search_url = "https://api.chucknorris.io/jokes/search?query={query}"




'''
Part I
The program should welcome the user by displaying a random chuch norris joke
'''
r = requests.get(random_url)
print(f"Status Code: {r.status_code}")

response_dict = r.json()

print("Welcome! Here's your first Chuck Norris joke:")
print(f"Joke: {response_dict['value']}")


'''
Part II
list the categories to the user and ask to pick a category
'''
r = requests.get(category_url)
print(f"Status Code: {r.status_code}")

categories = r.json()

print("Select Joke Catagories:\n")
for cat in categories:
    print(cat)

user_choice = input("Enter a category from the list above: \n").lower()

if user_choice in categories:
    print(f"You selected the '{user_choice}' category!")
else:
    print("Invalid category selected")



'''
Part III
Display a joke based on the category picked by the user
'''



'''
Part IV
See if you can find a match for the user's favorite chuck norris joke
by asking the user to enter in a few key words of the joke
'''


