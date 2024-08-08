from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_answer(question):
    conn = sqlite3.connect('hpc_data.db')
    c = conn.cursor()
    
    c.execute('SELECT answer FROM answers WHERE keyword LIKE ?', ('%' + question + '%',))
    result = c.fetchone()
    
    conn.close()
    
    if result:
        return result[0]
    return "Sorry, I don't understand your question. Please try again."

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')
    answer = get_answer(user_input)
    return jsonify({'question': user_input, 'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
