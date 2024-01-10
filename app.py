import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

GET_NUMBER_OF_TASKS = (
    "SELECT COUNT(*) as Count FROM tasks"
)

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test")
def test():
    return "<h1>Test New</h1>"


@app.route("/get_count")
def get_count():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_NUMBER_OF_TASKS)
            count = cursor.fetchone()[0]
    return "" + str(count)


if __name__ == "__main__":
    app.run(debug=True)
