import os
import psycopg2
from flask import Flask

app = Flask(__name__)

# DB connection info from environment
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

@app.route("/")
def hello():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        conn.close()
        return "Hello from web1! DB connection successful."
    except Exception as e:
        return f"Hello from web1! DB connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
