import sqlite3

def setup_database():
    conn = sqlite3.connect('hpc_data.db')
    
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keyword TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
