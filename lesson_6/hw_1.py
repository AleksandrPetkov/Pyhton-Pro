from flask import Flask
from utils import get_formated_text

app = Flask(__name__)


@app.route("/")
def view():
    """Функция для отображения данных в браузере."""
    with open('requirements.txt', encoding='utf-8') as f:
        result = get_formated_text(f.read())
        return result


app.run(debug=True)
