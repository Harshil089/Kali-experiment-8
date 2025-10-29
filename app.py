from flask import Flask, request
import sqlite3
app = Flask(__name__)
@app.route('/')
def home():
    return '''
    <h1>Login</h1>
    <form method="POST" action="/login">
        Username: <input name="username"><br>
        Password: <input name="password"><br>
        <input type="submit">
    </form>
    '''
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # WARNING: vulnerable to SQL injection
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    c.execute(query)
    result = c.fetchone()
    conn.close()
    if result:
        return f"<h2>Welcome {username}!</h2>"
    else:
        return "<h2>Login Failed!</h2>"
if __name__ == "__main__":
    app.run(debug=True)
