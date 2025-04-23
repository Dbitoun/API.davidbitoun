import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#create an output file so we can see the json response that was
#returned by the API call
outfile = open('output.json', 'w')


response = r.json()

json.dump(response,outfile,indent=4)

list_of_repos = response['items']

#print out the number of repos returned from the API call
print(len(list_of_repos))

#Examine the first repo
first_repo = list_of_repos[0]

#number of keys in each repo
print(f"Number of Keys: {len(first_repo)}")

#print each key
for key in first_repo:
    print(key)

# EXCERCISE
# print out the full name, the html url, the license name, and the topics for the
# first repo

print(f"Full Name: {first_repo['full_name']}")
print(f"html url: {first_repo['owner']['html_url']}")
print(f"License Name: {first_repo['license']['name']}")

for topic in first_repo['topics']:
    print(f"Topic Name: {topic}")

#grab the top 10 repos based on star count and represent them on a bar chart

from plotly.graph_objs import Bar
from plotly import offline

repo_names,stars = [], []

for repo_dict in list_of_repos[:10]:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])


data = [
    {
        "type":"bar",
        "x":repo_names,
        "y":stars,
        "marker": {
            "color": "rgb(60,100,150)",
            "line":{"width":1.5, "color":"rgb(25,25,25)"}
        },
        "opacity":0.6
    }
]

my_layout = {
    "title": "Most streamed Python Repositories on GitHub",
    "xaxis":{"title":"Repository"},
    "yaxis":{"title":"Stars"},
}

fig = {"data":data, "layout":my_layout}

offline.plot(fig, filename="python_repos.html")