import os
import json
from bs4 import BeautifulSoup
from collections import defaultdict

html_dir = './html_files/'

index = defaultdict(list)  
content_list = []

for filename in os.listdir(html_dir):
    if filename.endswith(".html"):
        with open(os.path.join(html_dir, filename), 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')
            title = soup.title.string if soup.title else 'No Title'
            body = soup.get_text()
            url = filename.replace('.html', '')

            content_list.append({
                "title": title,
                "content": body,
                "url": url
            })

            words = body.lower().split()  
            for word in set(words):
                weight = 1
                if word in title.lower():
                    weight += 2  
                index[word].append((url, weight))

with open('content.json', 'w') as json_file:
    json.dump(content_list, json_file, indent=4)

with open('index.json', 'w') as index_file:
    json.dump(index, index_file, indent=4)
