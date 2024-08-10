import json

with open('content.json', 'r') as json_file:
    content = json.load(json_file)

with open('index.json', 'r') as index_file:
    index = json.load(index_file)

def search(query):
    query = query.lower()
    result_urls = index.get(query, []) 

    results = sorted(
        [item for item in content if item['url'] in [r[0] for r in result_urls]],
        key=lambda x: next((r[1] for r in result_urls if r[0] == x['url']), 0),
        reverse=True
    )

    if not results:
        print("No results found.")
        return

    for result in results:
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}.html")
        print(f"Snippet: {result['content'][:150]}...")
        print('-' * 80)

if __name__ == "__main__":
    while True:
        query = input("Enter search term (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        search(query)
