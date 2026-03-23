from flask import Flask
import os
import time
import MySQLdb

app = Flask(__name__)

while True:
    try:
        db = MySQLdb.connect(
            host="mysql",
            user="root",
            passwd="root",
            db="testdb"
        )
        print("Connected to MySQL ✅")
        break
    except Exception as e:
        print("Waiting for MySQL...", e)
        time.sleep(2)

@app.route('/')
def home():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT 1")
        return "MySQL Connected ✅"
    except Exception as e:
        return f"Database connection failed! {e}"

@app.route('/health')
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
