from flask import Flask, request
import os
import sqlite3
app = Flask(__name__)
# Função para criar a tabela 'users' no banco de dados
def create_table():
    db_path = os.path.abspath('../data/database.sqlite')
    print("VAI PRINTAR")
    print(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
@app.route('/')
def hello():
    return 'Tanaria feia'
@app.route('/create_table')
def create_table_route():
    create_table()
    return 'Table created successfully!'

@app.route('/post', methods=['POST'])  # Use 'methods' instead of the second argument
def post_teste():
    data = request.get_json()  # Assuming you're sending JSON data in the request
    print(data)
    return data  # You can return the data or any response you want
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 