import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_data():
    url = 'https://hpc.nyu.edu/faq'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    faq_items = soup.find_all('div', class_='faq-item')
    data = []
    for item in faq_items:
        question = item.find('h3').text.strip()
        answer = item.find('div', class_='answer').text.strip()
        data.append((question, answer))

    return data

def update_database(data):
    conn = sqlite3.connect('hpc_data.db')
    c = conn.cursor()
    
    c.execute('DELETE FROM answers')
    
    for question, answer in data:
        c.execute('INSERT INTO answers (keyword, answer) VALUES (?, ?)', (question, answer))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    data = scrape_data()
    update_database(data)
