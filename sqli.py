import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin22')")
    c.execute("INSERT INTO users (username, password) VALUES ('user1', 'password123')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    # Get form data from POST request
    username = request.form.get('username')
    password = request.form.get('password')
    
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    # VULNERABLE: SQL Injection - string concatenation in query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Executing query:", query)
        
    try:
        c.execute(query)
        result = c.fetchone()
        conn.close()
        
        if result:
            return render_template('login.html', message="Login successful! ✓", message_type="success")
        else:
            return render_template('login.html', message="Login failed! Invalid credentials.", message_type="error")
    except Exception as e:
        conn.close()
        return render_template('login.html', message=f"Error: {str(e)}", message_type="error")

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
