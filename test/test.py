import requests
from bs4 import BeautifulSoup

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text

def parse_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []

    for g in soup.find_all(class_='tF2Cxc'):
        title = g.find('h3')
        link = g.find('a')['href']
        snippet = g.find(class_='IsZvec')
        
        if title and link:
            title_text = title.text
            snippet_text = snippet.text if snippet else "No snippet available"
            results.append({
                'title': title_text,
                'link': link,
                'snippet': snippet_text
            })
    
    return results

def main():
    query = "NYU HPC"
    html = google_search(query)
    search_results = parse_results(html)
    
    if not search_results:
        print("No results found.")
    else:
        for result in search_results:
            print(f"Title: {result['title']}")
            print(f"Link: {result['link']}")
            print(f"Snippet: {result['snippet']}\n")

if __name__ == '__main__':
    main()
