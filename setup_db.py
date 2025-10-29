import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
''')
# Add sample data
c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
c.execute("INSERT INTO users (username, password) VALUES ('user', 'user123')")
conn.commit()
conn.close()
print("Database setup complete!")
