import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
subtext = soup.select('.subtext')

res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.a["href"]
        vote = votes[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 199:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn


arr = create_custom_hn(links, subtext)
arr2 = create_custom_hn(links2, subtext2)
arr3 = sort_stories_by_votes(arr+arr2)

for i in arr3:
    print(f'Title: {i['title']}, Votes: {i['votes']}, link: {i['link']}')
