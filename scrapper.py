import requests
from bs4 import BeautifulSoup
def extract_news():
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n' + '<br>' + '-' * 50 + '<br>')
    response = requests.get('https://news.ycombinator.com/')
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i + 1) + ' :: ' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
        # print(tag.prettify) #find_all('span',attrs={'class':'sitestr'}))
    return (cnt)

a= extract_news()
print(a)