import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
outfile = open('hn.json', 'w')
submission_ids = r.json()

json.dump(submission_ids,outfile,indent=4)

#Make another call to an API to get specific details for a story
url = 'https://hacker-news.firebaseio.com/v0/item/43614285.json'
r = requests.get(url)

outfile = open('hn2.json', 'w')
json.dump(r.json(), outfile, indent=4)

# Exercise
# Grab the top 10 stories and print out the Title, Discussion link and Comments.
# Sort it based on number of comments

sub_list = []

for sub_id in submission_ids[:10]:
    #make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{sub_id}.json"
    r = requests.get(url)
    #print(f"id: {sub_id}\t\tstatus{r.status_code}")

    #the response is a dictionary, so save it to a dictionary variable
    response_dict = r.json()

    #create a new dictionary of just the data you need
    a_dict = {
        'title':response_dict['title'],
        'hn_link':f"https://news.ycombinator.com/item?id={sub_id}",
        'comments':response_dict['descendants']
    }

    #add this dictionary to your final list
    sub_list.append(a_dict)

print(sub_list)

#sub_list = sorted(sub_list,key=lambda x:x['comments'], reverse=True)

from operator import itemgetter

sub_list = sorted(sub_list,key=itemgetter('comments'), reverse=True)

for d in sub_list:
    print(f"Title: {d['title']}")
    print(f"DIscussion link: {d['hn_link']}")
    print(f"No. of comments: {d['comments']}")