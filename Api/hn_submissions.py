from operator import itemgetter

import requests
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
submission_dics = []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dic = r.json()

    #build a dictionary for each submission
    submission_dic = {
        'title': response_dic['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dic['descendants'],
    }
    submission_dics.append(submission_dic)

    submission_dics = sorted(submission_dics, key=itemgetter('comments'), reverse=True)

    for submission_dic in submission_dics:
        print(f"\nTitle: {submission_dic['title']}")
        print(f"Disccusion: {submission_dic['hn_link']}")
        print(f"Comments: {submission_dic['comments']}")
    
