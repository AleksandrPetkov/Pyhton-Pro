from flask import Flask, render_template
from utils1 import convert_data

app1 = Flask(__name__)


@app1.route('/')
def home_page():
    return render_template('home_page.html', title='Home page')


@app1.route('/avr_data')
def average_data():

    with open('hw.csv', encoding='utf-8') as f:
        result = convert_data(f.read())
        return render_template('avr_data.html', title='Average data', content=result)


app1.run(debug=True, port=2536)
